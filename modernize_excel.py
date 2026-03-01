    import re

filepath = r'c:\Users\DELL\Desktop\LearnX\courses\excel.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Head
head_pattern = re.compile(r'<head>.*?</head>', re.DOTALL)
new_head = """<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LearnX | Excel Masterclass</title>
  <link rel="icon" href="../assets/img/LOGO.jpeg" type="image/jpeg">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../assets/css/style.css">
  <style>
    :root {
      --primary-gradient: linear-gradient(135deg, #217346 0%, #1a5c38 100%);
      --accent-color: #2da44e;
      --sidebar-bg-modern: #1b1e23;
      --card-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
      --card-radius: 16px;
    }
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #f1f1f1; }
    ::-webkit-scrollbar-thumb { background: #217346; border-radius: 4px; }
    html { scroll-behavior: smooth; }
    .sidebar { background: var(--sidebar-bg-modern); border-right: 1px solid rgba(255, 255, 255, 0.05); padding-top: 20px; }
    .sidebar a { border-radius: 8px; margin: 4px 15px; padding: 10px 18px; transition: all 0.3s ease; display: flex; align-items: center; gap: 10px; color: #ccc; font-size: 14px; text-decoration: none; }
    .sidebar a:hover { background: rgba(33, 115, 70, 0.1); color: var(--accent-color); transform: translateX(5px); }
    .sidebar a.active { background: var(--primary-gradient); box-shadow: 0 4px 15px rgba(33, 115, 70, 0.3); color: #fff; }
    .sidebar-section-label { padding: 15px 25px 8px; font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; color: #666; font-weight: 700; }
    .lesson-section { background: #fff; padding: 45px; border-radius: var(--card-radius); margin-bottom: 50px; box-shadow: var(--card-shadow); border: 1px solid #eee; position: relative; overflow: hidden; }
    .lesson-section::before { content: ''; position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: var(--primary-gradient); }
    .dark-mode .lesson-section { background: #24292e; border-color: #30363d; color: #c9d1d9; }
    .breadcrumb { margin-bottom: 30px; font-size: 14px; color: #666; }
    .breadcrumb a { color: var(--accent-color); font-weight: 600; text-decoration: none; }
  </style>
</head>"""
content = head_pattern.sub(new_head, content)

# 2. Update Sidebar and Layout Start
layout_start_pattern = re.compile(r'<div class="course-layout">.*?<div class="breadcrumb">', re.DOTALL)
new_layout_start = """<div class="course-layout">
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <i class="fas fa-file-excel" style="color:#217346"></i> Excel Masterclass
      </div>
      <div class="sidebar-section-label">Getting Started</div>
      <a href="#excel-home" class="active"><i class="fas fa-house"></i> Home Tab</a>
      <a href="#excel-introduction"><i class="fas fa-book"></i> Introduction</a>
      <a href="#excel-get-started"><i class="fas fa-rocket"></i> Get Started</a>
      <a href="#excel-overview"><i class="fas fa-desktop"></i> Interface</a>
      <div class="sidebar-section-label">Basics & Editing</div>
      <a href="#excel-syntax"><i class="fas fa-code"></i> Syntax</a>
      <a href="#excel-ranges"><i class="fas fa-th"></i> Ranges</a>
      <a href="#excel-fill"><i class="fas fa-fill-drip"></i> Fill & Series</a>
      <a href="#excel-move-cells"><i class="fas fa-arrows-alt"></i> Move Cells</a>
      <a href="#excel-add-cells"><i class="fas fa-plus-square"></i> Add Cells</a>
      <a href="#excel-delete-cells"><i class="fas fa-minus-square"></i> Delete Cells</a>
      <a href="#excel-undo-redo"><i class="fas fa-undo-alt"></i> Undo / Redo</a>
      <div class="sidebar-section-label">Formulas & Logic</div>
      <a href="#excel-formulas"><i class="fas fa-calculator"></i> All Formulas</a>
      <a href="#excel-relative-reference"><i class="fas fa-link"></i> Relative Ref</a>
      <a href="#excel-absolute-reference"><i class="fas fa-lock"></i> Absolute Ref</a>
      <a href="#excel-arithmetic-operators"><i class="fas fa-percent"></i> Operators</a>
      <a href="#excel-parentheses"><i class="fas fa-brackets-curly"></i> Parentheses</a>
      <a href="#excel-functions"><i class="fas fa-function"></i> Basic Functions</a>
      <div class="sidebar-section-label">Formatting</div>
      <a href="#excel-formatting"><i class="fas fa-paint-brush"></i> Main Formatting</a>
      <a href="#excel-format-painter"><i class="fas fa-copy"></i> Format Painter</a>
      <a href="#excel-format-colors"><i class="fas fa-palette"></i> Colors</a>
      <a href="#excel-format-fonts"><i class="fas fa-font"></i> Fonts</a>
      <a href="#excel-format-borders"><i class="fas fa-border-all"></i> Borders</a>
      <a href="#excel-format-numbers"><i class="fas fa-hashtag"></i> Numbers</a>
      <div class="sidebar-section-label">Data Analysis</div>
      <a href="#excel-sort"><i class="fas fa-sort-amount-down"></i> Sort</a>
      <a href="#excel-filter"><i class="fas fa-filter"></i> Filter</a>
      <a href="#excel-tables"><i class="fas fa-table"></i> Tables</a>
      <a href="#excel-conditional-format"><i class="fas fa-highlighter"></i> Conditional Format</a>
      <a href="#excel-charts"><i class="fas fa-chart-line"></i> Charts</a>
      <a href="#table-pivot-intro"><i class="fas fa-columns"></i> Pivot Tables</a>
      <div class="sidebar-footer">
        <a href="../index1.html"><i class="fas fa-arrow-left"></i> Back to Dashboard</a>
      </div>
    </aside>
    <main class="course-main">
      <div class="course-content-area">
        <div class="breadcrumb">"""
content = layout_start_pattern.sub(new_layout_start, content)

# 3. Standardize Sections
# Replace <section id="xxx"> with <section id="xxx" class="lesson-section">
# But avoid those that already have a class or special styling
content = re.sub(r'<section id="([^"]+)"(?!\s+class)', r'<section id="\1" class="lesson-section"', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Modernized excel.html successfully")
