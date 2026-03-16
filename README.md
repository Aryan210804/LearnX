# LearnX 🚀

<div align="center">
  <img src="assets/img/LOGO.jpeg" alt="LearnX Logo" width="120" />
</div>

<p align="center">
  <strong>The World's Largest Open-Source Learning Platform for Developers</strong><br>
  <em>Clean, minimal, and premium educational interface inspired by W3Schools.</em>
</p>

---

## 🌟 Overview

**LearnX** is a modern, premium educational platform designed to make learning programming simple, accessible, and highly structured. We mimic the straightforward methodology of top-tier coding bootcamps, removing the noise and presenting pure, practical, and text-based knowledge with an intuitive interface.

### 🔥 Key Features

- **🛡️ Secure Access:** Full integration with **Firebase Authentication**. Users must sign up and log in to access the premium course content.
- **💻 "Try it Yourself" Live Editor:** Every course features dynamic, inline code editors allowing students to execute and experiment with HTML/CSS/JS code directly inside the browser.
- **🌗 Dual-Theme Engine:** A flawless, high-contrast **Light & Dark Mode** toggle available globally on every page. Powered by a shared `theme.js` module.
- **📚 14 Comprehensive Masterclasses:** Navigate seamlessly between high-quality tutorials via our horizontally scrolling premium Navigation Bar.
- **📊 Interactive Dashboard:** A personalized hub displaying live statistics, available courses, and web development fundamentals.
- **💬 Real-Time Feedback:** Direct integration with **Firebase Firestore** allows users to submit real-time feedback forms straight to the admin dashboard.
- **👤 User Profiles:** Manage display name, bio, age, and location via the profile page.
- **🔐 Admin Panel:** Protected admin command center to view all feedbacks and manage user accounts.

---

## 🎒 Available Courses

LearnX currently offers fully interactive, multi-chapter curriculums for the following technologies:

| Web Development | Backend & Systems | Data Science & AI |
| :---: | :---: | :---: |
| HTML | Python | NumPy |
| CSS | Java | Pandas |
| JavaScript | C | Matplotlib |
| Excel | SQL | Machine Learning & AI |
| — | R | — |

Each course includes:
- Chapter-based navigation with a sidebar
- Code examples with syntax highlighting
- "Try it Yourself" interactive code editors
- Chapter badges & prev/next pagination
- Real-world projects and mini tasks

---

## 🏗️ Project Architecture

```
LearnX/
├── index.html          ← Login / Registration page (Firebase Auth)
├── index1.html         ← Authenticated Dashboard (course listing)
├── home.html           ← Public landing page (marketing)
├── about.html          ← About the platform
├── Contact.html        ← Developer contact information
├── feedback.html       ← Feedback form (saves to Firestore)
├── admin.html          ← Admin panel (Firestore: view feedback, manage users)
├── profile.html        ← User profile editor (name, bio, location)
│
├── assets/
│   ├── css/
│   │   └── style.css           ← Global design system (themes, layout, components)
│   ├── js/
│   │   ├── theme.js            ← Shared dark/light mode toggle
│   │   ├── firebase-init.js    ← Shared Firebase initialization (ES Module)
│   │   ├── course.js           ← Mobile sidebar toggle + scroll-sync
│   │   └── tryit.js            ← "Try it Yourself" editor functionality
│   └── img/                    ← Logos and course images
│
├── courses/
│   ├── html.html       ← 14 course pages, each with sidebar + chapters
│   ├── css.html
│   ├── js.html
│   ├── python.html
│   ├── sql.html
│   ├── java.html
│   ├── c.html
│   ├── excel.html
│   ├── numpy.html
│   ├── pandas.html
│   ├── matplotlib.html
│   ├── ai.html
│   └── r.html
│
├── README.md
└── LICENSE
```

### Design System (`style.css`)

The CSS design system provides:
- **CSS Custom Properties** for all colors, spacing, and typography
- **Dark & Light theme** via `[data-theme]` attribute
- **Course page layout**: Fixed top-nav, fixed sidebar, scrollable content area
- **Reusable components**: `.topic-section`, `.example-box`, `.try-btn`, `.tryit-panel`, `.note-box`, `.tip-box`, `.warning-box`
- **Dashboard components**: `.course-grid`, `.course-card`, `.dash-stats`, `.modal-overlay`
- **Utility classes**: `.text-center`, `.text-muted`, `.mt-1` through `.mt-4`, `.mb-1` through `.mb-4`

### Shared JavaScript Modules

| Module | Purpose |
|--------|---------|
| `theme.js` | Manages dark/light mode with `localStorage` persistence. Auto-initializing IIFE. |
| `firebase-init.js` | Exports `auth` and `db` for Firebase Auth + Firestore. ES Module. |
| `course.js` | Handles mobile sidebar toggle and scroll-based active section highlighting. |
| `tryit.js` | Provides `openTryIt()`, `closeTryIt()`, `runTryIt()` for inline code editors. |

---

## 🛠️ Technology Stack

- **Frontend:** HTML5, Vanilla JavaScript (ES6+ Modules), Modern CSS3 (Custom Properties, Grid, Flexbox).
- **Backend/BaaS:** Google Firebase (Authentication, Firestore Database).
- **Icons & Typography:** Font Awesome 6.4, Google Fonts (`Inter`, `Fira Code`).
- **No Build Step Required:** Pure static files — serve with any HTTP server.

---

## 🚀 Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Edge, Safari)
- [Node.js](https://nodejs.org/) (only for the local dev server)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Aryan210804/LearnX.git
   cd LearnX
   ```

2. **Start the local server**
   ```bash
   npx serve . --listen 3000
   ```

3. **Open the platform**
   Navigate to `http://localhost:3000` in your web browser. You will be greeted by the `index.html` login screen. Create an account to access the dashboard!

### Quick Start (No Server)

You can also open `home.html` directly in your browser. However, ES Module imports (`firebase-init.js`) require a server to work correctly due to CORS restrictions.

---

## 🎨 Design Philosophy

LearnX was rigorously refactored to prioritize *visual excellence* and *educational clarity*:

- **No Distractions:** Information is organized into clean card layouts and grid systems.
- **Consistent Hierarchy:** A standardized 8px spacing scale, carefully selected border radiuses, and dynamic hover states create micro-interactions across the board.
- **W3Schools Style Navigation:** Sidebar navigation allows users to effortlessly jump between chapters (e.g., *Intro, Variables, Syntax, Loops*), combined perfectly with Chapter Badges and Next/Prev Pagination.
- **Dual Theme:** Every component and page supports both light and dark modes via CSS custom properties.

---

## 📬 Contact & Support

Developed and maintained by **Aryan Kumar Ojha**.
Feel free to open an issue, submit a pull request, or connect with me:

- **Email:** [aryankumar735588@gmail.com](mailto:aryankumar735588@gmail.com)
- **LinkedIn:** [Aryan Kumar](https://www.linkedin.com/in/aryan-kumar-487953297)
- **GitHub:** [Aryan210804](https://github.com/Aryan210804)
- **Instagram:** [@ak__ojha](https://www.instagram.com/ak__ojha/)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <i>Built with ❤️ by <strong>Aryan Kumar Ojha</strong>.</i><br>
  <small>&copy; 2024–2026 Aryan Kumar Ojha. All rights reserved.</small>
</p>
