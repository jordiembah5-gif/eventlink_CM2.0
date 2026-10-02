# EventLink CM Project - FastAPI Migration Documentation

This document explains the steps taken to migrate the project's backend from a placeholder Django configuration to a functional, modern **FastAPI** backend, and how the frontend JavaScript was updated to interface with this backend.

## 1. Project Dependencies

**File Created:** `requirements.txt`

The `requirements.txt` file is the standard way to declare Python dependencies. We added three key libraries:
*   `fastapi==0.104.1`: The core web framework. It is modern, incredibly fast, and very easy to use for creating API endpoints.
*   `uvicorn==0.24.0`: An ASGI (Asynchronous Server Gateway Interface) web server. FastAPI is the framework, but Uvicorn is the actual server that runs the code and listens to HTTP requests.
*   `pydantic==2.5.2`: A data validation library. FastAPI uses Pydantic to ensure that the data being sent from the frontend (like JSON objects containing emails and passwords) strictly matches the expected format.

## 2. The Backend Server

**File Created:** `main.py`

This is the central entry point for the FastAPI application.

### Logic and Syntax Breakdown:

1.  **Imports and Initialization**:
    ```python
    from fastapi import FastAPI, HTTPException
    from fastapi.staticfiles import StaticFiles
    from pydantic import BaseModel
    import os

    app = FastAPI()
    ```
    We import necessary tools, including `HTTPException` to return errors (like 400 Bad Request or 401 Unauthorized), `StaticFiles` to serve our HTML/CSS/JS files, and `BaseModel` from Pydantic for data validation. `app = FastAPI()` initializes the main server object.

2.  **In-Memory Database**:
    ```python
    users_db = {}
    rsvps_db = {}
    ```
    To keep the logic straightforward without needing external database servers (like PostgreSQL or SQLite) during initial development, we use Python dictionaries (`{}`) to store registered users and event RSVPs temporarily in the computer's RAM. Note that this data resets if the server restarts.

3.  **Data Validation (Pydantic Models)**:
    ```python
    class UserRegister(BaseModel):
        name: str
        email: str
        password: str
    ```
    This class defines the exact "shape" of the data we expect when someone registers. If the frontend sends data missing an `email`, FastAPI will automatically reject the request before our logic even runs, providing built-in security and error handling.

4.  **API Endpoints**:
    ```python
    @app.post("/api/register")
    def register(user: UserRegister):
        # logic...
    ```
    The `@app.post` decorator tells FastAPI: "If you receive an HTTP POST request to the URL `/api/register`, run the function immediately below it." The function takes the validated `UserRegister` data, checks if the email already exists in `users_db` (raising a 400 error if so), and otherwise saves the user.

    Similar endpoints were created for `/api/login` and `/api/events/{event_id}/rsvp`. The curly braces in `{event_id}` make it a "path parameter", allowing us to capture dynamic URLs (e.g., `/api/events/tech-meetup/rsvp`).

5.  **Serving the Frontend**:
    ```python
    frontend_path = os.path.join(os.path.dirname(__file__), "EventLink CM Project", "frontend")
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
    ```
    Instead of making users start a separate server for the HTML files, we tell FastAPI to "mount" the folder containing your HTML/CSS/JS directly to the root URL `/`. The `html=True` flag tells it to serve `index.html` by default when a user visits the site.

## 3. Frontend Updates

The vanilla JavaScript files were updated to replace browser-only `localStorage` manipulations with asynchronous `fetch` requests communicating with the new backend.

**Files Modified:** `register.js`, `login.js`, `events.js`

### Logic and Syntax Breakdown (using `login.js` as an example):

```javascript
async function loginUser(event) {
    event.preventDefault(); // Prevents the form from refreshing the page
    // ... get email and password from DOM ...

    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });
        
        const data = await response.json();
```
*   **`async` and `await`**: These keywords allow Javascript to pause execution while waiting for the server to respond, avoiding "callback hell" and making the code look synchronous.
*   **`fetch('/api/login', ...)`**: This sends the actual HTTP request to our Python server. We specify it's a `POST` request, tell the server we're sending JSON data (`Content-Type`), and convert our Javascript object into a JSON string using `JSON.stringify()`.
*   **`response.json()`**: Once the server responds, this parses the response back into a Javascript object.

If the response is successful (`response.ok`), the JS displays a success message, saves the user's email into `localStorage` (so `events.js` knows who is logged in when they try to RSVP), and redirects to the events page.

## 4. Clean-up

**File Deleted:** `api/urls.py`

Since the backend routing is now completely handled by FastAPI via decorators (like `@app.post`), the isolated `urls.py` file, which utilized Django routing syntax, was removed to prevent confusion.
