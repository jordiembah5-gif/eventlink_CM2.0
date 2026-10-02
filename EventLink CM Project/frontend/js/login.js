async function loginUser(event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const message = document.getElementById("message");

    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            message.textContent = "Login successful!";
            localStorage.setItem("currentUser", email);
            
            // Automatically process any pending RSVPs
            const pendingRSVP = localStorage.getItem("pendingRSVP");
            if (pendingRSVP) {
                try {
                    await fetch(`/api/events/${pendingRSVP}/rsvp`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ email: email })
                    });
                    localStorage.removeItem("pendingRSVP");
                } catch (e) {
                    console.error("Failed to process pending RSVP", e);
                }
            }

            setTimeout(function() {
                const redirect = localStorage.getItem("redirectAfterLogin");
                if (redirect) {
                    localStorage.removeItem("redirectAfterLogin");
                    window.location.href = redirect;
                } else {
                    window.location.href = "/user-home";
                }
            }, 1000);
        } else {
            message.textContent = data.detail || "Invalid email or password.";
        }
    } catch (error) {
        message.textContent = "An error occurred connecting to the server.";
    }
}