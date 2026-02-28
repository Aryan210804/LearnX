import re

# Update home.html
with open('home.html', 'r', encoding='utf-8') as f:
    home_content = f.read()

# 1. Replace all courses links with index.html in home.html (forcing login)
home_content = re.sub(r'href="(courses/[^"]+)"', 'href="index.html"', home_content)

# 2. Remove certificate from top bar
home_content = home_content.replace('and earn certificates.', '')

# 3. Modify feature item about certificates
feat_old = """<div class="feature-icon"><i class="fas fa-certificate"></i></div>
        <div class="feature-text">
          <h4>Earn Certificates</h4>
          <p>Complete courses and earn certificates to showcase your skills.</p>
        </div>"""
feat_new = """<div class="feature-icon"><i class="fas fa-laptop-code"></i></div>
        <div class="feature-text">
          <h4>Real-world Projects</h4>
          <p>Build real-world projects to showcase your skills to employers.</p>
        </div>"""
home_content = home_content.replace(feat_old, feat_new)

with open('home.html', 'w', encoding='utf-8') as f:
    f.write(home_content)


# Update index1.html
with open('index1.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

stat_old = """<div class="dash-stat">
        <div class="dash-stat-icon" style="background:rgba(229,57,53,0.1);color:#e53935"><i class="fas fa-certificate"></i></div>
        <div>
          <div class="dash-stat-num">14</div>
          <div class="dash-stat-label">Certificates</div>
        </div>
      </div>"""
stat_new = """<div class="dash-stat">
        <div class="dash-stat-icon" style="background:rgba(229,57,53,0.1);color:#e53935"><i class="fas fa-tasks"></i></div>
        <div>
          <div class="dash-stat-num">150+</div>
          <div class="dash-stat-label">Exercises</div>
        </div>
      </div>"""
index_content = index_content.replace(stat_old, stat_new)

with open('index1.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

print('Done')
