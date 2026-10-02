 EventLink CM 🎫🇨🇲

Connect • Discover • Experience

EventLink CM is a web-based event discovery and management platform designed to connect event organizers with participants across Cameroon.

The platform allows users to discover available events, create accounts, register for events, organize events, manage RSVPs, and track attendance through QR-code scanning and event analytics.

⸻

📌 Project Overview

Finding and participating in events can be difficult when event information is scattered across different platforms and communication channels.

EventLink CM provides a centralized platform where:

* Participants can discover events.
* Users can create accounts and log in.
* Participants can search and filter events.
* Participants can RSVP to events.
* Organizers can create and manage their events.
* Organizers can view registered participants.
* Event attendance can be recorded through QR-code scanning.
* Organizers can view event attendance analytics.
* The application provides a simple, responsive interface for users.

The project is developed as an academic software-development project with the goal of demonstrating the design and implementation of a real-world event management solution.

⸻

🎯 Aim

The main aim of EventLink CM is to provide a simple and accessible digital platform for discovering, organizing and participating in events in Cameroon.

⸻

🎯 Objectives

The project objectives are to:

1. Create a centralized platform for event discovery.
2. Allow users to register and log in to the platform.
3. Allow organizers to create events.
4. Allow participants to browse and search for events.
5. Allow participants to RSVP to events.
6. Keep track of event registrations.
7. Support QR-based attendance scanning.
8. Provide organizers with attendance information and analytics.
9. Provide a responsive and user-friendly interface.
10. Provide a foundation that can be expanded with additional event-management features.

⸻

✨ Main Features

👤 User Registration

Users can create an EventLink CM account using:

* Name
* Email address
* Password
* Gender

The backend checks whether an email address has already been registered.

🔐 Login

Registered users can log in using their email address and password.

📅 Event Discovery

Users can view available events and obtain information such as:

* Event name
* Category
* Location
* Date
* Event image/icon
* Organizer

🔎 Event Search and Filtering

The frontend provides event searching and category filtering.

Available categories include examples such as:

* Music
* Business
* Technology
* Education

📝 Event RSVP

Participants can register for an event through the RSVP functionality.

The system prevents the same user from registering for the same event more than once.

🏗️ Event Creation

Organizers can create events by providing information such as:

* Event name
* Category
* Location
* Date
* Event image/icon
* Organizer email

📊 Event Analytics

Organizers can retrieve information about their events, including:

* Total RSVPs
* Number of participants who arrived
* Participant information
* Gender breakdown
* Attendance status
* Arrival time

🎟️ QR Attendance Scanning

The backend provides an attendance-scanning endpoint.

When an RSVP is scanned:

1. The system identifies the participant.
2. The participant’s RSVP is located.
3. The RSVP is marked as scanned.
4. The arrival time is recorded.
5. The system returns the attendance result.

The system also prevents an already-scanned ticket from being counted as a new attendance.

⸻

🏗️ System Architecture

EventLink CM uses a simple client-server architecture.

┌──────────────────────────────┐
│        USER / BROWSER        │
│                              │
│ HTML + CSS + JavaScript      │
└──────────────┬───────────────┘
               │
               │ HTTP Requests
               ▼
┌──────────────────────────────┐
│          FASTAPI             │
│          Backend             │
│                              │
│ Authentication               │
│ Event Management             │
│ RSVP Management              │
│ Attendance                   │
│ Analytics                    │
└──────────────┬───────────────┘
               │
               │ SQLAlchemy ORM
               ▼
┌──────────────────────────────┐
│           SQLite             │
│                              │
│ Users                        │
│ Events                       │
│ RSVPs                        │
└──────────────────────────────┘

⸻

🛠️ Technologies Used

Frontend

Technology	Purpose
HTML5	Structure of web pages
CSS3	Styling and responsive design
JavaScript	Client-side interaction
Responsive CSS	Mobile and desktop layouts

Backend

Technology	Purpose
Python	Backend programming language
FastAPI	Web framework and REST API
Uvicorn	ASGI server
Pydantic	Request/data validation
SQLAlchemy	Database ORM

Database

Technology	Purpose
SQLite	Local application database
SQLAlchemy	Communication between Python and SQLite

Development Tools

* Git
* GitHub
* Visual Studio Code / Codespaces
* Python virtual environment
* Browser developer tools

⸻

📂 Project Structure

The repository currently follows a structure similar to:

eventlink_CM2.0/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── test_backend.py
│
├── FastAPI_Documentation.md
│
├── add_qr.py
├── apply_futuristic.py
├── fix_reg.py
├── patch_date.py
├── refactor_pages.py
├── update_icons.py
│
├── generate_doc.py
├── generate_team_doc.py
├── generate_three_docs.py
├── generate_ultimate_doc.py
│
└── EventLink CM Project/
    │
    └── frontend/
        │
        ├── index.html
        ├── about.html
        ├── events.html
        ├── contact.html
        ├── login.html
        ├── register.html
        ├── create-event.html
        ├── dashboard.html
        ├── user-home.html
        ├── organized.html
        ├── analytics.html
        │
        ├── css/
        │   ├── home.css
        │   ├── about.css
        │   ├── auth.css
        │   ├── contact.css
        │   └── events.css
        │
        ├── js/
        │   ├── home.js
        │   ├── about.js
        │   ├── contact.js
        │   ├── events.js
        │   ├── login.js
        │   └── register.js
        │
        └── images/
            └── background.jpeg

⸻

🗄️ Database Design

The application currently uses SQLite through SQLAlchemy.

The main database tables are:

Users

Stores registered user information.

Users
-------------------------
email       PRIMARY KEY
name
password
gender

Events

Stores event information.

Events
-------------------------
id              PRIMARY KEY
name
category
location
date
icon
created_by

RSVPs

Stores participant registrations and attendance information.

RSVPs
-------------------------
id              PRIMARY KEY
event_id
user_email
scanned
time_arrived

Conceptually:

       ┌─────────────┐
       │    USER     │
       └──────┬──────┘
              │
              │ registers
              ▼
       ┌─────────────┐
       │    RSVP     │
       └──────┬──────┘
              │
              │ belongs to
              ▼
       ┌─────────────┐
       │    EVENT    │
       └─────────────┘

⸻

🔌 API Endpoints

The FastAPI backend provides endpoints for the main application operations.

Authentication

Register

POST /api/register

Registers a new user.

Login

POST /api/login

Authenticates an existing user.

⸻

Events

Get Events

GET /api/events

Returns the available events.

Create Event

POST /api/events

Creates a new event.

Event Analytics

GET /api/events/{event_id}/analytics

Returns attendance and participant analytics for an event.

⸻

RSVP

Register for an Event

POST /api/events/{event_id}/rsvp

Creates an RSVP for a participant.

Get User RSVPs

GET /api/users/{email}/rsvps

Returns events registered by a participant.

Get Organized Events

GET /api/users/{email}/organized

Returns events created by an organizer.

⸻

Attendance

Scan Ticket

POST /api/events/{event_id}/scan

Marks an RSVP as attended and records the arrival time.

⸻

🌐 Frontend Routes

The FastAPI application serves the frontend pages through routes such as:

Route	Page
/	Home
/about	About
/events	Events
/contact	Contact
/login	Login
/register	Registration
/create-event	Create Event
/dashboard	Dashboard
/user-home	Participant Home
/organized	Organized Events
/analytics	Event Analytics

⸻

⚙️ Installation

1. Clone the repository

git clone https://github.com/jordiembah5-gif/eventlink_CM2.0.git

Move into the project:

cd eventlink_CM2.0

⸻

2. Create a virtual environment

Windows

python -m venv venv

Activate it:

venv\Scripts\activate

macOS/Linux

python3 -m venv venv

Activate it:

source venv/bin/activate

⸻

3. Install dependencies

pip install -r requirements.txt

The current requirements include:

fastapi
uvicorn
sqlalchemy
pydantic

⸻

▶️ Running the Application

Start the FastAPI server using:

uvicorn main:app --reload

The application should then be available at:

http://127.0.0.1:8000

or:

http://localhost:8000

⸻

📚 API Documentation

FastAPI automatically provides interactive API documentation.

After starting the server, open:

http://127.0.0.1:8000/docs

The alternative documentation interface is available at:

http://127.0.0.1:8000/redoc

These interfaces can be used to inspect and test the API endpoints.

⸻

🧪 Testing

The repository contains a backend testing file:

test_backend.py

Backend functionality should be tested after starting the application.

The main areas to test include:

* User registration
* Duplicate registration prevention
* User login
* Invalid login
* Event retrieval
* Event creation
* Event RSVP
* Duplicate RSVP prevention
* User RSVP retrieval
* Organizer event retrieval
* Attendance scanning
* Duplicate attendance scanning
* Event analytics

⸻

🔄 Application Workflow

The general participant workflow is:

Open EventLink CM
       │
       ▼
Browse Events
       │
       ▼
Select Event
       │
       ▼
Login / Register
       │
       ▼
RSVP
       │
       ▼
Receive/Use Event Ticket
       │
       ▼
Attend Event
       │
       ▼
QR / Ticket Scan
       │
       ▼
Attendance Recorded

The organizer workflow is:

Login
  │
  ▼
Organizer Dashboard
  │
  ▼
Create Event
  │
  ▼
Publish Event
  │
  ▼
Participants RSVP
  │
  ▼
View Registrations
  │
  ▼
Scan Attendance
  │
  ▼
View Analytics

⸻

🔒 Security Considerations

EventLink CM is currently an academic/development project and should not be considered production-ready without additional security work.

Future security improvements should include:

* Password hashing.
* Secure authentication tokens/session management.
* Role-based access control.
* Input sanitization and validation.
* HTTPS in production.
* Environment variables for sensitive configuration.
* Protection against unauthorized event modification.
* Protection against unauthorized attendance scanning.
* Database constraints and stronger relationship management.
* Rate limiting for authentication endpoints.

Important: Sensitive credentials should never be committed to the repository.

⸻

🚧 Current Limitations

The current version is an evolving project. Some functionality may still require further integration and refinement.

Current limitations include:

* Authentication is still basic.
* Production-grade password security needs to be implemented.
* SQLite is currently used for local development.
* Some frontend pages are static or partially integrated.
* Payment functionality is not currently implemented.
* Email verification is not yet part of the current core implementation.
* Full production-grade authorization still needs to be added.
* QR attendance functionality requires further frontend integration for a complete scanning experience.

⸻

🔮 Future Improvements

Future versions of EventLink CM can include:

Authentication

* Email verification.
* Password reset.
* Secure password hashing.
* Role-based authentication.
* Organizer and participant profiles.

Event Management

* Event editing and deletion.
* Event images.
* Event capacity limits.
* Event status management.
* Event reminders.
* Event recommendations.

Tickets

* Unique digital tickets.
* QR-code generation.
* QR-code scanner interface.
* Downloadable tickets.
* Attendance history.

Payments

A future version could support local payment services such as:

* MTN Mobile Money.
* Orange Money.

Payment integration is intentionally outside the current core implementation.

Communication

* Email notifications.
* Event reminders.
* Organizer announcements.
* Participant notifications.

Analytics

* Attendance charts.
* Registration statistics.
* Event performance reports.
* Exportable reports.
* PDF attendance reports.

Localization

The platform can also be expanded to support both:

* English
* French

to make the system more accessible to users across Cameroon.

⸻

🧑‍💻 Development Methodology

The project follows an iterative software-development approach inspired by Agile/Scrum.

Development activities can be divided into:

1. Requirement analysis
2. System design
3. Database design
4. Backend development
5. Frontend development
6. API integration
7. Testing
8. Debugging
9. Documentation
10. Deployment

The team can use GitHub branches to allow different members to work on separate parts of the application before integrating their work.

⸻

🌿 Git Workflow

A recommended workflow is:

git checkout -b feature-name

Make changes, then:

git add .
git commit -m "Describe your changes"
git push origin feature-name

After testing, the feature branch can be merged into the main development branch.

⸻

👥 Team Collaboration

Team members can divide development responsibilities into areas such as:

Role	Responsibility
Project/Infrastructure Lead	Repository, environment and application configuration
Backend/API Developer	FastAPI endpoints and business logic
Frontend Developer	HTML, CSS and JavaScript interfaces
Database Developer	SQLAlchemy models and database structure
Testing/Documentation	Testing, bug tracking and project documentation

⸻

📖 Project Documentation

Additional technical documentation is available in:

FastAPI_Documentation.md

The repository also contains scripts used during different stages of development and documentation generation.

⸻

📌 Project Status

Status: 🚧 Active Development

EventLink CM currently provides the foundation for:

* User registration
* Login
* Event discovery
* Event creation
* RSVP management
* Attendance tracking
* Event analytics
* Frontend/backend integration

Further development is required before the system should be considered a fully production-ready event-management platform.

⸻

📜 License

This project was developed as an academic/project-based software application.

Unless a separate license is added to the repository, the project should not be assumed to grant permission for unrestricted commercial redistribution or reuse.

⸻

👨‍💻 Repository

GitHub Repository:

https://github.com/jordiembah5-gif/eventlink_CM2.0

⸻

❤️ About EventLink CM

EventLink CM is built around a simple idea:

Make it easier for people to discover events, participate in them, and connect with their community.

EventLink CM — Connect • Discover • Experience 🇨🇲
