import os
import re

def title_case(s):
    # Just capitalize first letter of each word
    return ' '.join(word.capitalize() for word in s.split())

def rebuild_course(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all sections and their main <h1> titles
    sections = re.findall(r'<section[^>]*id="([^"]+)"[^>]*>\s*<h1>(.*?)</h1>', content)
    
    if not sections:
        print(f"No sections found in {filepath}")
        return

    basename = os.path.basename(filepath).replace('.html', '')
    
    # Map raw basename to display names
    display_names = {
        'css': 'CSS', 'js': 'JavaScript', 'python': 'Python', 'sql': 'SQL',
        'c': 'C Programming', 'java': 'Java', 'excel': 'Excel',
        'matplotlib': 'Matplotlib', 'numpy': 'NumPy', 'pandas': 'Pandas',
        'ml': 'Machine Learning', 'ai': 'Artificial Intelligence',
        'r': 'R Programming'
    }
    
    course_name = display_names.get(basename, basename.title())
    
    if course_name == 'HTML':
        return # Skip html.html as it's our template
        
    # Get icon
    icons = {
        'CSS': 'fab fa-css3-alt" style="color:#1572b6',
        'JavaScript': 'fab fa-js" style="color:#f7df1e',
        'Python': 'fab fa-python" style="color:#306998',
        'C Programming': 'fas fa-c" style="color:#00599C',
        'Java': 'fab fa-java" style="color:#f89820',
        'Machine Learning': 'fas fa-brain" style="color:#ff9900',
        'Artificial Intelligence': 'fas fa-robot" style="color:#00d2ff',
        'SQL': 'fas fa-database" style="color:#f29111',
        'Excel': 'fas fa-file-excel" style="color:#217346',
        'NumPy': 'fas fa-cubes" style="color:#013243',
        'Pandas': 'fas fa-table" style="color:#150458',
        'Matplotlib': 'fas fa-chart-bar" style="color:#11557c',
        'R Programming': 'fas fa-registered" style="color:#276cb8'
    }
    icon = icons.get(course_name, 'fas fa-book" style="color:var(--primary)')

    # 1. Build the new sidebar
    sidebar_html = f'''<aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <i class="{icon}"></i> {course_name} Tutorial
      </div>

      <div class="sidebar-section-label">{course_name} Basic</div>\n'''
      
    for i, (sec_id, title) in enumerate(sections):
        active_class = ' class="active"' if i == 0 else ''
        sidebar_html += f'      <a href="#{sec_id}"{active_class}>{title}</a>\n'

    sidebar_html += f'''
      <div class="sidebar-footer">
        <a href="../index1.html"><i class="fas fa-arrow-left"></i> Back to Dashboard</a>
      </div>
    </aside>'''

    # Replace the old sidebar
    content = re.sub(r'<aside class="sidebar" id="sidebar">.*?</aside>', sidebar_html, content, flags=re.DOTALL)
    
    # 2. Update the Breadcrumb and Masterclass h1 title to have the text color class
    # Replace `<h1 style="font-size:38px; margin-bottom: 40px; color:var(--secondary);">CSS Masterclass</h1>`
    # Replace `<h1 style="font-size:38px; margin-bottom: 40px; color:var(--text);">CSS Masterclass</h1>`
    # We will just globally replace `color:var(--secondary);` to `color:var(--text);` inside style attributes for h1
    content = content.replace('color:var(--secondary);', 'color:var(--text);')

    # 3. Add Chapter Badge and Prev/Next to EVERY section
    for i, (sec_id, title) in enumerate(sections):
        # We need to find the <section> block up to the next </section> or EOF
        # So we just match <h1>title</h1> inside that section
        
        # Calculate Next and Prev ids
        prev_link = f'#{sections[i-1][0]}' if i > 0 else '#'
        prev_vis = '' if i > 0 else 'visibility:hidden;'
        
        next_link = f'#{sections[i+1][0]}' if i < len(sections)-1 else '#'
        next_vis = '' if i < len(sections)-1 else 'visibility:hidden;'
        
        badge_html = f'''<h1>{title}</h1>
          <div class="chapter-badge">Chapter {i+1}</div>

          <div class="topic-nav" style="margin-top:10px; margin-bottom:30px;">
            <a href="{prev_link}" class="nav-prev" style="{prev_vis}"><i class="fas fa-chevron-left"></i> Previous</a>
            <a href="{next_link}" class="nav-next" style="{next_vis}">Next <i class="fas fa-chevron-right"></i></a>
          </div>'''
          
        # Only replace the FIRST occurrence in case titles duplicate, but realistically we replace specifically inside the section
        # More safely, we find `<section[^>]*id="sec_id"[^>]*>\s*<h1>title</h1>`
        
        pattern = rf'(<section[^>]*id="{sec_id}"[^>]*>\s*)<h1>{re.escape(title)}</h1>(.*?(?:<div class="chapter-badge">)?)'
        
        def replacer(match):
            prefix = match.group(1)
            rest = match.group(2)
            if 'class="chapter-badge"' in rest:
                return match.group(0) # Already has badge
            return prefix + badge_html
            
        content = re.sub(pattern, replacer, content, count=1, flags=re.DOTALL)

    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filename in os.listdir('courses'):
    if filename.endswith('.html') and filename != 'html.html':
        rebuild_course(os.path.join('courses', filename))

print("Sidebars, chapter badges, and prev/next navigation updated!")
