import os
import re

THEME_JS = """
  <script>
    // Theme logic
    const toggleBtn = document.getElementById('theme-toggle');
    const updateThemeIcon = (isDark) => {
      if(toggleBtn) toggleBtn.innerHTML = isDark ? '<i class="fas fa-sun" style="font-size:16px;"></i><span class="theme-text" style="margin-left:5px;">Light</span>' : '<i class="fas fa-moon" style="font-size:16px;"></i><span class="theme-text" style="margin-left:5px;">Dark</span>';
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
  </script>
</body>"""

def add_theme_to_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has theme-toggle
    if 'id="theme-toggle"' in content:
        return

    # Add button to top-nav right before the auth/search area or inside it
    if 'home.html' in filepath:
        # Home page puts it before Log In button
        btn_html = ' <button id="theme-toggle" class="nav-btn" style="background:#282A35; color:#fff; border:1px solid rgba(255,255,255,0.2); margin-right:15px; display:inline-flex; align-items:center; cursor:pointer;" title="Change Theme"><i class="fas fa-sun"></i></button>\n            <a href="index.html" class="btn-outline">Log In</a>'
        content = content.replace('<a href="index.html" class="btn-outline">Log In</a>', btn_html)
    elif 'index1.html' in filepath or 'about.html' in filepath or 'Contact.html' in filepath or 'feedback.html' in filepath:
        # Dashboard/Pages put it right before the search bar or inside top-nav-links
        # Right after the dashboard loops, find search or hamburger
        btn_html = ' <button id="theme-toggle" class="nav-btn" style="background:transparent; color:var(--text); border:1px solid var(--border); margin-right:15px; display:inline-flex; align-items:center; justify-content:center; cursor:pointer;"><i class="fas fa-sun"></i></button>\n    <button class="hamburger"'
        # Replace the hamburger logic
        content = content.replace('<button class="hamburger"', btn_html)
        
        # If no hamburger (about, contact, feedback)
        if '<button class="hamburger"' not in content:
            # Inject at the end of top-nav-links
            btn2_html = '\n      <button id="theme-toggle" class="nav-btn" style="background:transparent; color:var(--text); border:1px solid var(--border); margin-left:auto; display:inline-flex; align-items:center; justify-content:center; cursor:pointer; padding: 6px 12px;"><i class="fas fa-sun"></i></button>\n    </div>'
            content = content.replace('</div>\n  </nav>', btn2_html + '\n  </nav>')
            
    elif 'index.html' in filepath:
        pass # Optional to add to login screen itself visually, but we will add logic.
        
    else:
        # Courses pages
        # Find logout-btn wrapper and prepend it
        btn_html = ' <button id="theme-toggle" class="nav-btn" style="background:transparent; border:1px solid #aaa; color:#ccc; margin-right:10px; display:inline-flex; align-items:center; cursor:pointer;"><i class="fas fa-sun"></i></button>\n      <button id="logout-btn"'
        content = content.replace('<button id="logout-btn"', btn_html)

    # Add Logic
    if '// Theme logic' not in content:
        content = content.replace('</body>', THEME_JS)

    # Fix Index1.html card colors to be brighter for dark mode
    if 'index1.html' in filepath:
        color_fixes = {
            '#013243': '#00a8cc', # NumPy
            '#150458': '#7e57c2', # Pandas
            '#11557c': '#29b6f6', # Matplotlib
            '#1572b6': '#2196f3', # CSS
        }
        for old_c, new_c in color_fixes.items():
            content = content.replace(f'--card-accent:{old_c}', f'--card-accent:{new_c}')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


# Process specific files in root
for p in ['home.html', 'index1.html', 'about.html', 'Contact.html', 'feedback.html', 'index.html']:
    if os.path.exists(p):
        add_theme_to_file(p)

# Process courses
if os.path.isdir('courses'):
    for filename in os.listdir('courses'):
        if filename.endswith(".html"):
            add_theme_to_file(os.path.join('courses', filename))

print("Theme toggle and visibility fixes applied!")
