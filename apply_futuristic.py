import os
import shutil

# Paths
artifact_dir = r"C:\Users\jordi\.gemini\antigravity\brain\2d3814a1-29f2-49a2-8be2-829dbd744638"
images_dir = r"g:\EventLink-CM_project\EventLink CM Project\frontend\images"
base_dir = r"g:\EventLink-CM_project"

# Ensure images dir exists
os.makedirs(images_dir, exist_ok=True)

# Copy generated images to the frontend
image_mapping = {
    "futuristic_music_1790178561703.jpg": "futuristic_music.jpg",
    "futuristic_tech_1790178606353.jpg": "futuristic_tech.jpg",
    "futuristic_business_1790178621563.jpg": "futuristic_business.jpg"
}

for src, dest in image_mapping.items():
    src_path = os.path.join(artifact_dir, src)
    if os.path.exists(src_path):
        shutil.copy(src_path, os.path.join(images_dir, dest))

# Inject CSS into all HTML files
html_files = [
    "EventLink CM Project/frontend/index.html",
    "EventLink CM Project/frontend/events.html",
    "EventLink CM Project/frontend/about.html",
    "EventLink CM Project/frontend/contact.html",
    "EventLink CM Project/frontend/login.html",
    "EventLink CM Project/frontend/register.html",
    "EventLink CM Project/frontend/create-event.html"
]

for rel_path in html_files:
    path = os.path.join(base_dir, rel_path)
    if not os.path.exists(path):
        continue
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "futuristic.css" not in content:
        content = content.replace("</head>", '    <link rel="stylesheet" href="css/futuristic.css">\n</head>')
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

print("CSS injected and images copied!")
