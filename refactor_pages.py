import os
import re

base_dir = r"g:\EventLink-CM_project\EventLink CM Project\frontend"

html_files = [
    "index.html",
    "events.html",
    "about.html",
    "contact.html",
    "login.html",
    "register.html",
    "create-event.html"
]

footer_html = """
<footer style="background-color: #f9f9f9; padding: 40px 10%; border-top: 1px solid #ddd; margin-top: 40px;">
    <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
        <div style="flex: 1; min-width: 250px;">
            <h3 style="color: #10003c; margin-bottom: 15px; font-family: 'Orbitron', sans-serif;">EventLink CM</h3>
            <p style="color: #555; line-height: 1.6;">Your premium platform to discover, organize, and connect with people through amazing events across Cameroon. We bring the community together, one event at a time.</p>
        </div>
        <div style="flex: 1; min-width: 200px;">
            <h3 style="color: #10003c; margin-bottom: 15px; font-family: 'Orbitron', sans-serif;">Quick Links</h3>
            <ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 10px;"><a href="/" style="color: #28a745; text-decoration: none; font-weight: bold;">Home</a></li>
                <li style="margin-bottom: 10px;"><a href="/events" style="color: #28a745; text-decoration: none; font-weight: bold;">Browse Events</a></li>
                <li style="margin-bottom: 10px;"><a href="/create-event" style="color: #28a745; text-decoration: none; font-weight: bold;">Create an Event</a></li>
                <li style="margin-bottom: 10px;"><a href="/about" style="color: #28a745; text-decoration: none; font-weight: bold;">About Us</a></li>
                <li style="margin-bottom: 10px;"><a href="/contact" style="color: #28a745; text-decoration: none; font-weight: bold;">Contact</a></li>
            </ul>
        </div>
        <div style="flex: 1; min-width: 250px;">
            <h3 style="color: #10003c; margin-bottom: 15px; font-family: 'Orbitron', sans-serif;">Contact Us</h3>
            <p style="color: #555; margin-bottom: 10px;"><i class="fas fa-map-marker-alt"></i> 123 Innovation Avenue, Douala, Cameroon</p>
            <p style="color: #555; margin-bottom: 10px;"><i class="fas fa-envelope"></i> info@eventlink-cm.com</p>
            <p style="color: #555;"><i class="fas fa-phone"></i> +237 600 000 000</p>
        </div>
    </div>
    <div style="text-align: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; color: #777;">
        <p>© 2026 EventLink CM. Built with precision and care. All rights reserved.</p>
    </div>
</footer>
"""

for filename in html_files:
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        continue
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace links
    content = content.replace('href="index.html"', 'href="/"')
    content = content.replace('href="events.html"', 'href="/events"')
    content = content.replace('href="about.html"', 'href="/about"')
    content = content.replace('href="contact.html"', 'href="/contact"')
    content = content.replace('href="login.html"', 'href="/login"')
    content = content.replace('href="register.html"', 'href="/register"')
    content = content.replace('href="create-event.html"', 'href="/create-event"')
    
    # Replace JS references (window.location.href)
    content = content.replace("window.location.href = 'events.html", "window.location.href = '/events")
    content = content.replace("window.location.href = 'login.html'", "window.location.href = '/login'")

    # Replace footer
    # Using regex to find the entire footer block and replace it
    content = re.sub(r'<footer.*?>.*?</footer>', footer_html, content, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("HTML pages refactored successfully.")
