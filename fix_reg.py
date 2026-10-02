with open('EventLink CM Project/frontend/register.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the broken inject
if '`n' in html:
    html = html.replace('`n            <button type="submit" class="primary-btn">', '')
    html = html.replace('<select id="gender"', '\n            <select id="gender"')
    html = html.replace('</select>', '</select>\n            <button type="submit" class="primary-btn">')

with open('EventLink CM Project/frontend/register.html', 'w', encoding='utf-8') as f:
    f.write(html)
