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

  function initEscapeRoom(container){
    let cfg = null;
    try { cfg = JSON.parse(container.getAttribute('data-config')||'{}'); } catch(e){ cfg = {}; }
    const steps = Array.isArray(cfg.steps) ? cfg.steps : [];
    const caseInsensitive = !!cfg.caseInsensitive;

    // Build UI
    const root = document.createElement('div');
    root.className = 'er-root';

    const header = document.createElement('div');
    header.className = 'er-header';
    const progress = document.createElement('div');
    progress.className = 'er-progress';
    header.appendChild(progress);

    const body = document.createElement('div');
    body.className = 'er-body';

  const controls = document.createElement('div');
    controls.className = 'er-controls';
    const codeInput = document.createElement('input'); codeInput.type = 'text'; codeInput.placeholder = 'Skriv kode';
    const submitBtn = document.createElement('button'); submitBtn.className='er-btn primary'; submitBtn.textContent='Sjekk';
    const feedback = document.createElement('div'); feedback.className='er-feedback';
    controls.appendChild(codeInput); controls.appendChild(submitBtn);

    root.appendChild(header); root.appendChild(body); root.appendChild(controls); root.appendChild(feedback);

    let idx = 0;
    // Avoid auto-scrolling on initial load by not auto-focusing until user interacts
    let userInitiated = false;
    const markUserInitiated = ()=>{ userInitiated = true; try { codeInput.focus({ preventScroll: true }); } catch(e){ try { codeInput.focus(); } catch(_){} } };
    try {
      container.addEventListener('pointerdown', markUserInitiated, { once: true, capture: true });
      container.addEventListener('keydown', function onKey(){ userInitiated = true; container.removeEventListener('keydown', onKey, true); }, true);
    } catch(e){}

    function normalizeCode(s){
      const t = String(s||'').trim();
      return caseInsensitive ? t.toLowerCase() : t;
    }

    function updateProgress(){
      progress.textContent = `Rom ${Math.min(idx+1, steps.length)} av ${steps.length}`;
    }

    function renderStep(){
      body.innerHTML = '';
      feedback.textContent = '';
      updateProgress();
      if (idx >= steps.length){
        const done = document.createElement('div');
        done.className = 'er-complete';
        done.innerHTML = '<h3> Ferdig! 🎉</h3>';
        body.appendChild(done);
        controls.style.display = 'none';
        return;
      }
      controls.style.display = '';
      const step = steps[idx] || {};
      const title = document.createElement('h3'); title.className='er-title'; title.textContent = step.title || `Oppgave ${idx+1}`;
      const q = document.createElement('div'); q.className='er-q'; q.innerHTML = step.question || '';
      body.appendChild(title); body.appendChild(q);
      renderMathIfAvailable(q); highlightCodeIfAvailable(q);
      codeInput.value = '';
      if (userInitiated) {
        try { codeInput.focus({ preventScroll: true }); } catch(e){ try { codeInput.focus(); } catch(_){} }
      }
    }

    function check(){
      const step = steps[idx] || {};
      const allowed = Array.isArray(step.codes) ? step.codes : [];
      const entered = normalizeCode(codeInput.value);
      const ok = allowed.map(normalizeCode).includes(entered);
      if (ok){
        feedback.textContent = '';
        idx += 1;
        renderStep();
      } else {
        feedback.textContent = 'Feil kode. Prøv igjen.';
        feedback.classList.add('er-error');
        setTimeout(()=>{ feedback.classList.remove('er-error'); }, 500);
      }
    }

    submitBtn.addEventListener('click', check);
    codeInput.addEventListener('keydown', function(e){
      if (e.key === 'Enter') { e.preventDefault(); check(); }
    });

    container.innerHTML = '';
    container.appendChild(root);
    renderStep();
  }

  document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.escape-room-container[data-config]').forEach(initEscapeRoom);
  });
})();
