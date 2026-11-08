(function () {
  const key = 'portfolio-theme';
  const root = document.documentElement;
  const button = document.getElementById('theme-toggle');
  if (!button) return;

  function syncButton() {
    const dark = root.getAttribute('data-theme') === 'dark';
    button.setAttribute('aria-label', dark ? 'Aktifkan light mode' : 'Aktifkan dark mode');
    button.setAttribute('title', dark ? 'Light mode' : 'Dark mode');
    button.setAttribute('aria-pressed', String(dark));
    const icon = button.querySelector('i');
    if (icon) icon.className = dark ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
  }

  button.addEventListener('click', function () {
    const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem(key, next); } catch (_) { /* storage unavailable */ }
    syncButton();
  });

  syncButton();
}());
