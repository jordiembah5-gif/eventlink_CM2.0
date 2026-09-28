# ==============================================================================
# CHAPTER 2: DATABASE MODELS (models.py)
# ==============================================================================
# Welcome! This file defines HOW our data is structured inside the database.
#
# --- WHAT IS OBJECT-ORIENTED PROGRAMMING (OOP)? ---
# In programming, we use OOP to represent real-world concepts in code.
# 1. A "Class" is a BLUEPRINT. Think of a class like an architect's blueprint for a house.
# 2. An "Object" is the actual HOUSE built from that blueprint.
# 3. "Attributes" are the properties of the house (e.g., color, number of doors).
# 4. "Inheritance" means a blueprint can borrow rules from a master blueprint.
# ==============================================================================

# We import the tools needed to define our data types (Strings for text, Integers for numbers).
from sqlalchemy import Column, String, Integer, Boolean
# We import the master blueprint (Base) we created in database.py
from database import Base

# ------------------------------------------------------------------------------
# THE USER BLUEPRINT (Class)
# ------------------------------------------------------------------------------
# Here we define the "DBUser" class. 
# Notice the "(Base)" in parenthesis? That is INHERITANCE. 
# It tells Python: "DBUser is a database table that borrows all the rules from Base."
class DBUser(Base):
    # __tablename__ tells the database exactly what to name the folder holding these records.
    __tablename__ = "users"
    
    # These are ATTRIBUTES. Every time a new User Object is created, it must have these traits:
    # "primary_key=True" means this is the unique identifier for the user (like an ID card number).
    # Two users cannot have the same email.
    email = Column(String, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
    gender = Column(String)

# ------------------------------------------------------------------------------
# THE EVENT BLUEPRINT (Class)
# ------------------------------------------------------------------------------
class DBEvent(Base):
    __tablename__ = "events"
    
    id = Column(String, primary_key=True, index=True) # Unique ID like "tech-meetup-2026"
    name = Column(String)                             # Name of the event
    category = Column(String)                         # e.g., "music", "business"
    location = Column(String)                         # Where it happens
    date = Column(String)                             # When it happens
    icon = Column(String)                             # The image path for the event
    created_by = Column(String, index=True)           # The email of the person who hosts it

# ------------------------------------------------------------------------------
# THE RSVP (TICKET) BLUEPRINT (Class)
# ------------------------------------------------------------------------------
class DBRSVP(Base):
    __tablename__ = "rsvps"
    
    # autoincrement=True means the database will automatically count up (Ticket 1, Ticket 2, etc.)
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # We store WHICH event they are attending, and WHO is attending.
    event_id = Column(String, index=True)
    user_email = Column(String, index=True)
    
    # Boolean means True or False. By default, when a ticket is created, it has NOT been scanned.
    scanned = Column(Boolean, default=False)
    
    # We record the exact time they arrive. It's nullable=True because they haven't arrived yet!
    time_arrived = Column(String, nullable=True)
