/* Native anchor navigation works even with JavaScript disabled. */
(() => {
  const navLinks = [...document.querySelectorAll('#paper-nav a')];
  const sections = navLinks.map(link => document.getElementById(link.hash.slice(1))).filter(Boolean);
  const select = document.getElementById('chapter-select');
  const progress = document.getElementById('paper-progress');
  const printButton = document.getElementById('print-button');
  const top = document.querySelector('.top');
  const mobileNav = document.querySelector('.mobile-nav');
  let scheduled = false;

  function update() {
    scheduled = false;
    const offset = top.offsetHeight + (mobileNav.offsetHeight || 0) + 36;
    let current = sections[0];
    for (const section of sections) {
      if (section.getBoundingClientRect().top <= offset) current = section;
    }
    const max = document.documentElement.scrollHeight - window.innerHeight;
    if (max > 0 && max - window.scrollY < 4) current = sections.at(-1);
    navLinks.forEach(link => {
      const active = link.hash === `#${current.id}`;
      link.classList.toggle('active', active);
      if (active) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
    select.value = current.id;
    progress.style.width = `${Math.min(100, Math.max(0, 100 * window.scrollY / Math.max(1, max)))}%`;
  }

  function scheduleUpdate() {
    if (!scheduled) {
      scheduled = true;
      requestAnimationFrame(update);
    }
  }

  select.addEventListener('change', () => { window.location.hash = select.value; });
  window.addEventListener('scroll', scheduleUpdate, { passive: true });
  window.addEventListener('resize', scheduleUpdate, { passive: true });
  window.addEventListener('hashchange', scheduleUpdate);
  document.querySelectorAll('details').forEach(item => item.addEventListener('toggle', scheduleUpdate));
  update();

  // Make the full backlog available to the browser's print / Save as PDF dialog.
  let previousDetails = null;
  window.addEventListener('beforeprint', () => {
    if (previousDetails !== null) return;
    previousDetails = [...document.querySelectorAll('details')].map(item => [item, item.open]);
    previousDetails.forEach(([item]) => { item.open = true; });
  });
  window.addEventListener('afterprint', () => {
    if (previousDetails === null) return;
    previousDetails.forEach(([item, wasOpen]) => { item.open = wasOpen; });
    previousDetails = null;
    scheduleUpdate();
  });
  printButton.addEventListener('click', () => window.print());
})();
