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
    try { cfg = JSON.parse(container.getAttribute('data-config')||'{}'); } catch(e){ cfg = {}; }
    const nTeams = Math.max(1, parseInt(cfg.teams||1,10));
    const categories = cfg.categories||[];
  const values = (cfg.values||[]).slice().sort(function(a,b){return a-b;});

  // Track per-tile state: whether points have been allocated/deallocated
  const tileStates = Object.create(null); // key: "ci|value" -> { locked: true }
  const categoryStats = categories.map(()=>({correct:0, wrong:0}));
  let totalPlayableTiles = 0;
  let scoreboardShown = false;

    // Build top score bar
    const scorebar = document.createElement('div');
    scorebar.className = 'jeopardy-scorebar';

  const teams = [];
  const teamCategoryPoints = Array.from({length: nTeams}, () => Array.from({length: categories.length}, () => 0));
    for(let i=0;i<nTeams;i++){
      const team = { name: `Lagnavn ${i+1}`, score: 0 };
      teams.push(team);
      const el = document.createElement('div');
      el.className = 'jeopardy-team';
      const nameInput = document.createElement('input');
      nameInput.className = 'team-name';
      nameInput.value = team.name;
      nameInput.addEventListener('input', ()=>{ team.name = nameInput.value; });
      const scoreSpan = document.createElement('span');
      scoreSpan.className = 'score';
      scoreSpan.textContent = '0';
      el.appendChild(nameInput);
      el.appendChild(scoreSpan);
      scorebar.appendChild(el);
      team._elScore = scoreSpan;
    }

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
    const closeBtn = document.createElement('button'); closeBtn.className='j-btn warn'; closeBtn.textContent='Lukk';
    const body = document.createElement('div'); body.className='jeopardy-modal-body';
    const footer = document.createElement('div'); footer.className='jeopardy-modal-footer';

    header.appendChild(title); header.appendChild(closeBtn);
    modal.appendChild(header); modal.appendChild(body); modal.appendChild(footer);
    backdrop.appendChild(modal);

    function setScore(i, delta){ teams[i].score += delta; teams[i]._elScore.textContent = String(teams[i].score); }
    let escHandler = null;
    const hideModal = ()=>{ 
      backdrop.style.display = 'none'; 
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

    function openModal(category, value, data, tile, key){
      title.textContent = `${category} – ${value}`;
      body.innerHTML = '';
      footer.innerHTML = '';

      const q = document.createElement('div'); q.className='jeopardy-q'; q.innerHTML = data && data.question ? data.question : '';
      const a = document.createElement('div'); a.className='jeopardy-a'; a.innerHTML = data && data.answer ? data.answer : '';

      const actions = document.createElement('div'); actions.className='jeopardy-actions';
      const revealBtn = document.createElement('button'); revealBtn.className='j-btn secondary'; revealBtn.textContent='Fasit';
      revealBtn.addEventListener('click', ()=>{ a.style.display = a.style.display==='block' ? 'none' : 'block'; });
      actions.appendChild(revealBtn);

  body.appendChild(q); body.appendChild(actions); body.appendChild(a);

      // Team +/- buttons for this value
      let scored = false; // prevent multiple allocations for this tile in this session
      const teamActions = document.createElement('div'); teamActions.className='jeopardy-team-actions';
      const disableTeamButtons = () => {
        teamActions.querySelectorAll('button').forEach(b=>{ b.disabled = true; });
      };
      teams.forEach((t, i)=>{
        const add = document.createElement('button'); add.className='j-btn primary'; add.textContent = `+${value} ${t.name}`;
        const sub = document.createElement('button'); sub.className='j-btn secondary'; sub.textContent = `-${value} ${t.name}`;
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
          // Auto-close the modal after scoring with a brief delay
          try { setTimeout(()=>{ hideModal(); checkCompletionAndShowWinner(); }, 300); } catch(e){}
        };
        add.addEventListener('click', ()=> handle(value));
        sub.addEventListener('click', ()=> handle(-value));
        // If already locked from earlier, disable buttons
        if (tileStates[key] && tileStates[key].locked) { add.disabled = true; sub.disabled = true; }
        teamActions.appendChild(add); teamActions.appendChild(sub);
      });
      footer.appendChild(teamActions);

  renderMathIfAvailable(q); renderMathIfAvailable(a);
  highlightCodeIfAvailable(q); highlightCodeIfAvailable(a);

      backdrop.style.display = 'flex';
      enableEscClose();
      closeBtn.onclick = hideModal; backdrop.onclick = (e)=>{ if(e.target===backdrop) hideModal(); };
    }

    // Assemble
    container.innerHTML = '';
    container.appendChild(scorebar);
    container.appendChild(table);
    container.appendChild(backdrop);
  }

  document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.jeopardy-container[data-config]').forEach(initJeopardy);
  });
})();
