import re

def modernize_c_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Head Section with premium styles
    head_match = re.search(r'<head>.*?</head>', content, re.DOTALL)
    if head_match:
        new_head = """<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LearnX | C Masterclass</title>
  <link rel="icon" href="../assets/img/LOGO.jpeg" type="image/jpeg">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../assets/css/style.css">
  <style>
    :root {
      --primary-gradient: linear-gradient(135deg, #00599C 0%, #004481 100%);
      --accent-color: #00599C;
      --sidebar-bg-modern: #1b1e23;
      --card-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
      --card-radius: 16px;
    }

    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: #00599C; border-radius: 4px; }
    html { scroll-behavior: smooth; }

    /* Modernized sub-nav */
    .sub-nav {
      background: #1b1e23 !important;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      display: flex;
      align-items: center;
      padding: 0 15px;
      gap: 5px;
      overflow-x: auto;
      scrollbar-width: none;
      z-index: 1000;
      position: fixed;
      top: 60px; /* height of top-nav */
      left: 0;
      right: 0;
      height: 50px;
    }
    .sub-nav::-webkit-scrollbar { display: none; }
    .sub-nav a {
      color: #999;
      font-size: 13px;
      font-weight: 600;
      padding: 0 15px;
      height: 100%;
      display: flex;
      align-items: center;
      text-decoration: none;
      transition: all 0.2s;
      white-space: nowrap;
    }
    .sub-nav a:hover { color: #fff; background: rgba(255, 255, 255, 0.05); }
    .sub-nav a.active { background: #00599C !important; color: #fff !important; }

    /* Premium Sidebar */
    .sidebar { background: var(--sidebar-bg-modern) !important; border-right: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; }
    .sidebar-header {
      padding: 25px 20px;
      font-size: 16px;
      font-weight: 800;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 12px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      margin-bottom: 10px;
    }
    .sidebar a {
      border-radius: 8px;
      margin: 2px 12px;
      padding: 10px 15px;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 10px;
      color: #999;
      font-size: 13.5px;
      text-decoration: none !important;
    }
    .sidebar a:hover { background: rgba(0, 89, 156, 0.15); color: #fff; transform: translateX(3px); }
    .sidebar a.active {
      background: var(--primary-gradient) !important;
      color: #fff !important;
      font-weight: 600;
      box-shadow: 0 4px 12px rgba(0, 89, 156, 0.3);
    }
    .sidebar-section-label {
      padding: 15px 25px 8px;
      font-size: 11px;
      font-weight: 700;
      color: #555;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    /* Content Cards */
    .lesson-section {
      background: var(--bg-card);
      padding: 50px;
      border-radius: var(--card-radius);
      margin-bottom: 60px;
      box-shadow: var(--card-shadow);
      border: 1px solid var(--border);
      position: relative;
      overflow: hidden;
      color: var(--text);
    }
    .lesson-section::after {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--primary-gradient);
    }
    .lesson-section h1 {
      font-size: 32px;
      font-weight: 800;
      margin-bottom: 25px;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 15px;
    }
    .section-content-card {
      background: rgba(0, 89, 156, 0.03);
      border: 1px solid rgba(0, 89, 156, 0.1);
      border-radius: 12px;
      padding: 30px;
      margin: 25px 0;
    }
    .section-content-card h3 {
      font-size: 18px;
      color: #333;
      margin-top: 0;
      margin-bottom: 15px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    [data-theme="dark"] .section-content-card {
      background: rgba(255, 255, 255, 0.02);
      border-color: rgba(255, 255, 255, 0.05);
    }
    [data-theme="dark"] .section-content-card h3 { color: #fff; }

    .example-box {
      background: #1e1e1e;
      border-radius: 12px;
      margin: 25px 0;
      border: 1px solid #333;
    }
    .example-header {
      padding: 12px 20px;
      background: #252525;
      border-bottom: 1px solid #333;
      color: #aaa;
      font-size: 13px;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 10px;
      border-radius: 12px 12px 0 0;
    }
    .example-code {
      padding: 20px;
      margin: 0;
      color: #dcdcdc;
      font-family: 'Fira Code', 'Courier New', monospace;
      font-size: 14px;
      line-height: 1.6;
      overflow-x: auto;
    }

    .breadcrumb {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 30px;
      color: #888;
      font-size: 14px;
    }
    .breadcrumb a { color: var(--accent-color); text-decoration: none; font-weight: 600; }
    .breadcrumb span { color: #555; }
  </style>
</head>"""
        content = content.replace(head_match.group(0), new_head)

    # 2. Add Sub-Nav after Top-Nav
    sub_nav = """  <!-- SUB NAV -->
  <nav class="sub-nav">
    <a href="html.html">HTML</a>
    <a href="css.html">CSS</a>
    <a href="js.html">JAVASCRIPT</a>
    <a href="python.html">PYTHON</a>
    <a href="sql.html">SQL</a>
    <a href="java.html">JAVA</a>
    <a href="c.html" class="active">C</a>
    <a href="excel.html">EXCEL</a>
    <a href="numpy.html">NUMPY</a>
    <a href="pandas.html">PANDAS</a>
    <a href="matplotlib.html">MATPLOTLIB</a>
    <a href="ai.html">AI & ML</a>
    <a href="r.html">R</a>
  </nav>"""
    if '<!-- SUB NAV -->' not in content:
        content = content.replace('</nav>', '</nav>\n\n' + sub_nav, 1)

    # 3. Modernize Sidebar (Remove <li> and fix structure)
    sidebar_content = re.search(r'<aside class="sidebar".*?</aside>', content, re.DOTALL)
    if sidebar_content:
        # Extract individual links and clean them
        links = re.findall(r'<li><a href="(.*?)">(.*?)</a></li>', sidebar_content.group(0))
        
        new_sidebar_inner = """<div class="sidebar-header">
        <i class="fas fa-microchip" style="color:#00599C"></i> C Masterclass
      </div>
      <div class="sidebar-section-label">General</div>"""
        
        # Mapping section labels
        section_labels = {
            "c-home": "General",
            "c-functions": "Advanced Functions",
            "c-create-files": "File Operations",
            "c-structures": "Data Structures",
            "c-enums": "Memory & Types",
            "c-errors": "Debugging & Safety",
            "c-date": "Extras",
            "c-projects": "Applications"
        }

        icon_map = {
            "c-home": "fa-house",
            "c-intro": "fa-book",
            "c-get-started": "fa-rocket",
            "c-syntax": "fa-code",
            "c-output": "fa-terminal",
            "c-comments": "fa-comment-dots",
            "c-variables": "fa-box",
            "c-data-types": "fa-database",
            "c-type-conversion": "fa-exchange-alt",
            "c-constants": "fa-lock",
            "c-operators": "fa-calculator",
            "c-booleans": "fa-toggle-on",
            "c-if-else": "fa-code-branch",
            "c-switch": "fa-list-ul",
            "c-while-loop": "fa-redo",
            "c-for-loop": "fa-sync",
            "c-break-continue": "fa-strikethrough",
            "c-arrays": "fa-layer-group",
            "c-strings": "fa-quote-left",
            "c-user-input": "fa-keyboard",
            "c-memory-address": "fa-microchip",
            "c-pointers": "fa-hand-pointer",
            "c-functions": "fa-function",
            "c-function-parameters": "fa-sliders-h",
            "c-scope": "fa-eye",
            "c-function-declaration": "fa-file-signature",
            "c-math-functions": "fa-plus-minus",
            "c-recursion": "fa-undo",
            "c-create-files": "fa-file-medical",
            "c-write-to-files": "fa-file-export",
            "c-read-files": "fa-file-import",
            "c-structures": "fa-sitemap",
            "c-unions": "fa-object-group",
            "c-memory-management": "fa-memory",
            "c-errors": "fa-bug",
            "c-projects": "fa-laptop-code"
        }

        current_label = ""
        for href, text in links:
            id_val = href.lstrip('#')
            if id_val in section_labels:
                new_sidebar_inner += f'\n      <div class="sidebar-section-label">{section_labels[id_val]}</div>'
            
            icon = icon_map.get(id_val, "fa-circle-notch")
            active_class = ' class="active"' if id_val == "c-home" else ""
            new_sidebar_inner += f'\n      <a href="{href}"{active_class}><i class="fas {icon}"></i> {text}</a>'

        new_sidebar_inner += """
      <div class="sidebar-footer">
        <a href="../index1.html"><i class="fas fa-arrow-left"></i> Back to Dashboard</a>
      </div>"""
        
        content = re.sub(r'<aside class="sidebar".*?</aside>', f'<aside class="sidebar" id="sidebar">\n      {new_sidebar_inner}\n    </aside>', content, flags=re.DOTALL)

    # 4. Wrap Main Content
    if '<main class="course-main">' not in content:
        # User likely removed main tag. Reconstruct layout.
        content = content.replace('</aside>', '</aside>\n\n    <main class="course-main">\n      <div class="course-content-area">\n        <div class="breadcrumb">\n          <a href="../index1.html">Home</a> <span>/</span> <span>C Masterclass</span>\n        </div>')
        content += '\n      </div>\n    </main>'

    # 5. Standardize Section Card UI
    # Replace .key-concepts-box with .section-content-card
    content = content.replace('<div class="key-concepts-box">', '<div class="section-content-card">')
    
    # Ensure sections have .lesson-section class
    content = re.sub(r'<section id="(.*?)"\s*>', r'<section id="\1" class="lesson-section">', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

modernize_c_html(r'c:\Users\DELL\Desktop\LearnX\courses\c.html')
print("Modernization of c.html completed")
