import os
import re

COURSE_DIR = 'courses'

# Theme toggle JS
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

    // Try It Editor functions (applied globally to all courses)
    window.openTryIt = function(btn) {
      const panel = btn.nextElementSibling;
      panel.classList.add('open');
      btn.style.display = 'none';
      runTryIt(panel.querySelector('.tryit-run'));
    };
    window.closeTryIt = function(btn) {
      const panel = btn.closest('.tryit-panel');
      panel.classList.remove('open');
      panel.previousElementSibling.style.display = 'inline-flex';
    };
    window.runTryIt = function(btn) {
      const panel = btn.closest('.tryit-panel');
      const code = panel.querySelector('.tryit-editor').value;
      const iframe = panel.querySelector('iframe');
      // basic wrapping for output display
      iframe.srcdoc = `
        <style>body{font-family:sans-serif; color:#333; background:#fff;}</style>
        ${code}
      `;
    };
  </script>
</body>
"""

# Common HTML replacements
def process_course_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix stray closing divs inside sections
    content = re.sub(r'</div>\s*</section>', '</section>', content)

    # 2. Add Theme Toggle Button to Top Nav
    if 'id="theme-toggle"' not in content:
        theme_btn = '<button id="theme-toggle" class="nav-btn" style="background:#3d3f4e; color:#fff; border:none; margin-right:10px;"><i class="fas fa-sun"></i> Toggle</button>'
        content = content.replace('<button id="logout-btn"', theme_btn + '\n      <button id="logout-btn"')

    # 3. Inject Try It Panels into EVERY example box
    # We find: <div class="example-box">...<code ...>(.*?)</code>...</pre></div>
    # And we append the Try It panel to it if it doesn't already have one.
    
    # Split by example boxes to process them
    parts = content.split('<div class="example-box">')
    new_content = parts[0]
    
    for part in parts[1:]:
        if 'class="try-btn"' in part:
            # Already has it
            new_content += '<div class="example-box">' + part
            continue
            
        # Extract code to put in textarea
        code_match = re.search(r'<code[^>]*>(.*?)</code>', part, re.DOTALL)
        if code_match:
            code_text = code_match.group(1).replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
            
            # Simple escape for textarea
            textarea_code = code_text.replace('<', '&lt;').replace('>', '&gt;')
            
            panel = f'''
            <button class="try-btn" onclick="openTryIt(this)">Try it Yourself <i class="fas fa-play"></i></button>
            <div class="tryit-panel">
              <div class="tryit-toolbar">
                <span>Live Editor</span>
                <button class="tryit-run" onclick="runTryIt(this)"><i class="fas fa-play"></i> Run Code</button>
                <button class="tryit-close" onclick="closeTryIt(this)"><i class="fas fa-times"></i> Close</button>
              </div>
              <textarea class="tryit-editor" spellcheck="false">{textarea_code}</textarea>
              <div class="tryit-output"><iframe srcdoc=""></iframe></div>
            </div>
            '''
            # insert panel before the closing div of the example-box
            # The part usually ends with </div> somewhere before the next </section> or it's wrapped cleanly.
            # Assuming part contains `</pre></div>`
            part = part.replace('</pre></div>', f'</pre>{panel}</div>', 1)
            
        new_content += '<div class="example-box">' + part

    content = new_content

    # 4. Inject script logic at the bottom
    if '// Theme logic' not in content:
        content = content.replace('</body>', THEME_JS)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    return True


if __name__ == "__main__":
    count = 0
    for filename in os.listdir(COURSE_DIR):
        if filename.endswith('.html'):
            filepath = os.path.join(COURSE_DIR, filename)
            process_course_html(filepath)
            count += 1
    
    print(f"Fixed {count} course files.")
