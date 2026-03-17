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

  // 3. User Authentication Observer
  onAuthStateChanged(auth, (user) => {
    const protectedPages = ['index1.html', 'profile.html', 'admin.html', 'feedback.html'];
    const isProtected = protectedPages.some(page => currentPath.endsWith(page)) || currentPath.includes('/courses/');

    if (user) {
      // User is logged in
      const displayName = user.displayName || user.email.split('@')[0];
      if (userDisplay) userDisplay.textContent = displayName;
      
      // Also update dashboard-specific display if it exists
      const dashDisplay = document.getElementById('user-display-name');
      if (dashDisplay) dashDisplay.textContent = displayName;
      if (userPill) userPill.style.display = 'flex';
      if (authBtns) authBtns.style.display = 'none';

      
      // Admin link visibility
      const adminLink = document.getElementById('admin-link');
      if (adminLink) {
        if (user.email === "aryankumar735588@gmail.com") {
          adminLink.style.display = 'flex';
        } else {
          adminLink.style.display = 'none';
        }
      }
    } else {
      // User is logged out
      if (userPill) userPill.style.display = 'none';
      if (authBtns) authBtns.style.display = 'flex';
      
      // Strict access control: redirect to login if on protected page
      if (isProtected) {
        console.warn("Unauthorized access attempt. Redirecting to login...");
        window.location.href = 'index.html';
      }
    }
  });

  // 4. Logout Handler
  if (logoutBtn) {
    logoutBtn.addEventListener('click', (e) => {
      e.preventDefault();
      if (confirm("Are you sure you want to logout?")) {
        signOut(auth).then(() => {
          window.location.href = 'index.html';
        }).catch(err => {
          console.error("Logout error:", err);
        });
      }
    });
  }
});

