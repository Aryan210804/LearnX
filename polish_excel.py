import re

filepath = r'c:\Users\DELL\Desktop\LearnX\courses\excel.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Top Nav to match html.html style
top_nav_pattern = r'<nav class="top-nav">.*?</nav>'
new_top_nav = """  <!-- TOP NAV -->
  <nav class="top-nav">
    <button class="hamburger" id="mobile-toggle"><i class="fas fa-bars"></i></button>
    <a href="../index1.html" class="brand">LearnX</a>

    <div class="top-nav-search">
      <input type="text" placeholder="Search course content..." />
      <button><i class="fas fa-search"></i></button>
    </div>

    <div class="nav-profile-links">
      <span id="user-display"></span>
      <button id="theme-toggle" title="Toggle Theme"><i class="fas fa-sun"></i></button>
      <button id="logout-btn" class="nav-btn">Logout</button>
    </div>
  </nav>"""
content = re.sub(top_nav_pattern, new_top_nav, content, flags=re.DOTALL)

# 2. Fix Sub Nav to match html.html style
sub_nav_pattern = r'<nav class="sub-nav">.*?</nav>'
new_sub_nav = """  <!-- SUB NAV (Course Links) -->
  <nav class="sub-nav">
    <a href="../index1.html"><i class="fas fa-th-large"></i> DASHBOARD</a>
    <a href="html.html">HTML</a>
    <a href="css.html">CSS</a>
    <a href="js.html">JAVASCRIPT</a>
    <a href="python.html">PYTHON</a>
    <a href="sql.html">SQL</a>
    <a href="java.html">JAVA</a>
    <a href="c.html">C++</a>
    <a href="excel.html" class="active">EXCEL</a>
    <a href="numpy.html">NUMPY</a>
    <a href="pandas.html">PANDAS</a>
    <a href="matplotlib.html">MATPLOTLIB</a>
    <a href="ai.html">AI & ML</a>
    <a href="r.html">R</a>
  </nav>"""
content = re.sub(sub_nav_pattern, new_sub_nav, content, flags=re.DOTALL)

# 3. Structural Cleanup: Remove empty structural wrapper divs
# These were likely left over from the modernization process
to_remove_wrappers = [
    'key-concepts', 'detailed-explanation', 'syntax-formula', 
    'real-world-usecase', 'common-mistakes', 'best-practices'
]

for wrapper in to_remove_wrappers:
    # Pattern to find the empty/redundant wrapper div and unwrap its content (simplified)
    # We want to remove <div class="wrapper"> </div> but keep the content inside the section-content-card if it exists
    # Actually, let's just remove the empty ones first
    content = re.sub(rf'<div class="{wrapper}">\s*</div>', '', content)
    # And then the wrapping ones that just wrap a section-content-card
    content = re.sub(rf'<div class="{wrapper}">\s*(<div class="section-content-card">.*?</div>)\s*</div>', r'\1', content, flags=re.DOTALL)

# 4. Remove triple/double section-content-card wrapping
content = re.sub(r'<div class="section-content-card">\s*<div class="section-content-card">', r'<div class="section-content-card">', content)
content = content.replace('</div>\s*</div>\s*</section>', '</div>\s*</section>') # This is risky with regex, better be careful

# 5. Fix double </div> at the end of sections if any
# Let's use a more robust way to clean up the nesting
# Finding all sections and fixing their internal structure

sections = re.findall(r'(<section id=".*?" class="lesson-section">.*?</section>)', content, flags=re.DOTALL)
new_sections = []
for sec in sections:
    # Remove redundant inner divs but keep the content
    # Look for patterns where a div wraps nothing but another div of the same class or similar
    sec = re.sub(r'<div class="section-content-card">\s*<div class="section-content-card">', r'<div class="section-content-card">', sec)
    sec = re.sub(r'</div>\s*</div>\s*(</div>\s*)?</section>', '</div>\n        </section>', sec)
    new_sections.append(sec)

# This replacement might be brittle, let's just do a string replacement for the most common artifacts
content = content.replace('<div class="section-content-card">\n            <div class="section-content-card">', '<div class="section-content-card">')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Final polish applied to excel.html")
