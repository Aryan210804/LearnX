import re

def polish_c_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix duplicated General label
    content = content.replace('<div class="sidebar-section-label">General</div>\n      <div class="sidebar-section-label">General</div>', '<div class="sidebar-section-label">General</div>')

    # 2. Fix Sidebar icons (Adding missing ones)
    icon_fixes = {
        "c-functions-challenge": "fa-trophy",
        "c-inline-functions": "fa-bolt",
        "c-function-pointers": "fa-crosshairs",
        "c-structs-challenge": "fa-puzzle-piece",
        "c-nested-structures": "fa-sitemap",
        "c-structs-pointers": "fa-location-arrow",
        "c-typedef": "fa-tag",
        "c-struct-padding": "fa-align-justify",
        "c-enums": "fa-list-ol",
        "c-error-challenge": "fa-vial",
        "c-debugging": "fa-search",
        "c-null": "fa-ban",
        "c-error-handling": "fa-hand-holding-heart",
        "c-input-validation": "fa-user-check",
        "c-date": "fa-calendar-alt",
        "c-random-numbers": "fa-random",
        "c-macros": "fa-bullhorn",
        "c-organize-code": "fa-folder-open",
        "c-storage-classes": "fa-warehouse",
        "c-bitwise": "fa-binary",
        "c-fixed-width-integers": "fa-ruler-combined",
        "c-reference": "fa-bookmark",
        "c-examples": "fa-vials"
    }
    for href_id, icon in icon_fixes.items():
        content = re.sub(f'href="#{href_id}"><i class="fas fa-circle-notch"></i>', f'href="#{href_id}"><i class="fas {icon}"></i>', content)

    # 3. Fix Section Card Titles (Add lightbulb icon if missing)
    content = re.sub(r'<div class="section-content-card">\s*<h3>Key Concepts</h3>', r'<div class="section-content-card">\n        <h3><i class="fas fa-lightbulb"></i> Key Concepts</h3>', content)

    # 4. Fix closing tags at the end of file
    # Remove everything after </html>
    content = re.sub(r'</html>.*', '</html>', content, flags=re.DOTALL)

    # 5. Fix Javascript section selector
    content = content.replace("const sections = document.querySelectorAll('.topic-section');", "const sections = document.querySelectorAll('.lesson-section');")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

polish_c_html(r'c:\Users\DELL\Desktop\LearnX\courses\c.html')
print("Polishing of c.html completed")
