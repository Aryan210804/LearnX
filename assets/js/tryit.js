/**
 * LearnX — Try It Yourself Editor
 * Provides open/close/run functionality for inline code editors.
 * Include this script on any course page with .try-btn elements.
 */
window.openTryIt = function (btn) {
  const panel = btn.nextElementSibling;
  if (!panel) return;
  panel.classList.add('open');
  btn.style.display = 'none';
  const runBtn = panel.querySelector('.tryit-run');
  if (runBtn) window.runTryIt(runBtn);
};

window.closeTryIt = function (btn) {
  const panel = btn.closest('.tryit-panel');
  if (!panel) return;
  panel.classList.remove('open');
  const tryBtn = panel.previousElementSibling;
  if (tryBtn) tryBtn.style.display = 'inline-flex';
};

window.runTryIt = function (btn) {
  const panel = btn.closest('.tryit-panel');
  if (!panel) return;
  const code = panel.querySelector('.tryit-editor').value;
  const iframe = panel.querySelector('iframe');
  if (!iframe) return;
  iframe.srcdoc = `
    <style>body{font-family:'Inter',sans-serif;color:#333;background:#fff;padding:12px;}</style>
    ${code}
  `;
};
