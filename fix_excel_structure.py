import re

filepath = r'c:\Users\DELL\Desktop\LearnX\courses\excel.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

output = []
skip_mode = False

# Mapping of section IDs to desired icons for the premium look
icons = {
    "excel-formatting-main": "fas fa-paint-brush",
    "excel-format-painter": "fas fa-copy",
    "excel-format-colors": "fas fa-palette",
    "excel-format-fonts": "fas fa-font",
    "excel-format-borders": "fas fa-border-all",
    "excel-format-numbers": "fas fa-hashtag",
    "excel-data-analysis": "fas fa-chart-pie",
    "excel-sort": "fas fa-sort-amount-down",
    "excel-filter": "fas fa-filter",
    "excel-tables": "fas fa-table",
    "excel-conditional-format": "fas fa-highlighter",
    "excel-charts": "fas fa-chart-line",
    "excel-pivot-tables": "fas fa-columns"
}

i = 0
while i < len(lines):
    line = lines[i]
    
    # 1. Detect and skip the nested HTML boilerplate
    if '<!-- File: excel-formatting-data-analysis.html -->' in line:
        skip_mode = True
        i += 1
        continue
    
    if skip_mode:
        if '<!DOCTYPE html>' in line or '<html lang="en">' in line or '<head>' in line or '</head>' in line or '<body>' in line or '</body>' in line or '</html>' in line or '<meta charset="UTF-8">' in line or '<title>Excel Formatting' in line or '<link rel="stylesheet"' in line:
            i += 1
            continue
        
        # Detect a section start in the new part
        match = re.search(r'<section id="(.*?)">', line)
        if match:
            section_id = match.group(1)
            icon = icons.get(section_id, "fas fa-star")
            
            # Start modernized section
            output.append(f'        <section id="{section_id}" class="lesson-section">\n')
            
            # Collect content until </section>
            i += 1
            inner_content = []
            while i < len(lines) and '</section>' not in lines[i]:
                inner_content.append(lines[i])
                i += 1
            
            # Process inner content
            title = ""
            paragraph = ""
            key_concepts = []
            example_box = ""
            
            j = 0
            while j < len(inner_content):
                cl = inner_content[j]
                if '<h1>' in cl:
                    title = re.sub(r'</?h1>', '', cl).strip()
                elif j < 2 and '<p>' in cl:
                    paragraph = cl.strip()
                elif 'class="key-concepts"' in cl:
                    j += 1
                    while j < len(inner_content) and '</div>' not in inner_content[j]:
                        key_concepts.append(inner_content[j])
                        j += 1
                elif 'class="example-box"' in cl:
                    while j < len(inner_content) and '</div>' not in inner_content[j]:
                        example_box += inner_content[j]
                        j += 1
                    example_box += inner_content[j]
                j += 1
            
            # Reconstruct modernized section
            output.append(f'          <h1>{title}</h1>\n')
            if paragraph:
                output.append(f'          {paragraph}\n')
            
            if key_concepts:
                output.append('          <div class="section-content-card">\n')
                output.append(f'            <h3><i class="{icon}"></i> Key Concepts</h3>\n')
                # Clean up ul/li inside key concepts
                concepts_str = "".join(key_concepts)
                # Ensure no redundant tags
                concepts_str = re.sub(r'</?ul>', '', concepts_str)
                output.append('            <ul style="list-style: none; padding-left: 0;">\n')
                items = re.findall(r'<li>(.*?)</li>', concepts_str)
                for item in items:
                    output.append('              <li style="margin-bottom: 12px; display: flex; gap: 10px; align-items: flex-start;">\n')
                    output.append('                <i class="fas fa-check-circle" style="color: var(--accent-color); margin-top: 4px;"></i>\n')
                    output.append(f'                <span>{item}</span>\n')
                    output.append('              </li>\n')
                output.append('            </ul>\n')
                output.append('          </div>\n')
            
            if example_box:
                output.append('          ' + example_box.strip() + '\n')
            
            output.append('        </section>\n')
            i += 1
            continue
            
    # Stop skip_mode when we reach the completion section
    if '🎉 Excel Masterclass Complete!' in line:
        skip_mode = False

    # 2. Fix double wrapping in early sections
    if '<div class="section-content-card">' in line and i + 1 < len(lines) and '<div class="section-content-card">' in lines[i+1]:
        output.append(line)
        i += 2
        continue

    output.append(line)
    i += 1

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(output)

print("Cleaned and modernized excel.html successfully")
