def check_tags(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    tags = ['div', 'section', 'main', 'aside', 'nav', 'ul', 'li', 'h1', 'h2', 'h3']
    for tag in tags:
        open_count = content.count(f'<{tag}')
        close_count = content.count(f'</{tag}>')
        print(f"{tag}: {open_count} open, {close_count} close")

check_tags(r'c:\Users\DELL\Desktop\LearnX\courses\excel.html')
