// ==============================================================================
// CHAPTER 6: JAVASCRIPT - CREATING EVENTS (create-event.js)
// ==============================================================================
// This file controls the logic when a user fills out the "Host an Event" form.
// It handles advanced features like dynamic dates, stopping unauthenticated users,
// and sending data securely to the Python backend.
// ==============================================================================

// ------------------------------------------------------------------------------
// 1. DYNAMIC DATES (Preventing Time Travel)
// ------------------------------------------------------------------------------
// 'DOMContentLoaded' triggers exactly when the page finishes loading.
document.addEventListener('DOMContentLoaded', () => {
    
    // We grab the Date Calendar input box from the HTML page.
    const dateInput = document.getElementById('eventDate');
    
    if (dateInput) {
        // We create a "Date Object" which asks the computer for the exact current time.
        const now = new Date();
        
        // Timezones are tricky! We subtract the timezone offset to ensure the browser
        // gets the exact local time in Cameroon, rather than Greenwich Mean Time (GMT).
        now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
        
        // We slice the long string (e.g., "2026-11-15T15:30:00.000Z") to just the date and time ("2026-11-15T15:30")
        const minDateTime = now.toISOString().slice(0, 16);
        
        // We set the "min" attribute on the calendar. 
        // This physically blocks the user from clicking ANY date before this exact moment!
        dateInput.min = minDateTime;
    }
});

// ------------------------------------------------------------------------------
// 2. MOBILE MENU LOGIC
// ------------------------------------------------------------------------------
function toggleMenu() {
    const menu = document.getElementById("navMenu");
    // If the menu is showing, hide it. Otherwise, show it.
    if (menu.style.display === "flex") {
        menu.style.display = "none";
    } else {
        menu.style.display = "flex";
        menu.style.flexDirection = "column";
        menu.style.position = "absolute";
        menu.style.top = "75px";
        menu.style.right = "5%";
        menu.style.background = "#ffffff";
        menu.style.padding = "15px";
    }
}

// ------------------------------------------------------------------------------
// 3. GOOGLE MAPS AUTOCOMPLETE
// ------------------------------------------------------------------------------
// This connects our location box to Google Maps so it auto-fills city names!
function initMap() {
    const locationInput = document.getElementById('eventLocation');
    if (typeof google !== 'undefined') {
        const autocomplete = new google.maps.places.Autocomplete(locationInput);
    }
}

// ------------------------------------------------------------------------------
// 4. THE SUBMIT FUNCTION (Sending data to the Backend)
// ------------------------------------------------------------------------------
async function submitEvent(event) {
    // STOP the browser from refreshing the page automatically!
    event.preventDefault();

    // Check the browser's memory (localStorage) to see if they are logged in.
    const currentUserEmail = localStorage.getItem("currentUser");
    if (!currentUserEmail) {
        // If they are NOT logged in, save their intent and kick them to the register page.
        localStorage.setItem("redirectAfterLogin", "/create-event");
        window.location.href = "/register";
        return; // Stop the function here.
    }

    // Grab all the values the user typed into the HTML form boxes.
    const name = document.getElementById("eventName").value;
    const category = document.getElementById("eventCategory").value;
    const location = document.getElementById("eventLocation").value;
    
    // The calendar outputs dates with a "T" in the middle (e.g. 2026-10-15T10:00).
    // We use .replace() to swap the "T" with a normal space so it looks beautiful on the frontend.
    const date = document.getElementById("eventDate").value.replace("T", " ");
    const message = document.getElementById("message");

    // We use a "Dictionary" (Object) to automatically assign a cool default image
    // based on the category they selected from the dropdown menu!
    const icons = {
        "music": "images/futuristic_music.jpg",
        "business": "images/futuristic_business.jpg",
        "technology": "images/futuristic_tech.jpg",
        "education": "images/futuristic_tech.jpg"
    };
    // "||" means OR. If the category doesn't match, give them the tech image as a backup.
    const icon = icons[category] || "images/futuristic_tech.jpg";

    try {
        // We use the Fetch API to send our newly packaged event over the internet to the Python server.
        const response = await fetch('/api/events', {
            method: 'POST', // POST means we are sending NEW data to be created in the database
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, category, location, date, icon, created_by: currentUserEmail })
        });

        // We unpack the server's reply.
        const data = await response.json();

        // If the server says "200 OK", the event was saved to the database successfully!
        if (response.ok) {
            message.textContent = "Event created successfully!";
            message.style.color = "green";
            
            // Wait 1 second, then teleport them to the main events page to see their new event.
            setTimeout(() => {
                window.location.href = "events.html";
            }, 1000);
        } else {
            // If the server rejected it, show the error in red text.
            message.textContent = data.detail || "Failed to create event.";
            message.style.color = "red";
        }
    } catch (error) {
        // If the internet is disconnected, catch the crash and warn them.
        message.textContent = "An error occurred connecting to the server.";
        message.style.color = "red";
    }
}
