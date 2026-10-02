// ==============================================================================
// CHAPTER 5: JAVASCRIPT - THE ELECTRICITY (register.js)
// ==============================================================================
// Welcome to JavaScript (JS)! If HTML is the structure of a house, and CSS is
// the paint, then JavaScript is the electricity and plumbing. It makes the page 
// INTERACTIVE. It responds to clicks, typing, and talks to the server.
// ==============================================================================

// ------------------------------------------------------------------------------
// 1. ASYNC FUNCTIONS (The Mini-Machines)
// ------------------------------------------------------------------------------
// A "function" is a reusable block of code that performs a specific action.
// The word "async" (asynchronous) means this function talks to the internet. 
// Because the internet can be slow, "async" tells the browser: "Start this job, 
// but don't freeze the rest of the website while you wait for a reply!"
async function registerUser(event) {
    
    // When a user submits a form, the browser naturally tries to refresh the page.
    // We use "preventDefault()" to STOP the page from refreshing so we can handle it silently.
    event.preventDefault();

    // --------------------------------------------------------------------------
    // 2. VARIABLES AND THE DOM
    // --------------------------------------------------------------------------
    // "const" creates a variable. Think of a variable as a labeled box where we store data.
    // The "DOM" (Document Object Model) is how JavaScript reads the HTML page.
    // "document.getElementById('name').value" tells JS: 
    // "Look at the webpage, find the box with the ID 'name', and grab whatever the user typed inside it."
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;
    const gender = document.getElementById("gender").value;
    
    // Here we grab the invisible message text area on the screen so we can write to it later.
    const message = document.getElementById("message");

    // --------------------------------------------------------------------------
    // 3. CONDITIONAL LOGIC (If / Else Statements)
    // --------------------------------------------------------------------------
    // An "If" statement is how the computer makes decisions. 
    // "!=" means "is NOT equal to". 
    // So this reads: "IF the password is NOT equal to the confirm password, do this:"
    if (password !== confirmPassword) {
        // Change the text on the screen to show an error, then STOP the function (return).
        message.textContent = "Passwords do not match.";
        return;
    }

    // "try / catch" is a safety net. It means: "Try to do this code, but if the internet crashes, 
    // CATCH the error so the whole website doesn't break."
    try {
        // ----------------------------------------------------------------------
        // 4. THE FETCH API (Talking to the Backend)
        // ----------------------------------------------------------------------
        // "fetch" is how JavaScript sends a message over the internet to our Python Backend (main.py).
        // "await" means "pause this specific function until the backend replies".
        const response = await fetch('/api/register', {
            method: 'POST', // POST means we are sending hidden, secure data (like a password).
            headers: { 'Content-Type': 'application/json' },
            // JSON (JavaScript Object Notation) is the universal language of the internet. 
            // We package our variables into a JSON box to send to Python.
            body: JSON.stringify({ name, email, password, gender })
        });
        
        // We receive the reply from Python and unpack the JSON box.
        const data = await response.json();
        
        // If the server replied with an "ok" status (code 200)...
        if (response.ok) {
            message.textContent = "Registration successful! Logging you in...";
            
            // ------------------------------------------------------------------
            // 5. LOCAL STORAGE (The Browser's Memory)
            // ------------------------------------------------------------------
            // "localStorage" is a small memory bank inside your web browser (Chrome/Safari).
            // We save their email here so the browser remembers they are logged in even if they close the tab.
            localStorage.setItem("currentUser", email);
            
            // Automatically process any pending RSVPs (if they clicked 'Join Event' before registering)
            const pendingRSVP = localStorage.getItem("pendingRSVP");
            if (pendingRSVP) {
                try {
                    await fetch(`/api/events/${pendingRSVP}/rsvp`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ email: email })
                    });
                    localStorage.removeItem("pendingRSVP"); // Clean up the memory bank
                } catch (e) {
                    console.error("Failed to process pending RSVP", e);
                }
            }

            // "setTimeout" creates a countdown timer. 
            // Wait 1000 milliseconds (1 second), then move them to their dashboard!
            setTimeout(function() {
                const redirect = localStorage.getItem("redirectAfterLogin");
                if (redirect) {
                    localStorage.removeItem("redirectAfterLogin");
                    window.location.href = redirect; // Move to their intended page
                } else {
                    window.location.href = "/user-home"; // Move to the default dashboard
                }
            }, 1000);
            
        } else {
            // If the server rejected the registration (e.g. email already exists), show the error.
            message.textContent = data.detail || "Registration failed.";
        }
    } catch (error) {
        // If the catch block triggers, it means the server is offline or internet disconnected.
        message.textContent = "An error occurred connecting to the server.";
    }
}