/* Progressive enhancement: the complete catalog is readable without JavaScript. */
(() => {
  'use strict';
  const $ = (selector, scope = document) => scope.querySelector(selector);
  const $$ = (selector, scope = document) => [...scope.querySelectorAll(selector)];
  const data = JSON.parse($('#survey-data').textContent);
  const papers = data.papers;
  const byId = new Map(papers.map(paper => [paper.id, paper]));
  const list = $('#paper-list');
  const cards = new Map($$('.paper-card').map(card => [card.dataset.paperId, card]));
  const stageIds = data.stages.map(stage => stage.id);
  const categories = data.stages.flatMap(stage => stage.categories.map(category => category.id));
  const normalize = value => String(value).normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const searchIndex = new Map(papers.map(p => [p.id, normalize([p.name, p.title, p.authors, p.venue, p.venue_label, ...p.categories.map(id => data.categoryNames[id])].join(' '))]));
  const PAGE_SIZE = 12;
  let limit = PAGE_SIZE;
  const defaults = () => ({q: '', stage: '', category: '', year: '', type: '', code: false, sort: 'newest'});
  let state = defaults();
  const fields = {q: $('#paper-search'), year: $('#year-filter'), category: $('#category-filter'), type: $('#type-filter'), sort: $('#sort-filter'), code: $('#code-filter')};
  function readURL() {
    const params = new URLSearchParams(location.search);
    state = defaults();
    state.q = (params.get('q') || '').slice(0, 500);
    state.stage = stageIds.includes(params.get('stage')) ? params.get('stage') : '';
    state.category = categories.includes(params.get('category')) ? params.get('category') : '';
    if (state.category) state.stage = state.category.split('/')[0];
    state.year = papers.some(p => String(p.year) === params.get('year')) ? params.get('year') : '';
    state.type = ['core', 'enabling'].includes(params.get('type')) ? params.get('type') : '';
    state.sort = ['newest', 'oldest', 'name'].includes(params.get('sort')) ? params.get('sort') : 'newest';
    state.code = params.get('code') === '1';
    limit = PAGE_SIZE;
  }
  function writeURL() {
    try {
      const url = new URL(location.href);
      Object.keys(state).forEach(key => {
        url.searchParams.delete(key);
        const value = state[key];
        if (value && !(key === 'sort' && value === 'newest')) url.searchParams.set(key, value === true ? '1' : value);
      });
      history.replaceState(null, '', url);
    } catch (_) { /* Some browsers disallow history changes on file URLs. */ }
  }
  function syncControls() {
    for (const [key, field] of Object.entries(fields)) {
      if (key === 'code') field.checked = state.code;
      else if (field.value !== state[key]) field.value = state[key];
    }
    $$('.stage-filter').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.stage === state.stage)));
    $$('#category-filter option[data-stage]').forEach(option => { option.disabled = !!state.stage && option.dataset.stage !== state.stage; });
    $('#reset-filters').hidden = !Object.keys(state).some(key => key === 'sort' ? state[key] !== 'newest' : !!state[key]);
  }
  function render(resetLimit = false, updateURL = true) {
    if (resetLimit) limit = PAGE_SIZE;
    const terms = normalize(state.q.trim()).split(/\s+/).filter(Boolean);
    const matched = papers.filter(p => terms.every(term => searchIndex.get(p.id).includes(term)) &&
      (!state.stage || p.categories.some(id => id.startsWith(state.stage + '/'))) &&
      (!state.category || p.categories.includes(state.category)) &&
      (!state.year || String(p.year) === state.year) &&
      (!state.type || (state.type === 'enabling' ? p.enabling : !p.enabling)) && (!state.code || !!p.code_url));
    const sorted = [...matched].sort((a, b) => state.sort === 'name' ? a.name.localeCompare(b.name) :
      (state.sort === 'oldest' ? a.year - b.year : b.year - a.year) || a.name.localeCompare(b.name));
    cards.forEach(card => { card.hidden = true; });
    const fragment = document.createDocumentFragment();
    sorted.forEach((paper, index) => { const card = cards.get(paper.id); card.hidden = index >= limit; fragment.appendChild(card); });
    list.appendChild(fragment);
    const count = sorted.length;
    const shown = Math.min(count, limit);
    $('#result-count').textContent = count + (count === 1 ? ' paper' : ' papers') + ' · ' + papers.length + ' in the collection';
    $('#empty-state').hidden = count !== 0;
    $('#load-more').hidden = shown >= count;
    $('#load-more').textContent = 'Show ' + Math.min(PAGE_SIZE, count - shown) + ' more papers ↓';
    $('#page-progress').textContent = count ? 'Showing ' + shown + ' of ' + count + ' papers' : '';
    syncControls();
    if (updateURL) writeURL();
  }
  function reset() { state = defaults(); render(true); }
  for (const [key, field] of Object.entries(fields)) {
    field.addEventListener(key === 'q' ? 'input' : 'change', () => {
      state[key] = key === 'code' ? field.checked : field.value;
      if (key === 'category' && state.category) state.stage = state.category.split('/')[0];
      render(true);
    });
  }
  $$('.stage-filter').forEach(button => button.addEventListener('click', () => {
    state.stage = button.dataset.stage;
    if (state.category && !state.category.startsWith(state.stage + '/')) state.category = '';
    render(true);
  }));
  $('#reset-filters').addEventListener('click', reset);
  $('#empty-reset').addEventListener('click', reset);
  $('#load-more').addEventListener('click', () => {
    const oldLimit = limit; limit += PAGE_SIZE; render();
    $$('.paper-card:not([hidden])')[oldLimit]?.querySelector('a')?.focus({preventScroll: true});
  });
  document.addEventListener('click', event => {
    const target = event.target.closest('[data-filter-category], [data-filter-stage]');
    if (!target || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault(); state = defaults();
    if (target.dataset.filterCategory) { state.category = target.dataset.filterCategory; state.stage = state.category.split('/')[0]; }
    else state.stage = target.dataset.filterStage;
    render(true);
    try { history.replaceState(null, '', location.pathname + location.search + '#papers'); } catch (_) { /* file URL */ }
    $('#papers').scrollIntoView({behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth'});
    fields.q.focus({preventScroll: true});
  });
  window.addEventListener('popstate', () => { readURL(); render(false, false); });
  document.addEventListener('keydown', event => {
    if (event.key === '/' && !event.ctrlKey && !event.metaKey && !event.altKey && !event.target.closest('input, textarea, select, [contenteditable], dialog[open]')) {
      event.preventDefault(); fields.q.focus();
    }
  });
  const tabs = $$('.taxonomy-tab');
  function selectTab(index, focus = false) {
    tabs.forEach((tab, position) => {
      const active = index === position;
      tab.setAttribute('aria-selected', String(active)); tab.tabIndex = active ? 0 : -1;
      $('#' + tab.getAttribute('aria-controls')).hidden = !active;
    });
    if (focus) tabs[index].focus();
  }
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => selectTab(index));
    tab.addEventListener('keydown', event => {
      let next = index;
      if (['ArrowDown', 'ArrowRight'].includes(event.key)) next = (index + 1) % tabs.length;
      else if (['ArrowUp', 'ArrowLeft'].includes(event.key)) next = (index - 1 + tabs.length) % tabs.length;
      else if (event.key === 'Home') next = 0;
      else if (event.key === 'End') next = tabs.length - 1;
      else return;
      event.preventDefault(); selectTab(next, true);
    });
  });
  selectTab(0);
  const loopCopy = [
    ['Where should the agent look next?', 'Retrieve relevant moments, zoom into a segment, or invoke a perception tool to collect useful observations.', 'Explore acquisition ↗'],
    ['What should the agent remember?', 'Retain observations as text, structured events, compact representations, or an evolving streaming memory.', 'Explore memory ↗'],
    ['Which action should the agent take?', 'Select a tool, decompose a question, or coordinate agents using the evidence already observed.', 'Explore planning ↗'],
    ['Is the evidence sufficient to answer?', 'Compare candidate answers, reflect on reasoning, and reconcile claims with the available evidence. If needed, seek more.', 'Explore verification ↗']
  ];
  $$('.loop-step').forEach(button => button.addEventListener('click', () => {
    const index = Number(button.dataset.loop);
    $$('.loop-step').forEach(step => { const active = step === button; step.classList.toggle('active', active); step.setAttribute('aria-pressed', String(active)); });
    const strong = document.createElement('strong'); strong.textContent = loopCopy[index][0];
    $('#loop-description').replaceChildren(strong, document.createTextNode(' ' + loopCopy[index][1]));
    $('#loop-browse').textContent = loopCopy[index][2]; $('#loop-browse').dataset.filterStage = stageIds[index];
  }));
  $$('[data-close-dialog]').forEach(button => button.addEventListener('click', () => button.closest('dialog').close()));
  $$('dialog').forEach(dialog => dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const box = dialog.getBoundingClientRect();
    if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) dialog.close();
  }));
  $$('[data-figure]').forEach(link => link.addEventListener('click', event => {
    if (event.ctrlKey || event.metaKey || event.shiftKey || !$('#figure-dialog').showModal) return;
    event.preventDefault(); $('#figure-dialog-title').textContent = link.dataset.figure;
    $('#dialog-figure').src = link.href; $('#dialog-figure').alt = link.dataset.figure;
    $('#figure-download').href = link.href; $('#figure-dialog').showModal();
  }));
  $$('[data-cite]').forEach(button => {
    button.hidden = false;
    button.addEventListener('click', () => {
      const paper = byId.get(button.dataset.cite);
      $('#citation-method').textContent = paper.name + ' · ' + paper.year;
      $('#citation-code').textContent = paper.bibtex; $('#copy-status').textContent = '';
      $('#citation-dialog').showModal();
    });
  });
  $('#copy-citation').addEventListener('click', async () => {
    const citation = $('#citation-code').textContent;
    let copied = false;
    try { await navigator.clipboard.writeText(citation); copied = true; } catch (_) {
      const input = document.createElement('textarea'); input.value = citation;
      input.style.cssText = 'position:fixed;opacity:0;top:0;left:0';
      $('#citation-dialog').appendChild(input); input.select();
      try { copied = document.execCommand('copy'); } catch (_) { /* Manual fallback below. */ }
      input.remove(); $('#copy-citation').focus();
    }
    $('#copy-status').textContent = copied ? 'Citation copied.' : 'Select the citation text above and copy it manually.';
  });
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        $$('.desktop-nav a').forEach(link => {
          if (link.hash === '#' + entry.target.id) link.setAttribute('aria-current', 'location');
          else link.removeAttribute('aria-current');
        });
      });
    }, {rootMargin: '-15% 0px -60% 0px'});
    ['overview', 'agent-loop', 'taxonomy', 'papers'].forEach(id => observer.observe($('#' + id)));
  }
  readURL(); render(false, false); $('#explorer-controls').hidden = false;
})();
