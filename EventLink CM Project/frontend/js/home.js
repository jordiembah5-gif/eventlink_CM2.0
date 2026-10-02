// ==============================================================================
// CHAPTER 8: JAVASCRIPT - THE LOGIC & INTERACTIVITY (home.js)
// ==============================================================================
// This file handles the logic for the Home Page. 
// It contains "Functions" which are blocks of code that perform specific tasks.
// ==============================================================================

// ------------------------------------------------------------------------------
// 1. EVENT LISTENERS (Waiting for things to happen)
// ------------------------------------------------------------------------------
// "addEventListener" tells the browser to listen for a specific event.
// "DOMContentLoaded" means "Wait until the HTML is fully loaded on the screen".
document.addEventListener("DOMContentLoaded", () => {
    
    // --- SMART ROUTING LOGIC ---
    // If the browser memory (localStorage) already knows the user is logged in,
    // we don't want them to see the public landing page! 
    // We immediately teleport them to their private dashboard.
    if (localStorage.getItem("currentUser")) {
        window.location.href = "/user-home"; // Changes the URL instantly
    }
});

// ------------------------------------------------------------------------------
// 2. TOGGLING UI (The Mobile Menu)
// ------------------------------------------------------------------------------
// This function is attached to the Hamburger Menu button (~) on mobile screens.
function toggleMenu() {
    // We ask the DOM (the webpage) to find the HTML element with the ID "navMenu"
    const menu = document.getElementById("navMenu");
    
    // Conditional Logic (If / Else):
    // "If the menu is currently visible (flex), hide it (none)."
    if (menu.style.display === "flex") {
        menu.style.display = "none";
    } else {
        // "Else (if it is hidden), show it!"
        menu.style.display = "flex";
        
        // We inject CSS styling directly using Javascript to make it look like a dropdown
        menu.style.flexDirection = "column";
        menu.style.position = "absolute";
        menu.style.top = "75px";
        menu.style.right = "5%";
        menu.style.background = "#fff";
        menu.style.padding = "15px";
        menu.style.border = "1px solid #ddd";
    }
}

// ------------------------------------------------------------------------------
// 3. SEARCH LOGIC
// ------------------------------------------------------------------------------
function searchFromHome() {
    // Grab whatever the user typed into the search box
    const query = document.getElementById('homeSearch').value;
    
    if (query) {
        // If they typed something, send them to the events page and attach their query to the URL!
        // "encodeURIComponent" makes sure special characters (like spaces) don't break the web link.
        window.location.href = '/events?search=' + encodeURIComponent(query);
    } else {
        // If the box was empty, just send them to the normal events page.
        window.location.href = '/events';
    }
}

// ------------------------------------------------------------------------------
// 4. ACTION INTENT LOGIC (Smart Redirects)
// ------------------------------------------------------------------------------
// This runs when they click the "Host an Event" button on the homepage.
function goToCreateEvent() {
    // The "!" means NOT. So: "If there is NOT a currentUser in memory..."
    if (!localStorage.getItem("currentUser")) {
        // They are not logged in! 
        // 1. Save their intention to memory (so we remember where they wanted to go)
        localStorage.setItem("redirectAfterLogin", "/create-event");
        // 2. Send them to the register page first.
        window.location.href = "/register";
    } else {
        // If they ARE logged in, simply let them go to the create event page.
        window.location.href = "/create-event";
    }
}