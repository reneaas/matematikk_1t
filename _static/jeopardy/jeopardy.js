(function(){
  function renderMathIfAvailable(root){
    if (typeof renderMathInElement === 'function') {
      try { renderMathInElement(root, {delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false},
        {left: '\\(', right: '\\)', display: false},
        {left: '\\[', right: '\\]', display: true}
      ]}); } catch(e){}
    }
  }

  function highlightCodeIfAvailable(root){
    if (typeof hljs !== 'undefined' && root) {
      try {
        root.querySelectorAll('pre code').forEach(function(block){
          hljs.highlightElement(block);
        });
      } catch(e){}
    }
  }

  function initJeopardy(container){
    let cfg = null;
    try {
      // Prefer inline JSON script to avoid attribute escaping issues
      const dataNode = container.querySelector('script.jeopardy-data[type="application/json"]');
      let raw = dataNode ? (dataNode.textContent || dataNode.innerText || '') : '';
      if (!raw || !raw.trim()) {
        raw = container.getAttribute('data-config') || '{}';
      }
      // Fallback: decode common HTML entities if present
      if (raw && raw.indexOf('&') !== -1 && raw.indexOf('{') === -1) {
        const ta = document.createElement('textarea'); ta.innerHTML = raw; raw = ta.value;
      }
      cfg = JSON.parse(raw);
    } catch(e){ cfg = {}; }
  // Default to 2 teams unless overridden by config
  const nTeams = Math.max(1, parseInt(cfg.teams||2,10));
    const categories = cfg.categories||[];
  const values = (cfg.values||[]).slice().sort(function(a,b){return a-b;});

  // Track per-tile state: whether points have been allocated/deallocated
  const tileStates = Object.create(null); // key: "ci|value" -> { locked: true }
  const categoryStats = categories.map(()=>({correct:0, wrong:0}));
  let totalPlayableTiles = 0;
  let scoreboardShown = false;
  // Pre-game and runtime options
  let gameMode = 'duel'; // 'turn' | 'duel'
  let timerMs = 0; // 0 => no timer
  let currentTurn = 0;
  let started = false;

    // Build top score bar
  const scorebar = document.createElement('div');
  scorebar.className = 'jeopardy-scorebar';
  // Hide scorebar until the game has started
  scorebar.style.display = 'none';
  const turnIndicator = document.createElement('div');
  turnIndicator.className = 'jeopardy-turn-indicator';
  turnIndicator.style.display = 'none';

  let teams = [];
  let teamCategoryPoints = Array.from({length: nTeams}, () => Array.from({length: categories.length}, () => 0));
  function updateActiveTeamHighlight(){
    teams.forEach((t,i)=>{
      if (!t._el) return;
      if (gameMode==='turn' && i===currentTurn) t._el.classList.add('active');
      else t._el.classList.remove('active');
    });
    // Update visible turn text
    if (turnIndicator) {
      if (gameMode==='turn' && started && teams.length>0) {
        turnIndicator.style.display = '';
        turnIndicator.textContent = `Tur: ${teams[currentTurn].name}`;
      } else {
        turnIndicator.style.display = 'none';
        turnIndicator.textContent = '';
      }
    }
  }
  function rebuildTeams(newN, names){
    teams = [];
    scorebar.innerHTML = '';
    teamCategoryPoints = Array.from({length: newN}, () => Array.from({length: categories.length}, () => 0));
    for(let i=0;i<newN;i++){
      const team = { name: names && names[i] ? names[i] : `Lag ${i+1}`, score: 0 };
      teams.push(team);
      const el = document.createElement('div');
      el.className = 'jeopardy-team';
      const nameSpan = document.createElement('span');
      nameSpan.className = 'team-name';
      nameSpan.textContent = team.name;
      const scoreSpan = document.createElement('span');
      scoreSpan.className = 'score';
      scoreSpan.textContent = '0';
      el.appendChild(nameSpan);
      el.appendChild(scoreSpan);
      scorebar.appendChild(el);
      team._elScore = scoreSpan;
      team._el = el;
    }
    updateActiveTeamHighlight();
  }
  // Do not render teams until the game starts

    // Build grid as table
    const table = document.createElement('table');
    table.className = 'jeopardy-grid';

    const thead = document.createElement('thead');
    const thr = document.createElement('tr');
    categories.forEach(cat=>{
      const th = document.createElement('th');
      th.textContent = cat.name||'';
      thr.appendChild(th);
    });
    thead.appendChild(thr);

    const tbody = document.createElement('tbody');

    // create a quick map for lookup by category+value
    const lookup = {};
    categories.forEach((cat,ci)=>{
      (cat.tiles||[]).forEach(t=>{
        const key = ci+'|'+t.value;
        lookup[key] = t;
      });
    });
    totalPlayableTiles = Object.keys(lookup).length;

    values.forEach(val=>{
      const tr = document.createElement('tr');
      categories.forEach((cat,ci)=>{
        const td = document.createElement('td');
        const tile = document.createElement('button');
        tile.className = 'jeopardy-tile';
        tile.textContent = val;
        const key = ci+'|'+val;
        tile.dataset.key = key;
        const data = lookup[key] || null;
        if(!data){ tile.disabled = true; tile.classList.add('used'); }
        if (tileStates[key] && tileStates[key].locked) { tile.disabled = true; tile.classList.add('used'); }
        tile.addEventListener('click', ()=>{
          if(tile.classList.contains('used')||tile.disabled) return;
          if (!started) return;
          openModal(cat.name||'', val, data, tile, key);
        });
        td.appendChild(tile);
        tr.appendChild(td);
      });
      tbody.appendChild(tr);
    });

    table.appendChild(thead); table.appendChild(tbody);

    // Modal UI
    const backdrop = document.createElement('div');
    backdrop.className = 'jeopardy-modal-backdrop';
    const modal = document.createElement('div');
    modal.className = 'jeopardy-modal';
  const header = document.createElement('div'); header.className='jeopardy-modal-header';
  const title = document.createElement('div');
  const timerBox = document.createElement('div'); timerBox.className='jeopardy-timer'; timerBox.style.marginLeft='auto';
  const closeBtn = document.createElement('button'); closeBtn.className='j-btn warn'; closeBtn.textContent='Lukk';
    const body = document.createElement('div'); body.className='jeopardy-modal-body';
    const footer = document.createElement('div'); footer.className='jeopardy-modal-footer';

  header.appendChild(title); header.appendChild(timerBox); header.appendChild(closeBtn);
    modal.appendChild(header); modal.appendChild(body); modal.appendChild(footer);
    backdrop.appendChild(modal);

    function setScore(i, delta){ teams[i].score += delta; teams[i]._elScore.textContent = String(teams[i].score); }
    let escHandler = null;
    const hideModal = ()=>{ 
      backdrop.style.display = 'none'; 
      try { if (typeof stopTimer === 'function') stopTimer(); } catch(e){}
      if (escHandler) { 
        try { document.removeEventListener('keydown', escHandler); } catch(e){}
        escHandler = null; 
      }
    };
    function enableEscClose(){
      // Ensure only one active handler
      if (escHandler) {
        try { document.removeEventListener('keydown', escHandler); } catch(e){}
        escHandler = null;
      }
      escHandler = function(e){
        const key = e.key || e.code;
        if (key === 'Escape' || key === 'Esc') {
          try { e.preventDefault(); } catch(_){}
          hideModal();
        }
      };
      try { document.addEventListener('keydown', escHandler); } catch(e){}
    }
    function checkCompletionAndShowWinner(){
      if (scoreboardShown) return;
      if (totalPlayableTiles <= 0) return;
      let lockedCount = 0;
      for (const k in tileStates) { if (tileStates[k] && tileStates[k].locked) lockedCount++; }
      if (lockedCount >= totalPlayableTiles) {
        scoreboardShown = true;
        openWinner();
      }
    }
    function openWinner(){
      // Build a scoreboard sorted by score desc
      const sorted = teams.map((t,i)=>({name:t.name, score:t.score, idx:i}))
                          .sort((a,b)=> b.score - a.score);
      const max = sorted.length ? sorted[0].score : 0;
      const winners = sorted.filter(x=> x.score === max);
      title.textContent = winners.length > 1 ? 'Scoreboard' : 'Scoreboard';
      body.innerHTML = '';
      footer.innerHTML = '';
      // Build a table-like grid: Team | category1 | ... | categoryN | Score
      const grid = document.createElement('div');
      const cols = 2 + categories.length; // Team + categories... + Score
      grid.style.display = 'grid';
      grid.style.gridTemplateColumns = `1.5fr ${'auto '.repeat(categories.length)} auto`;
      grid.style.gap = '0.5rem 1rem';
      // Header row
      const hTeam = document.createElement('div'); hTeam.style.fontWeight = '700'; hTeam.textContent = 'Lag';
      grid.appendChild(hTeam);
      categories.forEach(cat => {
        const h = document.createElement('div'); h.style.fontWeight='700'; h.textContent = cat.name||''; grid.appendChild(h);
      });
      const hScore = document.createElement('div'); hScore.style.fontWeight='700'; hScore.textContent = 'Score';
      grid.appendChild(hScore);
      // Rows
      sorted.forEach(t => {
        const rowBold = (t.score === max);
        const name = document.createElement('div'); name.textContent = t.name; if (rowBold) name.style.fontWeight = '700'; grid.appendChild(name);
        const pointsRow = teamCategoryPoints[t.idx] || [];
        categories.forEach((_, ci) => {
          const cell = document.createElement('div');
          const val = pointsRow[ci] || 0;
          cell.textContent = String(val);
          if (rowBold) cell.style.fontWeight = '700';
          grid.appendChild(cell);
        });
        const sc = document.createElement('div'); sc.textContent = String(t.score); if (rowBold) sc.style.fontWeight = '700'; grid.appendChild(sc);
      });
      body.appendChild(grid);
      backdrop.style.display = 'flex';
      enableEscClose();
      closeBtn.onclick = hideModal; backdrop.onclick = (e)=>{ if(e.target===backdrop) hideModal(); };
    }

    // Timer utilities for modal
    let countdownId = null;
    function stopTimer(){ if (countdownId) { try { clearInterval(countdownId); } catch(e){} countdownId = null; } timerBox.textContent=''; }
    function startTimer(onTimeout){
      stopTimer();
      if (!timerMs || timerMs <= 0) return;
      let remaining = Math.floor(timerMs/1000);
      const render = () => { timerBox.textContent = `${Math.floor(remaining/60)}:${String(remaining%60).padStart(2,'0')}`; };
      render();
      countdownId = setInterval(()=>{
        remaining -= 1;
        if (remaining <= 0){ stopTimer(); try { onTimeout && onTimeout(); } catch(e){} }
        else render();
      }, 1000);
    }

    function openModal(category, value, data, tile, key){
      title.textContent = `${category} – ${value}`;
      body.innerHTML = '';
      footer.innerHTML = '';

      const q = document.createElement('div'); q.className='jeopardy-q'; q.innerHTML = data && data.question ? data.question : '';
      const a = document.createElement('div'); a.className='jeopardy-a'; a.innerHTML = data && data.answer ? data.answer : '';

      // Create the reveal (Fasit) button that will live in the footer (right side)
      const revealBtn = document.createElement('button'); revealBtn.className='j-btn success'; revealBtn.textContent='Fasit';
      revealBtn.addEventListener('click', ()=>{
        // Toggle visibility of the answer
        const showing = a.style.display !== 'block';
        a.style.display = showing ? 'block' : 'none';
        // After toggling, scroll the modal body to the bottom so the answer is visible
        try {
          // Allow layout to settle before scrolling
          setTimeout(()=>{
            if (typeof body.scrollTo === 'function') {
              body.scrollTo({ top: body.scrollHeight, behavior: 'smooth' });
            } else {
              body.scrollTop = body.scrollHeight;
            }
          }, 0);
        } catch(e){
          try { body.scrollTop = body.scrollHeight; } catch(_e){}
        }
      });
  body.appendChild(q); body.appendChild(a);

      // Team +/- buttons for this value
      let scored = false; // prevent multiple allocations for this tile in this session
      const teamActions = document.createElement('div'); teamActions.className='jeopardy-team-actions';
      const disableTeamButtons = () => {
        teamActions.querySelectorAll('button').forEach(b=>{ b.disabled = true; });
      };
      const onTimeout = ()=>{
        disableTeamButtons();
        if (gameMode==='turn' && teams.length>0){ currentTurn = (currentTurn+1)%teams.length; updateActiveTeamHighlight(); }
        try { setTimeout(()=>{ hideModal(); }, 300); } catch(e){}
      };
      teams.forEach((t, i)=>{
        // In turn-based mode, only show buttons for the active team
        if (gameMode==='turn' && i!==currentTurn) return;
  const add = document.createElement('button'); add.className='j-btn primary'; add.textContent = `+${value} ${t.name}`;
  const sub = document.createElement('button'); sub.className='j-btn warn'; sub.textContent = `-${value} ${t.name}`;
        const handle = (delta)=>{
          if (scored) return;
          if (tileStates[key] && tileStates[key].locked) return;
          setScore(i, delta);
          scored = true;
          tileStates[key] = { locked: true };
          // Update per-category stats
          try {
            const ci = parseInt(String(key).split('|')[0], 10);
            if (!isNaN(ci) && categoryStats[ci]) {
              if (delta > 0) categoryStats[ci].correct++;
              else if (delta < 0) categoryStats[ci].wrong++;
            }
            // Track points per team per category
            if (!isNaN(ci) && teamCategoryPoints[i]) {
              if (typeof teamCategoryPoints[i][ci] !== 'number') teamCategoryPoints[i][ci] = 0;
              teamCategoryPoints[i][ci] += delta;
            }
          } catch(e){}
          // Lock the tile so it cannot be opened again
          if (tile) { tile.classList.add('used'); tile.disabled = true; }
          // Disable further team actions for this question
          disableTeamButtons();
          if (gameMode==='turn' && teams.length>0){ currentTurn = (currentTurn+1)%teams.length; updateActiveTeamHighlight(); }
          // Auto-close the modal after scoring with a brief delay
          try { setTimeout(()=>{ hideModal(); checkCompletionAndShowWinner(); }, 300); } catch(e){}
        };
        add.addEventListener('click', ()=> handle(value));
        sub.addEventListener('click', ()=> handle(-value));
        // If already locked from earlier, disable buttons
        if (tileStates[key] && tileStates[key].locked) { add.disabled = true; sub.disabled = true; }
        teamActions.appendChild(add); teamActions.appendChild(sub);
      });
  // Footer layout: team +/- buttons on the left, Fasit button pinned to the right
  const footerRight = document.createElement('div');
  footerRight.className = 'jeopardy-footer-right';
  footerRight.appendChild(revealBtn);
  footer.appendChild(teamActions);
  footer.appendChild(footerRight);

  renderMathIfAvailable(q); renderMathIfAvailable(a);
  highlightCodeIfAvailable(q); highlightCodeIfAvailable(a);

      backdrop.style.display = 'flex';
      enableEscClose();
      startTimer(onTimeout);
      closeBtn.onclick = hideModal; backdrop.onclick = (e)=>{ if(e.target===backdrop) hideModal(); };
    }

    // Pre-game setup UI
    const setup = document.createElement('div'); setup.className='jeopardy-setup';
    const fTeams = document.createElement('div'); fTeams.className='jp-field';
    const lTeams = document.createElement('label'); lTeams.textContent='Antall lag:'; const sTeams=document.createElement('select');
    [1,2,3,4,5,6].forEach(n=>{ const opt=document.createElement('option'); opt.value=String(n); opt.textContent=String(n); if(n===nTeams) opt.selected=true; sTeams.appendChild(opt); });
    fTeams.appendChild(lTeams); fTeams.appendChild(sTeams);
    const namesWrap = document.createElement('div'); namesWrap.className='jp-names';
    function renderNames(){ namesWrap.innerHTML=''; const n=parseInt(sTeams.value,10)||1; for(let i=0;i<n;i++){ const row=document.createElement('div'); row.className='jp-name-row'; const lbl=document.createElement('label'); lbl.textContent=`Lagnavn ${i+1}`; const inp=document.createElement('input'); inp.type='text'; inp.value=`Lag ${i+1}`; row.appendChild(lbl); row.appendChild(inp); namesWrap.appendChild(row);} }
    sTeams.addEventListener('change', renderNames); renderNames();
    const fTimer=document.createElement('div'); fTimer.className='jp-field'; const lTimer=document.createElement('label'); lTimer.textContent='Timer:'; const sTimer=document.createElement('select'); [{label:'∞',ms:0},{label:'30s',ms:30000},{label:'1 min',ms:60000},{label:'2 min',ms:120000}].forEach((t,i)=>{ const opt=document.createElement('option'); opt.value=String(t.ms); opt.textContent=t.label; if(i===0) opt.selected=true; sTimer.appendChild(opt);}); fTimer.appendChild(lTimer); fTimer.appendChild(sTimer);
    const fMode=document.createElement('div'); fMode.className='jp-field'; const lMode=document.createElement('label'); lMode.textContent='Modus:'; const sMode=document.createElement('select'); [{v:'turn',t:'Turn-based'},{v:'duel',t:'Duell'}].forEach(m=>{ const opt=document.createElement('option'); opt.value=m.v; opt.textContent=m.t; if(m.v==='duel') opt.selected=true; sMode.appendChild(opt);}); fMode.appendChild(lMode); fMode.appendChild(sMode);
    const startBtn=document.createElement('button'); startBtn.className='j-btn primary'; startBtn.textContent='Start spill';
    startBtn.addEventListener('click', ()=>{
      const newN = parseInt(sTeams.value,10)||1;
      const names = Array.from(namesWrap.querySelectorAll('input')).map((inp,i)=> inp.value && inp.value.trim() ? inp.value.trim() : `Lag ${i+1}`);
      gameMode = sMode.value==='turn' ? 'turn' : 'duel';
      timerMs = parseInt(sTimer.value,10)||0;
      // Randomize who starts to avoid always starting with first team
      currentTurn = Math.floor(Math.random()*Math.max(1,newN));
      // Mark game as started before building UI so indicator shows immediately
      started = true;
      rebuildTeams(newN, names);
      // Show the scorebar now that the game has started
      try { scorebar.style.display = ''; } catch(e){}
      // Ensure indicator reflects the randomized start
      try { updateActiveTeamHighlight(); } catch(e){}
      setup.style.display='none';
    });
    setup.appendChild(fTeams); setup.appendChild(namesWrap); setup.appendChild(fTimer); setup.appendChild(fMode); setup.appendChild(startBtn);

    // Assemble
    container.innerHTML = '';
    container.appendChild(setup);
  container.appendChild(scorebar);
  container.appendChild(turnIndicator);
    container.appendChild(table);
    container.appendChild(backdrop);
  }

  document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.jeopardy-container[data-config]').forEach(initJeopardy);
  });
})();
