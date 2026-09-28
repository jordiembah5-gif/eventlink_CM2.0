# ==============================================================================
# CHAPTER 3: SCHEMAS & DATA VALIDATION (schemas.py)
# ==============================================================================
# Welcome! This file handles DATA VALIDATION.
# 
# Wait, didn't we just define our data in models.py? What's the difference?
# - models.py defines how data is permanently STORED in the database.
# - schemas.py defines how data is RECEIVED from the internet (from the user).
#
# Think of a Schema as a bouncer at a club. If a user tries to register, the 
# Schema (bouncer) checks if they provided a name, email, password, and gender.
# If they forgot their email, the Schema instantly blocks them and throws an error.
# ==============================================================================

# We use a tool called Pydantic for validation. BaseModel is the master blueprint for validation.
from pydantic import BaseModel

# ------------------------------------------------------------------------------
# 1. REGISTRATION SCHEMA
# ------------------------------------------------------------------------------
# When a user signs up, we EXPECT them to send us this exact information.
class UserRegister(BaseModel):
    name: str       # "str" means String (text). It must be text!
    email: str
    password: str
    gender: str

# ------------------------------------------------------------------------------
# 2. LOGIN SCHEMA
# ------------------------------------------------------------------------------
# When logging in, we don't need their gender or name, ONLY their email and password.
class UserLogin(BaseModel):
    email: str
    password: str

# ------------------------------------------------------------------------------
# 3. EVENT CREATION SCHEMA
# ------------------------------------------------------------------------------
# When an organizer creates a new event, they must provide these details.
class EventCreate(BaseModel):
    name: str
    category: str
    location: str
    date: str
    icon: str
    created_by: str

# ------------------------------------------------------------------------------
# 4. RSVP (JOIN EVENT) SCHEMA
# ------------------------------------------------------------------------------
# To join an event, we just need to know the email of the person joining.
class RSVP(BaseModel):
    email: str
