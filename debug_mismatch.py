import re

filepath = r'c:\Users\DELL\Desktop\LearnX\courses\excel.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

sections = re.findall(r'<section(.*?)>(.*?)</section>', content, flags=re.DOTALL)

for i, (attrs, inner) in enumerate(sections):
    div_open = inner.count('<div')
    div_close = inner.count('</div>')
    li_open = inner.count('<li')
    li_close = inner.count('</li>')
    if div_open != div_close or li_open != li_close:
        print(f"Section {i} (id={attrs}): div mismatch ({div_open} vs {div_close}), li mismatch ({li_open} vs {li_close})")
