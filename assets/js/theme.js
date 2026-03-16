/**
 * LearnX — Global Theme Toggle
 * Manages dark/light mode with localStorage persistence.
 * Include this script on every page that has a #theme-toggle button.
 */
(function initTheme() {
  const savedTheme = localStorage.getItem('theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);

  function updateIcon(isDark) {
    const btn = document.getElementById('theme-toggle');
    if (!btn) return;
    btn.innerHTML = isDark
      ? '<i class="fas fa-sun" style="font-size:16px;"></i><span class="theme-text" style="margin-left:5px;">Light</span>'
      : '<i class="fas fa-moon" style="font-size:16px;"></i><span class="theme-text" style="margin-left:5px;">Dark</span>';
  }

  document.addEventListener('DOMContentLoaded', () => {
    updateIcon(savedTheme === 'dark');

    const btn = document.getElementById('theme-toggle');
    if (btn) {
      btn.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('theme', next);
        updateIcon(next === 'dark');
      });
    }
  });
})();
