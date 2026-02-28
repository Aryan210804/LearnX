import os
import re

nav_links_html = """    <div class="top-nav-links">
      <a href="../index1.html"><i class="fas fa-home" style="margin-right:5px"></i> Dashboard</a>
      <a href="html.html">HTML</a>
      <a href="css.html">CSS</a>
      <a href="js.html">JavaScript</a>
      <a href="python.html">Python</a>
      <a href="sql.html">SQL</a>
      <a href="java.html">Java</a>
      <a href="c.html">C</a>
      <a href="excel.html">Excel</a>
      <a href="numpy.html">NumPy</a>
      <a href="pandas.html">Pandas</a>
      <a href="matplotlib.html">Matplotlib</a>
      <a href="ml.html">ML</a>
      <a href="ai.html">AI</a>
      <a href="r.html">R</a>
    </div>"""

# Ensure that the correct active class is set for each page!
def update_nav(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the top nav
    # Find <div class="top-nav-links"> ... </div> right before <div class="top-nav-search">
    pattern = r'<div class="top-nav-links">.*?</div>\s*<div class="top-nav-search">'
    
    basename = os.path.basename(filepath)
    
    # We will inject the active class
    file_specific_nav = nav_links_html.replace(f'href="{basename}"', f'href="{basename}" class="active"')
    
    replacement = file_specific_nav + '\n\n    <div class="top-nav-search">'
    
    # Try replacing
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {basename}")
    else:
        print(f"Failed to find match in {basename}")

if os.path.exists('courses'):
    for filename in os.listdir('courses'):
        if filename.endswith(".html"):
            update_nav(os.path.join('courses', filename))
