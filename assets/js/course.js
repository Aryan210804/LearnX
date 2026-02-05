document.addEventListener('DOMContentLoaded', () => {
    // Inject Mobile Nav Elements
    if (!document.querySelector('.mobile-nav-toggle')) {
        const toggleBtn = document.createElement('div');
        toggleBtn.className = 'mobile-nav-toggle';
        toggleBtn.innerHTML = '<i class="fas fa-bars"></i>';
        document.body.appendChild(toggleBtn);

        const overlay = document.createElement('div');
        overlay.className = 'sidebar-overlay';
        document.body.appendChild(overlay);

        // Event Listeners
        const sidebar = document.querySelector('.sidebar');

        function toggleSidebar() {
            sidebar.classList.toggle('active');
            overlay.classList.toggle('active');
            toggleBtn.innerHTML = sidebar.classList.contains('active') ?
                '<i class="fas fa-times"></i>' : '<i class="fas fa-bars"></i>';
        }

        toggleBtn.addEventListener('click', toggleSidebar);
        overlay.addEventListener('click', toggleSidebar);

        // Close sidebar when link is clicked
        sidebar.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 900) {
                    toggleSidebar();
                }
            });
        });
    }

    // Initial check for hash to open valid section
    if (window.location.hash) {
        const targetId = window.location.hash.substring(1);
        const targetSection = document.getElementById(targetId);
        if (targetSection && targetSection.classList.contains('section')) {
            targetSection.classList.add('expanded');
        }
    }

    // Add click listeners to all section headers
    document.querySelectorAll('.section-header').forEach(header => {
        header.addEventListener('click', () => {
            const section = header.parentElement;
            section.classList.toggle('expanded');
        });
    });
});

function expandAll() {
    document.querySelectorAll('.section').forEach(section => {
        section.classList.add('expanded');
    });
}

function collapseAll() {
    document.querySelectorAll('.section').forEach(section => {
        section.classList.remove('expanded');
    });
}
