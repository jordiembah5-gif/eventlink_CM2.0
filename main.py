import uuid
# ==============================================================================
# CHAPTER 4: THE MAIN APPLICATION (main.py)
# ==============================================================================
# Welcome! This is the brain of our website. It ties everything together.
# It listens for internet traffic, talks to the database, and sends web pages back.

import os
from datetime import datetime
from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

# Here, we IMPORT the files we separated earlier to keep our code clean!
from database import engine, get_db, Base, SessionLocal
from models import DBUser, DBEvent, DBRSVP
from schemas import UserRegister, UserLogin, EventCreate, RSVP

# 1. CREATE THE DATABASE TABLES
# This line tells our database engine to look at our blueprints (models.py) and build the actual tables.
Base.metadata.create_all(bind=engine)

# 2. DEFAULT DATA (Pre-populating events)
# This FUNCTION is called when the server starts. 
# A "function" is a reusable block of code that does a specific job.
def init_db():
    db = SessionLocal()
    # "if" statement: If the database is completely empty (0 events)...
    if db.query(DBEvent).count() == 0:
        # Create a list (collection) of default events
        default_events = [
            {"id": "yaounde-music-night", "name": "Yaoundé Music Night", "category": "music", "location": "Yaoundé", "date": "20 September 2026", "icon": "images/futuristic_music.jpg", "created_by": "admin@eventlink.cm"},
            {"id": "cameroon-business-forum", "name": "Cameroon Business Forum", "category": "business", "location": "Douala", "date": "25 September 2026", "icon": "images/futuristic_business.jpg", "created_by": "admin@eventlink.cm"}
        ]
        
        # --- WHAT IS A LOOP? ---
        # A "for loop" tells the computer to repeat an action. 
        # Here we say: "For every single event (ev) in our list, add it to the database."
        # This saves us from writing the same code 100 times!
        for ev in default_events:
            db_event = DBEvent(**ev)
            db.add(db_event)
        
        db.commit() # Save the changes to the database
    db.close()

init_db() # We call the function to actually run it

# 3. START THE APP
# We create our FastAPI application. Think of this as the main web server.
app = FastAPI()

# ==============================================================================
# 4. API ROUTES (The Communication Channels)
# ==============================================================================
# An API (Application Programming Interface) is how the frontend (website) talks to the backend (database).
# "@app.post" is a decorator. It creates a specific internet URL. 
# POST means the user is SENDING us secret data (like a password).
# GET means the user is ASKING for data (like reading a list of events).

@app.post("/api/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    # 1. Check if the email already exists
    existing = db.query(DBUser).filter(DBUser.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email is already registered.")
    
    # 2. Create the new user object and save it
    new_user = DBUser(email=user.email, name=user.name, password=user.password, gender=user.gender)
    db.add(new_user)
    db.commit()
    return {"message": "Registration successful"}

@app.post("/api/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    existing = db.query(DBUser).filter(DBUser.email == user.email).first()
    if not existing or existing.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid email or password.")
    return {"message": "Login successful", "name": existing.name}

@app.get("/api/events")
def get_events(db: Session = Depends(get_db)):
    # Ask the database for ALL events
    events = db.query(DBEvent).all()
    # We use a loop inside a list (list comprehension) to quickly package them up and send them back
    return {"events": [{"id": e.id, "name": e.name, "category": e.category, "location": e.location, "date": e.date, "icon": e.icon, "created_by": e.created_by} for e in events]}

@app.post("/api/events")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    # Create a base ID from the name
    base_id = event.name.lower().replace(" ", "-")
    # Append a short unique string to guarantee uniqueness
    event_id = f"{base_id}-{uuid.uuid4().hex[:6]}"
    
    new_event = DBEvent(
        id=event_id, name=event.name, category=event.category,
        location=event.location, date=event.date, icon=event.icon, created_by=event.created_by
    )
    db.add(new_event)
    db.commit()
    return {"message": "Event created successfully", "event": {"id": event_id, "name": event.name}}

@app.post("/api/events/{event_id}/rsvp")
def rsvp_event(event_id: str, rsvp: RSVP, db: Session = Depends(get_db)):
    existing_rsvp = db.query(DBRSVP).filter(DBRSVP.event_id == event_id, DBRSVP.user_email == rsvp.email).first()
    if existing_rsvp:
        raise HTTPException(status_code=400, detail="You already registered for this event.")
    
    new_rsvp = DBRSVP(event_id=event_id, user_email=rsvp.email)
    db.add(new_rsvp)
    db.commit()
    return {"message": f"Successfully RSVP'd to event"}

@app.get("/api/users/{email}/rsvps")
def get_user_rsvps(email: str, db: Session = Depends(get_db)):
    rsvps = db.query(DBRSVP).filter(DBRSVP.user_email == email).all()
    event_ids = [r.event_id for r in rsvps]
    events = db.query(DBEvent).filter(DBEvent.id.in_(event_ids)).all()
    
    results = []
    # Loop through every event they RSVP'd to, and check if their ticket was scanned yet
    for e in events:
        rsvp_details = next((r for r in rsvps if r.event_id == e.id), None)
        results.append({
            "id": e.id, "name": e.name, "category": e.category, "location": e.location, "date": e.date, "icon": e.icon,
            "scanned": rsvp_details.scanned if rsvp_details else False
        })
    return {"events": results}

@app.get("/api/users/{email}/organized")
def get_organized_events(email: str, db: Session = Depends(get_db)):
    events = db.query(DBEvent).filter(DBEvent.created_by == email).all()
    results = []
    # Loop to calculate how many people RSVP'd to each of the organizer's events
    for e in events:
        rsvp_count = db.query(DBRSVP).filter(DBRSVP.event_id == e.id).count()
        results.append({
            "id": e.id, "name": e.name, "category": e.category, "location": e.location, "date": e.date, "icon": e.icon, "rsvp_count": rsvp_count
        })
    return {"events": results}

@app.get("/api/events/{event_id}/analytics")
def get_event_analytics(event_id: str, db: Session = Depends(get_db)):
    rsvps = db.query(DBRSVP).filter(DBRSVP.event_id == event_id).all()
    
    attendees = []
    males, females, other, arrived = 0, 0, 0, 0
    
    # Loop to build our analytics statistics!
    for r in rsvps:
        user = db.query(DBUser).filter(DBUser.email == r.user_email).first()
        if user:
            gender = (user.gender or "Unknown").lower()
            if gender == "male": males += 1
            elif gender == "female": females += 1
            else: other += 1
            
            if r.scanned: arrived += 1
            
            attendees.append({
                "email": user.email, "name": user.name, "gender": user.gender,
                "scanned": r.scanned, "time_arrived": r.time_arrived
            })
            
    return {
        "total_rsvps": len(rsvps),
        "total_arrived": arrived,
        "gender_breakdown": {"male": males, "female": females, "other": other},
        "attendees": attendees
    }

@app.post("/api/events/{event_id}/scan")
def scan_qr(event_id: str, payload: RSVP, db: Session = Depends(get_db)):
    rsvp = db.query(DBRSVP).filter(DBRSVP.event_id == event_id, DBRSVP.user_email == payload.email).first()
    if rsvp.scanned:
        return {"message": "Ticket already scanned!", "already_scanned": True}
    
    rsvp.scanned = True
    rsvp.time_arrived = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.commit()
    return {"message": "Ticket successfully scanned!", "time_arrived": rsvp.time_arrived}

# ==============================================================================
# 5. FRONTEND ROUTING (Serving Web Pages)
# ==============================================================================
# This section tells the server: "If someone types /about in their browser, send them the about.html file."
frontend_path = os.path.join(os.path.dirname(__file__), "EventLink CM Project", "frontend")

@app.get("/")
def get_home(): return FileResponse(os.path.join(frontend_path, "index.html"))

@app.get("/about")
def get_about(): return FileResponse(os.path.join(frontend_path, "about.html"))

@app.get("/events")
def get_events_page(): return FileResponse(os.path.join(frontend_path, "events.html"))

@app.get("/contact")
def get_contact(): return FileResponse(os.path.join(frontend_path, "contact.html"))

@app.get("/login")
def get_login(): return FileResponse(os.path.join(frontend_path, "login.html"))

@app.get("/register")
def get_register(): return FileResponse(os.path.join(frontend_path, "register.html"))

@app.get("/create-event")
def get_create_event(): return FileResponse(os.path.join(frontend_path, "create-event.html"))

@app.get("/dashboard")
def get_dashboard(): return FileResponse(os.path.join(frontend_path, "dashboard.html"))

@app.get("/user-home")
def get_user_home(): return FileResponse(os.path.join(frontend_path, "user-home.html"))

@app.get("/organized")
def get_organized(): return FileResponse(os.path.join(frontend_path, "organized.html"))

@app.get("/analytics")
def get_analytics(): return FileResponse(os.path.join(frontend_path, "analytics.html"))

# This allows the HTML files to load CSS styles, Javascript, and Images!
app.mount("/css", StaticFiles(directory=os.path.join(frontend_path, "css")), name="css")
app.mount("/js", StaticFiles(directory=os.path.join(frontend_path, "js")), name="js")
app.mount("/images", StaticFiles(directory=os.path.join(frontend_path, "images")), name="images")
import os
from fastapi.staticfiles import StaticFiles

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount(
    "/",
    StaticFiles(
        directory=os.path.join(BASE_DIR, "EventLink CM Project", "frontend"),
        html=True,
    ),
    name="frontend",
)