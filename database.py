# ==============================================================================
# CHAPTER 1: THE DATABASE CONNECTION (database.py)
# ==============================================================================
# Welcome! This file is responsible for connecting our web application to the database.
# Think of the database as a highly organized filing cabinet where all our data 
# (users, events, tickets) is permanently stored so it isn't lost when the server turns off.

# We are importing specific tools from a library called 'sqlalchemy'.
# A "library" is a collection of pre-written code that we can borrow so we don't have to reinvent the wheel.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ------------------------------------------------------------------------------
# 1. DATABASE URL
# ------------------------------------------------------------------------------
# Here we define WHERE our filing cabinet is located. 
# "sqlite:///" tells the system we are using SQLite (a simple, lightweight database).
# "./eventlink.db" means "create a file named eventlink.db in this exact folder".
SQLALCHEMY_DATABASE_URL = "sqlite:///./eventlink.db"

# ------------------------------------------------------------------------------
# 2. THE ENGINE
# ------------------------------------------------------------------------------
# The "engine" is the actual machine that talks to our database file. 
# We give it the URL (the address of the filing cabinet) so it knows where to go.
# We also pass a special rule (check_same_thread=False) which is just a technical requirement for SQLite.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# ------------------------------------------------------------------------------
# 3. THE SESSION
# ------------------------------------------------------------------------------
# Imagine the Engine is a massive pipe connecting to the database. 
# A "Session" is a single conversation happening inside that pipe. 
# Whenever a user wants to log in or register, we open a temporary Session, do our work, and close it.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ------------------------------------------------------------------------------
# 4. THE BASE BLUEPRINT
# ------------------------------------------------------------------------------
# 'declarative_base()' creates a foundational blueprint.
# All of our future database tables (like Users, Events) will inherit properties from this Base.
Base = declarative_base()

# ------------------------------------------------------------------------------
# 5. GETTING A DATABASE CONNECTION
# ------------------------------------------------------------------------------
# This is a "function". A function is a mini-machine that performs a specific task.
# When called, this function opens a session (a conversation) with the database,
# "yields" (hands it over) to the part of the code that needs it, and finally closes it.
def get_db():
    db = SessionLocal() # Open the conversation
    try:
        yield db        # Hand over the connection to the code that requested it
    finally:
        db.close()      # Always close the connection when finished so we don't waste memory!
