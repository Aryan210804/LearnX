import os
import re

# Remove toggle button and THEME_JS from all files

THEME_JS = """  <script>
    // Theme logic
    const toggleBtn = document.getElementById('theme-toggle');
    const updateThemeIcon = (isDark) => {
      if(toggleBtn) toggleBtn.innerHTML = isDark ? '<i class="fas fa-sun"></i> Light Mode' : '<i class="fas fa-moon"></i> Dark Mode';
    };
    
    // Check saved theme
    let currentTheme = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', currentTheme);
    window.addEventListener('DOMContentLoaded', () => updateThemeIcon(currentTheme === 'dark'));

    if(toggleBtn) {
      toggleBtn.addEventListener('click', () => {
        let theme = document.documentElement.getAttribute('data-theme');
        let newTheme = theme === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeIcon(newTheme === 'dark');
      });
    }
  </script>"""

THEME_JS_COURSES = """    // Theme logic
    const toggleBtn = document.getElementById('theme-toggle');
    const updateThemeIcon = (isDark) => {
      if(toggleBtn) toggleBtn.innerHTML = isDark ? '<i class="fas fa-sun"></i> Light Mode' : '<i class="fas fa-moon"></i> Dark Mode';
    };
    
    // Check saved theme
    let currentTheme = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', currentTheme);
    window.addEventListener('DOMContentLoaded', () => updateThemeIcon(currentTheme === 'dark'));

    if(toggleBtn) {
      toggleBtn.addEventListener('click', () => {
        let theme = document.documentElement.getAttribute('data-theme');
        let newTheme = theme === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeIcon(newTheme === 'dark');
      });
    }"""


def process_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove theme-toggle button variants:
    # <button id="theme-toggle"...>...</button>
    content = re.sub(r'<button id="theme-toggle"[^>]*>.*?</button>\s*', '', content)
    
    # Remove THEME_JS
    content = content.replace(THEME_JS, '')
    content = content.replace(THEME_JS_COURSES, '')

    # Additional cleanup regarding certificates that grep found
    if 'certificate' in content.lower():
        # Home page certificate feature replacement
        content = re.sub(r'<div class="feature-icon">\s*<i class="fas fa-certificate"></i>\s*</div>\s*<div class="feature-text">\s*<h4>Earn Certificates</h4>\s*<p>Complete courses and earn certificates to showcase your skills.</p>\s*</div>',
                         '<div class="feature-icon"><i class="fas fa-laptop-code"></i></div><div class="feature-text"><h4>Real-world Projects</h4><p>Build real-world projects to showcase your skills to employers.</p></div>', content, flags=re.IGNORECASE)

        # Index1 page stats replacement
        content = re.sub(r'<div class="dash-stat">\s*<div class="dash-stat-icon" style="background:rgba\(229,57,53,0\.1\);color:#e53935">\s*<i class="fas fa-certificate"></i>\s*</div>\s*<div>\s*<div class="dash-stat-num">.*</div>\s*<div class="dash-stat-label">Certificates</div>\s*</div>\s*</div>',
                         '<div class="dash-stat"><div class="dash-stat-icon" style="background:rgba(229,57,53,0.1);color:#e53935"><i class="fas fa-tasks"></i></div><div><div class="dash-stat-num">150+</div><div class="dash-stat-label">Exercises</div></div></div>', content, flags=re.IGNORECASE)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Process base files
process_html_file('home.html')
process_html_file('index1.html')
process_html_file('index.html')

# Process /courses/ files
for filename in os.listdir('courses'):
    if filename.endswith(".html"):
        filepath = os.path.join('courses', filename)
        process_html_file(filepath)

print("Cleanup complete!")
