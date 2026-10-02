// Mobile Menu Toggle
function toggleMenu() {
    const menu = document.getElementById("navMenu");
    if (menu.style.display === "flex") {
        menu.style.display = "none";
    } else {
        menu.style.display = "flex";
        menu.style.flexDirection = "column";
        menu.style.position = "absolute";
        menu.style.top = "75px";
        menu.style.right = "5%";
        menu.style.background = "#10003c";
        menu.style.padding = "15px";
    }
}

// Load Events from FastAPI Backend
document.addEventListener("DOMContentLoaded", async () => {
    try {
        const response = await fetch('/api/events');
        const data = await response.json();
        const grid = document.getElementById("eventGrid");
        
        grid.innerHTML = ""; // Clear loading message
        
        data.events.forEach(event => {
            const article = document.createElement("article");
            article.className = "event-card";
            article.dataset.category = event.category;
            
            article.innerHTML = `
                <div class="event-icon">
                    <img src="${event.icon}" alt="Event Image">
                </div>
                <h2>${event.name}</h2>
                <p><i class="fas fa-map-marker-alt"></i> ${event.location}</p>
                <a href="https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(event.location)}" target="_blank" style="color: #0071E3; font-size: 14px; text-decoration: none; display: inline-block; margin-bottom: 10px;"><i class="fas fa-directions"></i> View on Google Maps</a>
                <p><i class="fas fa-calendar-alt"></i> ${event.date}</p>
                <button class="primary-btn" onclick="joinEvent('${event.name}', '${event.id}')" style="width: 100%; margin-top: 10px;">Join Event</button>
            `;
            
            grid.appendChild(article);
        });

        // Automatically filter if there's a search query in the URL
        const params = new URLSearchParams(window.location.search);
        if (params.has('search')) {
            document.getElementById('searchInput').value = params.get('search');
            filterEvents();
        }
    } catch (error) {
        console.error("Error loading events:", error);
        document.getElementById("eventGrid").innerHTML = "<p>Failed to load events. Is the backend running?</p>";
    }
});

// Search and Filter Events
function filterEvents() {
    const search = document.getElementById("searchInput").value.toLowerCase();
    const category = document.getElementById("categoryFilter").value;
    const events = document.querySelectorAll(".event-card");

    events.forEach(function(event) {
        const text = event.innerText.toLowerCase();
        const eventCategory = event.dataset.category;

        const matchesSearch = text.includes(search);
        const matchesCategory = category === "all" || eventCategory === category;

        if (matchesSearch && matchesCategory) {
            event.style.display = "block";
        } else {
            event.style.display = "none";
        }
    });
}

// Join Event and Show QR Code
async function joinEvent(eventName, eventId) {
    const currentUserEmail = localStorage.getItem("currentUser");

    if (!currentUserEmail) {
        localStorage.setItem("pendingRSVP", eventId);
        localStorage.setItem("redirectAfterLogin", "/dashboard");
        window.location.href = "/register";
        return;
    }

    try {
        const response = await fetch(`/api/events/${eventId}/rsvp`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: currentUserEmail })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            // Registration successful, show QR Code Modal
            document.getElementById("qrMessage").textContent = `You're successfully registered for ${eventName}!`;
            
            // Generate QR Code containing the event ID and User email
            const qrData = encodeURIComponent(`Event: ${eventName} | User: ${currentUserEmail}`);
            document.getElementById("qrImage").src = `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=${qrData}`;
            
            // Display the modal
            document.getElementById("qrModal").style.display = "flex";
        } else {
            alert(data.detail || "Failed to RSVP.");
        }
    } catch (error) {
        alert("An error occurred connecting to the server.");
    }
}

// Close QR Modal
function closeModal() {
    document.getElementById("qrModal").style.display = "none";
}