import requests
import sys

BASE_URL = "http://localhost:8000"

def run_tests():
    print("--- Starting Automated Tests ---")
    
    # Test 1: Load Frontend HTML
    r = requests.get(f"{BASE_URL}/events.html")
    if r.status_code == 200:
        print("[OK] Frontend events.html loaded")
    else:
        print("[FAIL] Failed to load events.html")
        sys.exit(1)

    # Test 2: Register User
    print("\n--- Testing Authentication ---")
    user_data = {"name": "Test User", "email": "test@example.com", "password": "password123"}
    r = requests.post(f"{BASE_URL}/api/register", json=user_data)
    if r.status_code == 200:
        print("[OK] User registration successful")
    elif r.status_code == 400 and "already registered" in r.text:
        print("[OK] User registration (already exists, handled correctly)")
    else:
        print(f"[FAIL] User registration failed: {r.text}")
        sys.exit(1)

    # Test 3: Login User
    login_data = {"email": "test@example.com", "password": "password123"}
    r = requests.post(f"{BASE_URL}/api/login", json=login_data)
    if r.status_code == 200:
        print("[OK] User login successful")
    else:
        print(f"[FAIL] User login failed: {r.text}")
        sys.exit(1)

    # Test 4: Create Event
    print("\n--- Testing Event Creation ---")
    event_data = {
        "name": "Automated Test Event",
        "category": "technology",
        "location": "Virtual",
        "date": "1 January 2030",
        "icon": "fa-laptop"
    }
    r = requests.post(f"{BASE_URL}/api/events", json=event_data)
    if r.status_code == 200:
        print("[OK] Event created successfully")
    else:
        print(f"[FAIL] Event creation failed: {r.text}")
        sys.exit(1)

    # Test 5: Get Events
    r = requests.get(f"{BASE_URL}/api/events")
    if r.status_code == 200:
        events = r.json().get("events", [])
        if any(e["name"] == "Automated Test Event" for e in events):
            print("[OK] Created event successfully appears in events list")
        else:
            print("[FAIL] Created event missing from list")
            sys.exit(1)
    else:
        print(f"[FAIL] Failed to fetch events: {r.text}")
        sys.exit(1)

    # Test 6: RSVP to Event
    print("\n--- Testing RSVP System ---")
    rsvp_data = {"email": "test@example.com"}
    r = requests.post(f"{BASE_URL}/api/events/automated-test-event/rsvp", json=rsvp_data)
    if r.status_code == 200:
        print("[OK] RSVP successful")
    else:
        print(f"[FAIL] RSVP failed: {r.text}")
        sys.exit(1)

    print("\n[OK] ALL TESTS PASSED. NO BUGS DETECTED IN BACKEND LOGIC.")

if __name__ == "__main__":
    run_tests()
