import re

filepath = r'c:\Users\DELL\Desktop\LearnX\courses\excel.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix unclosed <p> tags
content = re.sub(r'(<p>[^<]*?)(?=\s*<(div|section|h1|h3|ul|ol|pre|button))', r'\1</p>', content)

# 2. Fix Section 56 specifically (common pattern)
content = content.replace(
    '<button class="try-btn" onclick="openTryIt(this)">Try it Yourself</button>\n          <div class="tryit-panel">',
    '<button class="try-btn" onclick="openTryIt(this)">Try it Yourself</button>\n          <div class="tryit-panel">'
) # No change here, just placeholder

# Actually, let's fix the example-box closing
# If a section has an example-box and it ends without closing it
sections = re.findall(r'(<section id=".*?" class="lesson-section">)(.*?)(</section>)', content, flags=re.DOTALL)
new_sections = []
for start, inner, end in sections:
    div_diff = inner.count('<div') - inner.count('</div>')
    if div_diff > 0:
        # Check if the last div is an example-box or tryit-panel
        if '<div class="example-box">' in inner and '</div>\n          <div class="example-box">' not in inner:
             # This is complex. Let's just append the missing </div>s at the end of the inner content
             inner += '</div>' * div_diff
    new_sections.append(f"{start}{inner}{end}")

# Join back
# We can't just join if there's content between sections. 
# Better to use re.sub with a function

def fix_section(match):
    start = match.group(1)
    inner = match.group(2)
    end = match.group(3)
    div_diff = inner.count('<div') - inner.count('</div>')
    if div_diff > 0:
        inner += '</div>' * div_diff
    li_diff = inner.count('<li') - inner.count('</li>')
    if li_diff > 0:
        inner = inner.replace('</li>', '') # clean up
        inner = re.sub(r'<li>(.*?)(\s*<li|\s*</ul>)', r'<li>\1</li>\2', inner, flags=re.DOTALL)
    
    # Fix the unclosed <p> again more carefully
    inner = re.sub(r'(<p>[^<]*?)(?=\s*<div)', r'\1</p>', inner)
    
    return f"{start}{inner}{end}"

content = re.sub(r'(<section id=".*?" class="lesson-section">)(.*?)(</section>)', fix_section, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML tag balance fix completed")
