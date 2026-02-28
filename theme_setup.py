import os

THEME_JS = """
  <script>
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
  </script>
</body>
"""

# Modify home.html
with open('home.html', 'r', encoding='utf-8') as f:
    home_html = f.read()
if 'id="theme-toggle"' not in home_html:
    home_html = home_html.replace('<a href="index.html" class="btn-outline">Log In</a>', 
                                  '<button id="theme-toggle" class="btn-outline" style="border:none; cursor:pointer;"><i class="fas fa-moon"></i></button>\n            <a href="index.html" class="btn-outline">Log In</a>')
    if '// Theme logic' not in home_html:
        home_html = home_html.replace('</body>', THEME_JS)
    with open('home.html', 'w', encoding='utf-8') as f:
        f.write(home_html)

# Modify index1.html
with open('index1.html', 'r', encoding='utf-8') as f:
    dash_html = f.read()
if 'id="theme-toggle"' not in dash_html:
    dash_html = dash_html.replace('<button class="hamburger"', 
                                  '<button id="theme-toggle" class="nav-btn" style="background:transparent; border:1px solid #aaa; color:#ccc; margin-right:10px;"><i class="fas fa-sun"></i> Toggle</button>\n    <button class="hamburger"')
    if '// Theme logic' not in dash_html:
        dash_html = dash_html.replace('</body>', THEME_JS)
    with open('index1.html', 'w', encoding='utf-8') as f:
        f.write(dash_html)

# Inject into original login page too
with open('index.html', 'r', encoding='utf-8') as f:
    login_html = f.read()
if 'id="theme-toggle"' not in login_html:
    # Just setting the global theme logic for consistency on load
    if '// Theme logic' not in login_html:
        login_html = login_html.replace('</body>', THEME_JS)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(login_html)

print("Theme integration complete.")
