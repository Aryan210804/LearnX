import re

filepath = r'c:\Users\DELL\Desktop\LearnX\courses\excel.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for sections
section_pattern = r'(<section id="(.*?)" class="lesson-section">)(.*?)(</section>)'

def modernize_section_content(match):
    start_tag = match.group(1)
    section_id = match.group(2)
    inner_content = match.group(3)
    end_tag = match.group(4)
    
    # If already has section-content-card, skip or refine
    if 'section-content-card' in inner_content:
        return match.group(0)
    
    # Extract existing parts
    title_match = re.search(r'<h1>(.*?)</h1>', inner_content)
    title = title_match.group(1) if title_match else ""
    
    # Split content by major blocks
    p_match = re.search(r'<p>(.*?)</p>', inner_content)
    intro_p = f"<p>{p_match.group(1)}</p>" if p_match else ""
    
    # Key Concepts
    kc_match = re.search(r'<div class="key-concepts">(.*?)</div>', inner_content, flags=re.DOTALL)
    kc_content = kc_match.group(1) if kc_match else ""
    
    # Syntax
    syntax_match = re.search(r'<div class="syntax-formula">(.*?)</div>', inner_content, flags=re.DOTALL)
    syntax_content = syntax_match.group(1) if syntax_match else ""
    
    # Example Box
    example_match = re.search(r'<div class="example-box">(.*?)</div>', inner_content, flags=re.DOTALL)
    example_content = example_match.group(1) if example_match else ""
    
    # Reconstruct
    new_inner = f"\n          <h1>{title}</h1>\n          {intro_p}\n"
    
    if kc_content:
        new_inner += '          <div class="section-content-card">\n'
        new_inner += '            <h3><i class="fas fa-lightbulb"></i> Key Concepts</h3>\n'
        # Convert ul to premium style
        items = re.findall(r'<li>(.*?)</li>', kc_content)
        if items:
            new_inner += '            <ul style="list-style: none; padding-left: 0;">\n'
            for item in items:
                new_inner += '              <li style="margin-bottom: 12px; display: flex; gap: 10px; align-items: flex-start;">\n'
                new_inner += '                <i class="fas fa-check-circle" style="color: var(--accent-color); margin-top: 4px;"></i>\n'
                new_inner += f'                <span>{item}</span>\n'
                new_inner += '              </li>\n'
            new_inner += '            </ul>\n'
        else:
            new_inner += f"            {kc_content.strip()}\n"
        new_inner += '          </div>\n'
        
    if syntax_content:
        new_inner += '          <div class="section-content-card">\n'
        new_inner += '            <h3><i class="fas fa-code"></i> Syntax / Formula</h3>\n'
        new_inner += f"            {syntax_content.strip()}\n"
        new_inner += '          </div>\n'
        
    if example_content:
        # Check if it already has the header
        if 'example-header' not in example_content:
            new_inner += '          <div class="example-box">\n'
            new_inner += '            <div class="example-header"><i class="fas fa-code"></i> Example</div>\n'
            new_inner += f"            {example_content.strip()}\n"
            new_inner += '          </div>\n'
        else:
            new_inner += f'          <div class="example-box">{example_content.strip()}</div>\n'
            
    return f"{start_tag}{new_inner}        {end_tag}"

new_content = re.sub(section_pattern, modernize_section_content, content, flags=re.DOTALL)

# Cleanup some overlaps
new_content = new_content.replace('          <div class="example-box">          <div class="example-box">', '          <div class="example-box">')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Mass modernization completed for all sections in excel.html")
