import os
import re

COURSE_DIR = 'courses'
TEMPLATE_TOP = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="icon" href="../assets/img/LOGO.jpeg" type="image/jpeg">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body class="learnx-page">

  <!-- TOP NAV -->
  <nav class="top-nav">
    <a href="../index1.html" class="brand">LearnX</a>
    <div class="top-nav-links">
      <a href="../index1.html"><i class="fas fa-home" style="margin-right:5px"></i> Dashboard</a>
      <a href="html.html">HTML</a>
      <a href="css.html">CSS</a>
      <a href="js.html">JavaScript</a>
      <a href="python.html">Python</a>
      <a href="sql.html">SQL</a>
    </div>
    
    <div class="top-nav-search">
      <input type="text" placeholder="Search..."/>
      <button><i class="fas fa-search"></i></button>
    </div>
    
    <div style="display:flex; gap:10px; margin-left:14px; align-items:center;">
      <span id="user-display" style="color:#aaa; font-size:13px; font-weight:600;"></span>
      <button id="logout-btn" class="nav-btn" style="background:transparent; border:1px solid #aaa; color:#ccc;">Logout</button>
    </div>
  </nav>

  <!-- CONTENT WRAPPER -->
  <div class="course-layout">
    
    <!-- SIDEBAR -->
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        {icon_html} {course_name} Tutorial
      </div>
      
      {sidebar_links}
      
      <div class="sidebar-footer">
        <a href="../index1.html"><i class="fas fa-arrow-left"></i> Back to Dashboard</a>
      </div>
    </aside>

    <!-- MAIN CONTENT -->
    <main class="course-main">
      <div class="course-content-area">
        
        <div class="breadcrumb">
          <a href="../index1.html">Home</a> <span>/</span> <span>{course_name}</span>
        </div>
        
        <h1 style="font-size:38px; margin-bottom: 40px; color:var(--secondary);">{course_name} Masterclass</h1>
"""

TEMPLATE_BOTTOM = """
      </div>
    </main>
  </div>

  <script type="module">
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-app.js";
    import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-auth.js";

    const firebaseConfig = {
      apiKey: "AIzaSyDrOAHTg-BuXyDRcBAV3uxoFHUwIzlV3bU",
      authDomain: "learnx-d823d.firebaseapp.com",
      projectId: "learnx-d823d",
      storageBucket: "learnx-d823d.appspot.com",
      messagingSenderId: "1036419202232",
      appId: "1:1036419202232:web:4f7778b3b4c16f1a61084d"
    };

    const app = initializeApp(firebaseConfig);
    const auth = getAuth(app);

    onAuthStateChanged(auth, (user) => {
      if (user) {
        document.getElementById('user-display').textContent = user.displayName || user.email.split('@')[0];
      } else {
        window.location.href = "../index.html";
      }
    });

    document.getElementById('logout-btn').addEventListener('click', () => {
      signOut(auth).then(() => {
        window.location.href = "../index.html";
      });
    });
  </script>

  <script>
    // Sidebar active state syncing
    const sections = document.querySelectorAll('.topic-section');
    const navLinks = document.querySelectorAll('.sidebar a[href^="#"]');

    window.addEventListener('scroll', () => {
      let current = '';
      sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (pageYOffset >= sectionTop - 150) {
          current = section.getAttribute('id');
        }
      });

      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').includes(current)) {
          link.classList.add('active');
        }
      });
    });
  </script>
</body>
</html>
"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip files that have already been converted to learnx-page
    if 'class="learnx-page"' in content:
        return False

    # 1. Extract Title
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else "LearnX Course"
    
    course_name = title.replace("LearnX | ", "").replace(" Masterclass", "").strip()
    if not course_name:
        course_name = "Course"

    # 2. Extract Sidebar icon and links
    sidebar_match = re.search(r'<div class="sidebar">(.*?)<div.*?Back to Dashboard', content, re.DOTALL)
    sidebar_html = sidebar_match.group(1) if sidebar_match else ""
    
    # icon
    icon_match = re.search(r'<i class="(fab fa-[^"]+|fas fa-[^"]+)"[^>]*></i>', sidebar_html)
    icon_html = icon_match.group(0) if icon_match else '<i class="fas fa-book"></i>'
    
    # Extract just the <a> links from sidebar
    links = re.findall(r'<a href="#[^"]*">.*?</a>', sidebar_html)
    sidebar_links = "\n      ".join(links)

    # 3. Extract Main content sections
    content_area_match = re.search(r'<div class="course-content">(.*?)</div>\s*<!-- End content -->|<div class="course-content">(.*?)<script src=', content, re.DOTALL)
    if content_area_match:
        content_html = content_area_match.group(1) or content_area_match.group(2)
    else:
        # Fallback
        c = content.split('<div class="course-content">')
        if len(c) > 1:
            content_html = c[1].split('</div> <!-- End content -->')[0]
        else:
            content_html = ""

    # 4. Refactor Sections (<div class="section"> -> <section class="topic-section">)
    # We also need to strip the <div class="section-header"> and <div class="section-content">
    
    # Process each section
    sections_raw = re.split(r'<div class="section" id="([^"]+)">', content_html)
    
    new_content = ""
    
    if len(sections_raw) > 1:
        # sections_raw[0] is everything before first section (like h1, buttons) - skip it
        for i in range(1, len(sections_raw), 2):
            sec_id = sections_raw[i]
            sec_body = sections_raw[i+1]
            
            # Extract header text
            header_match = re.search(r'<div class="section-header">\s*<h2>(.*?)</h2>', sec_body, re.DOTALL)
            header_text = header_match.group(1) if header_match else f"{course_name} Topic"
            
            # Extract content text
            content_match = re.search(r'<div class="section-content">(.*?)</div>\s*$', sec_body, re.DOTALL)
            if not content_match:
                content_match = re.search(r'<div class="section-content">(.*?)</div>\s*</div>', sec_body, re.DOTALL)
            
            inner_content = content_match.group(1) if content_match else sec_body
            
            # Clean up inner content slightly to fit new styling
            # Replace code blocks with exact new markup if needed, but existing is fine mostly
            inner_content = inner_content.replace('<pre><code', '<div class="example-box"><pre class="example-code"><code')
            inner_content = inner_content.replace('</code></pre>', '</code></pre></div>')
            
            new_section = f'''
        <section class="topic-section" id="{sec_id}">
          <h1>{header_text}</h1>
          {inner_content}
        </section>
'''
            new_content += new_section

    # Assemble
    final_html = TEMPLATE_TOP.format(
        title=title,
        icon_html=icon_html,
        course_name=course_name,
        sidebar_links=sidebar_links
    ) + new_content + TEMPLATE_BOTTOM

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    return True

if __name__ == "__main__":
    count = 0
    for filename in os.listdir(COURSE_DIR):
        if filename.endswith(".html") and filename != "html.html":  # Skip html.html as it is already perfect
            filepath = os.path.join(COURSE_DIR, filename)
            if process_file(filepath):
                count += 1
                print(f"Refactored {filename}")
    
    print(f"Total files refactored: {count}")

