/**
 * LearnX — Course Page Utilities
 * Handles mobile sidebar toggling and active section highlighting.
 */
document.addEventListener('DOMContentLoaded', () => {
  const sidebar = document.querySelector('.sidebar');
  if (!sidebar) return;

  // ─── Mobile sidebar toggle ───
  if (!document.querySelector('.mobile-nav-toggle')) {
    const toggleBtn = document.createElement('div');
    toggleBtn.className = 'mobile-nav-toggle';
    toggleBtn.innerHTML = '<i class="fas fa-bars"></i>';
    toggleBtn.setAttribute('aria-label', 'Toggle sidebar navigation');
    document.body.appendChild(toggleBtn);

    const overlay = document.createElement('div');
    overlay.className = 'sidebar-overlay';
    document.body.appendChild(overlay);

    function toggleSidebar() {
      const isOpen = sidebar.classList.toggle('open');
      overlay.classList.toggle('active', isOpen);
      toggleBtn.innerHTML = isOpen
        ? '<i class="fas fa-times"></i>'
        : '<i class="fas fa-bars"></i>';
    }

    toggleBtn.addEventListener('click', toggleSidebar);
    overlay.addEventListener('click', toggleSidebar);

    // Close sidebar when a link is clicked on mobile
    sidebar.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 900 && sidebar.classList.contains('open')) {
          toggleSidebar();
        }
      });
    });
  }

  // ─── Sidebar active state syncing on scroll ───
  const sections = document.querySelectorAll('.topic-section');
  const navLinks = document.querySelectorAll('.sidebar a[href^="#"]');

  if (sections.length > 0 && navLinks.length > 0) {
    window.addEventListener('scroll', () => {
      let currentId = '';
      sections.forEach(section => {
        if (window.pageYOffset >= section.offsetTop - 150) {
          currentId = section.getAttribute('id');
        }
      });

      navLinks.forEach(link => {
        link.classList.remove('active');
        if (currentId && link.getAttribute('href') === '#' + currentId) {
          link.classList.add('active');
        }
      });
    });
  }
});
