 EventLink CM 🇨🇲

EventLink CM is a web-based event management and participation platform designed to connect event organizers with participants in Cameroon.

The platform allows organizers to create and manage events, monitor registrations and attendance, while participants can discover events, register for free tickets, receive event information, and access their tickets through a personal dashboard.

⸻

📌 Project Overview

EventLink CM aims to make event organization and participation easier by bringing the entire event process into one platform.

Instead of relying on scattered social media posts, messages, spreadsheets, or manual attendance lists, EventLink CM provides a centralized system where organizers and participants can interact with events.

Main Users

* Organizers — Create and manage events and monitor participants.
* Participants — Discover events, register, and manage their tickets.
* Administrators — Manage users, events, and platform data.

⸻

✨ Features

👤 User Accounts

* Participant registration
* Organizer registration
* User login and logout
* Email verification
* Password reset
* Separate organizer and participant dashboards
* User profile management

📅 Event Management

Organizers can:

* Create events
* Edit events
* Publish and manage events
* Add event descriptions
* Set event dates and locations
* Set participant limits
* Monitor registrations
* View registered participants
* Manage event attendance

🔎 Event Discovery

Participants can:

* Browse available events
* View event details
* Search for events
* Filter events
* Register for launched events
* View their registered events

🎟️ Free Tickets

The current version focuses on free event tickets.

Participants can:

* Register for free events
* Receive a digital ticket
* View their tickets from their dashboard
* Access a QR code associated with their ticket

Payment integration such as MTN Mobile Money and Orange Money is not included in the current phase.

📱 QR Code Attendance

EventLink CM supports QR-based attendance management.

Organizers can:

* Scan participant QR codes
* Mark participants as present
* Identify registered participants who have not checked in
* Monitor attendance

📊 Reports

Organizers can access attendance information, including:

* Total registered participants
* Number of participants present
* Number of participants absent
* Attendance statistics
* Event participation information

🌍 Language Support

The platform is designed to support:

* 🇬🇧 English


⸻

🛠️ Technology Stack

Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

Backend

* Python
* Django

Database

* PostgreSQL

Development Tools

* Git
* GitHub
* GitHub Codespaces
* pgAdmin 4

Deployment

The project is designed to support deployment using platforms such as:

* Render

⸻

📂 Project Structure

EventLink-CM/
│
├── manage.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
├── README.md
├── render.yaml
├── Procfile
│
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── api/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── permissions.py
│   ├── utils.py
│   ├── tests.py
│   │
│   └── migrations/
│       └── __init__.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── events.html
│   ├── event_detail.html
│   │
│   ├── accounts/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── organizer_register.html
│   │   ├── participant_register.html
│   │   ├── verify_email.html
│   │   ├── verification_success.html
│   │   ├── forgot_password.html
│   │   └── reset_password.html
│   │
│   ├── organizer/
│   │   ├── dashboard.html
│   │   ├── profile.html
│   │   ├── events.html
│   │   ├── create_event.html
│   │   ├── edit_event.html
│   │   ├── participants.html
│   │   ├── attendance.html
│   │   └── reports.html
│   │
│   └── participant/
│       ├── dashboard.html
│       ├── profile.html
│       ├── events.html
│       ├── event_detail.html
│       ├── my_tickets.html
│       ├── ticket_detail.html
│       └── notifications.html
│
├── static/
│   ├── css/
│   │   ├── style.css
│   │   ├── auth.css
│   │   ├── dashboard.css
│   │   ├── events.css
│   │   └── ticket.css
│   │
│   ├── js/
│   │   ├── main.js
│   │   ├── auth.js
│   │   ├── events.js
│   │   ├── dashboard.js
│   │   ├── ticket.js
│   │   └── qr-scanner.js
│   │
│   └── images/
│       ├── logo.png
│       ├── hero.jpg
│       └── placeholders/
│
└── ...

⸻

🚀 Getting Started

1. Clone the Repository

git clone https://github.com/jordiembah5-gif/eventlink_CM2.0.git

Move into the project directory:

cd EventLink-CM

⸻

2. Create a Virtual Environment

Windows

python -m venv venv

Activate it:

venv\Scripts\activate

macOS/Linux

python3 -m venv venv

Activate it:

source venv/bin/activate

⸻

3. Install Dependencies

pip install -r requirements.txt

⸻

🗄️ PostgreSQL Database Setup

EventLink CM uses PostgreSQL as its database.

Create a PostgreSQL database using PostgreSQL or pgAdmin 4.

Example database configuration:

DB_NAME=eventlink_cm
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

The actual values should be stored in the .env file and should not be committed to GitHub.

⸻

🔐 Environment Variables

Create a .env file in the project root.

Example:

SECRET_KEY=your-django-secret-key
DEBUG=True
DB_NAME=eventlink_cm
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
EMAIL_USE_TLS=True

Never upload passwords, API keys, database credentials, or other secrets to GitHub.

⸻

🧱 Database Migrations

After configuring PostgreSQL, run:

python manage.py makemigrations

Then:

python manage.py migrate

⸻

👨‍💻 Create an Administrator

Create a Django superuser:

python manage.py createsuperuser

Follow the instructions in the terminal.

⸻

▶️ Run the Development Server

Start the Django development server:

python manage.py runserver

The website will normally be available at:

http://127.0.0.1:8000/

You can also use:

http://localhost:8000/

⸻

🧪 Testing

Run the Django test suite with:

python manage.py test

You can also check the project configuration with:

python manage.py check

⸻

🔄 Development Workflow

The project can be developed collaboratively using Git and GitHub.

A typical workflow is:

git pull origin main

Create or switch to a feature branch:

git checkout -b feature-name

Make your changes, then:

git add .

Commit:

git commit -m "Describe your changes"

Push the branch:

git push origin feature-name

Create a Pull Request on GitHub and merge the completed work into main after review.

⸻

👥 Suggested Team Responsibilities

Person 1 — Infrastructure & Configuration

Responsible for:

* Django project setup
* Settings
* Environment variables
* PostgreSQL connection
* Dependencies
* Deployment configuration

Person 2 — Data & Backend

Responsible for:

* Database models
* Django admin
* Serializers
* Backend logic
* Permissions
* APIs

Person 3 — Frontend

Responsible for:

* HTML templates
* CSS
* JavaScript
* Responsive design
* User interface
* Connecting frontend pages to Django

Integration

The completed branches should be integrated into the main project and tested together before deployment.

⸻

🔐 Security

The following information should never be committed to GitHub:

* Database passwords
* Django secret keys
* Email passwords
* API keys
* Authentication tokens
* Private credentials

Use .env for local secrets.

The .gitignore file should include:

.env
venv/
__pycache__/
*.pyc
db.sqlite3

⸻

📈 Future Improvements

Possible future versions of EventLink CM may include:

* MTN Mobile Money payments
* Orange Money payments
* Paid event tickets
* Advanced event recommendations
* Push notifications
* SMS notifications
* Advanced analytics
* Event reviews and ratings
* Organizer verification
* Participant certificates
* Mobile application
* Improved QR attendance system
* Automated PDF reports

⸻

🎯 Project Goal

EventLink CM aims to provide a simple and centralized way for people to discover, organize, register for, and attend events.

The project focuses on making event participation easier for participants while reducing the manual work required by event organizers.

⸻

📞 Contact

For questions, suggestions, collaboration, or support, contact the EventLink CM team through the project’s official contact channel.

⸻

📄 License

This project is currently intended for educational and development purposes.

A formal open-source license can be added when the project is ready for public distribution.

⸻

🇨🇲 EventLink CM

Connecting organizers. Connecting participants. Connecting events.p
