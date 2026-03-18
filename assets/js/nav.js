/**
 * LearnX — Global Navigation Controller
 * Handles active state, user status (Firebase), theme toggling, and mobile menu.
 */
import { auth } from './firebase-init.js';
import { onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-auth.js";

document.addEventListener('DOMContentLoaded', () => {
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.top-nav-links a');
  const userDisplay = document.getElementById('user-display');
  const userPill = document.querySelector('.user-pill');
  const authBtns = document.querySelector('.auth-btns');
  const logoutBtn = document.getElementById('logout-btn');
  const hamburger = document.querySelector('.hamburger');
  const topNavLinks = document.querySelector('.top-nav-links');

  // 1. Sync Active State
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href && (currentPath.endsWith(href) || (currentPath === '/' && href === 'index.html'))) {
      link.classList.add('active');
    }
  });

  // 2. Mobile Menu Toggle
  if (hamburger && topNavLinks) {
    hamburger.addEventListener('click', () => {
      topNavLinks.classList.toggle('open');
      hamburger.querySelector('i').className = topNavLinks.classList.contains('open') 
        ? 'fas fa-times' 
        : 'fas fa-bars';
    });
  }

  // 3. Strict Auth Guard - Pre-loading Check
  const isSubdir = currentPath.includes('/courses/');
  const protectedPages = ['index1.html', 'profile.html', 'admin.html', 'feedback.html'];
  const isProtected = protectedPages.some(page => currentPath.endsWith(page)) || isSubdir;
  
  // Hide body immediately if protected so they don't see content before redirect
  if (isProtected) {
    document.body.style.visibility = 'hidden';
  }

  // 4. User Authentication Observer
  onAuthStateChanged(auth, (user) => {
    // Determine the root-relative path for redirects
    const loginPath = isSubdir ? '../auth.html' : 'auth.html';

    if (user) {
      // User is logged in
      const displayName = user.displayName || user.email.split('@')[0];
      if (userDisplay) userDisplay.textContent = displayName;
      
      const dashDisplay = document.getElementById('user-display-name');
      if (dashDisplay) dashDisplay.textContent = displayName;
      
      if (userPill) userPill.style.display = 'flex';
      if (authBtns) authBtns.style.display = 'none';

      // Reveal hidden content if it was a protected page
      if (isProtected) {
        document.body.style.visibility = 'visible';
      }

      // Admin link visibility
      const adminLink = document.getElementById('admin-link');
      if (adminLink) {
        adminLink.style.display = (user.email === "aryankumar735588@gmail.com") ? 'flex' : 'none';
      }

      if (currentPath.endsWith('admin.html') && user.email !== "aryankumar735588@gmail.com") {
        window.location.href = isSubdir ? '../index1.html' : 'index1.html';
      }

    } else {
      // User is logged out
      if (userPill) userPill.style.display = 'none';
      if (authBtns) authBtns.style.display = 'flex';
      
      if (isProtected) {
        console.warn("🔐 Unauthorized access attempt. Redirecting to login...");
        window.location.href = loginPath;
      }
    }
  });

  // 4. Logout Handler
  if (logoutBtn) {
    logoutBtn.addEventListener('click', (e) => {
      e.preventDefault();
      if (confirm("Are you sure you want to logout?")) {
        signOut(auth).then(() => {
          window.location.href = 'auth.html';
        }).catch(err => {
          console.error("Logout error:", err);
        });
      }
    });
  }

  // 5. Search Functionality
  const COURSES = [
    { name: 'HTML', url: 'html.html' },
    { name: 'CSS', url: 'css.html' },
    { name: 'JavaScript', url: 'js.html' },
    { name: 'Python', url: 'python.html' },
    { name: 'SQL', url: 'sql.html' },
    { name: 'Java', url: 'java.html' },
    { name: 'C', url: 'c.html' },
    { name: 'R', url: 'r.html' },
    { name: 'NumPy', url: 'numpy.html' },
    { name: 'Pandas', url: 'pandas.html' },
    { name: 'Matplotlib', url: 'matplotlib.html' },
    { name: 'AI', url: 'ai.html' },
    { name: 'Excel', url: 'excel.html' }
  ];

  function performSearch(query) {
    if (!query) return;
    
    query = query.trim().toLowerCase();
    const result = COURSES.find(c => c.name.toLowerCase() === query || query.includes(c.name.toLowerCase()));
    
    if (result) {
      let finalUrl = result.url;
      // If we are NOT in the courses directory, add the 'courses/' prefix
      if (!window.location.pathname.includes('/courses/')) {
        finalUrl = 'courses/' + finalUrl;
      }
      window.location.href = finalUrl;
    } else {
      alert(`No results found for "${query}". Try searching for HTML, Python, or C.`);
    }
  }

  // Attach to window so HTML onclick can find it
  window.doSearch = () => {
    // Check various common search input IDs
    const searchInputs = [
      document.getElementById('nav-search-input'),
      document.getElementById('hero-search'),
      document.querySelector('.top-nav-search input'),
      document.querySelector('.big-search input')
    ];
    
    for (const input of searchInputs) {
      if (input && input.value) {
        performSearch(input.value);
        return;
      }
    }
  };

  // Add event listeners for Enter key on all search inputs
  document.querySelectorAll('input[placeholder*="Search"]').forEach(input => {
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        performSearch(input.value);
      }
    });

    // Also handle the button next to the input
    const btn = input.nextElementSibling;
    if (btn && (btn.tagName === 'BUTTON' || btn.classList.contains('search-btn'))) {
      btn.addEventListener('click', () => performSearch(input.value));
    }
  });
});

