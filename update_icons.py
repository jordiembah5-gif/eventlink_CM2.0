import os

files_to_update = [
    "EventLink CM Project/frontend/index.html",
    "EventLink CM Project/frontend/events.html",
    "EventLink CM Project/frontend/about.html",
    "EventLink CM Project/frontend/contact.html",
    "EventLink CM Project/frontend/login.html",
    "EventLink CM Project/frontend/register.html"
]

emoji_map = {
    "🎉": '<i class="fas fa-glass-cheers"></i>',
    "📅": '<i class="fas fa-calendar-alt"></i>',
    "🤝": '<i class="fas fa-handshake"></i>',
    "🎵": '<i class="fas fa-music"></i>',
    "📍": '<i class="fas fa-map-marker-alt"></i>',
    "💼": '<i class="fas fa-briefcase"></i>',
    "💻": '<i class="fas fa-laptop-code"></i>',
    "📚": '<i class="fas fa-book-open"></i>',
    "🎯": '<i class="fas fa-bullseye"></i>',
    "🌍": '<i class="fas fa-globe-africa"></i>',
    "🚀": '<i class="fas fa-rocket"></i>',
    "📧": '<i class="fas fa-envelope"></i>',
    "📞": '<i class="fas fa-phone"></i>'
}

font_awesome_link = '    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n</head>'

base_dir = r"g:\EventLink-CM_project"

for rel_path in files_to_update:
    path = os.path.join(base_dir, rel_path)
    if not os.path.exists(path):
        continue
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Add FontAwesome if not present
    if "font-awesome" not in content:
        content = content.replace("</head>", font_awesome_link)
        
    # Replace emojis
    for emoji, icon in emoji_map.items():
        content = content.replace(emoji, icon)
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Icons updated successfully!")
