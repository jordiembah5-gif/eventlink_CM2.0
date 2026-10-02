import os

html_path = 'EventLink CM Project/frontend/create-event.html'
js_path = 'EventLink CM Project/frontend/js/create-event.js'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace text input with datetime-local
html = html.replace(
    '<input id="eventDate" type="text" placeholder="Date (e.g. 15 November 2026)" required>',
    '<input id="eventDate" type="datetime-local" required>'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Add DOMContentLoaded listener to set the min attribute
min_date_script = """
document.addEventListener('DOMContentLoaded', () => {
    const dateInput = document.getElementById('eventDate');
    if (dateInput) {
        // Get current local time and format it to YYYY-MM-DDTHH:MM for the input min attribute
        const now = new Date();
        now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
        const minDateTime = now.toISOString().slice(0, 16);
        dateInput.min = minDateTime;
    }
});

// Mobile Menu Toggle
"""

if "dateInput.min" not in js:
    js = js.replace('// Mobile Menu Toggle\n', min_date_script)

# Format the date properly before sending to the backend
if ".replace('T', ' ')" not in js:
    js = js.replace(
        'const date = document.getElementById("eventDate").value;',
        'const date = document.getElementById("eventDate").value.replace("T", " ");'
    )

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
