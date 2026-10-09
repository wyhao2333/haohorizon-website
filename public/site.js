'use strict';
document.documentElement.classList.add('js');
const toggle = document.querySelector('.menu-toggle');
const navigation = document.getElementById('primary-nav');
const setMenu = (open) => {
  if (!toggle || !navigation) return;
  toggle.setAttribute('aria-expanded', String(open));
  navigation.classList.toggle('is-open', open);
};
toggle?.addEventListener('click', () => setMenu(toggle.getAttribute('aria-expanded') !== 'true'));
navigation?.addEventListener('click', (event) => {
  if (event.target.closest('a')) setMenu(false);
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && toggle?.getAttribute('aria-expanded') === 'true') {
    setMenu(false);
    toggle.focus();
  }
});
const mobile = window.matchMedia('(max-width: 650px)');
mobile.addEventListener('change', () => setMenu(false));
document.querySelectorAll('[data-copy]').forEach((button) => {
  button.addEventListener('click', async () => {
    const status = document.querySelector('.copy-status');
    try {
      await navigator.clipboard.writeText(button.dataset.copy);
      if (status) status.textContent = 'Email copied.';
    } catch {
      if (status) status.textContent = 'Select and copy the email address above.';
    }
  });
});
