function showMsg(el, text, type) {
  el.textContent = text;
  el.className = 'alert ' + (type === 'success' ? 'alert-success' : 'alert-error');
  el.style.display = 'block';
}

async function loginUser(event) {
  event.preventDefault();

  const email    = document.getElementById('email').value.trim();
  const password = document.getElementById('password').value;
  const msgEl    = document.getElementById('message');

  try {
    const res  = await fetch('/api/login', {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify({ email, password })
    });
    const data = await res.json();

    if (res.ok) {
      showMsg(msgEl, 'Logged in! Redirecting…', 'success');
      localStorage.setItem('currentUser', email);

      // Process any pending RSVP
      const pending = localStorage.getItem('pendingRSVP');
      if (pending) {
        try {
          await fetch(`/api/events/${pending}/rsvp`, {
            method:  'POST',
            headers: { 'Content-Type': 'application/json' },
            body:    JSON.stringify({ email })
          });
          localStorage.removeItem('pendingRSVP');
        } catch (e) { console.warn('Pending RSVP failed', e); }
      }

      setTimeout(() => {
        const redirect = localStorage.getItem('redirectAfterLogin');
        if (redirect) { localStorage.removeItem('redirectAfterLogin'); window.location.href = redirect; }
        else          { window.location.href = '/user-home'; }
      }, 800);
    } else {
      showMsg(msgEl, data.detail || 'Incorrect email or password.', 'error');
    }
  } catch {
    showMsg(msgEl, 'Could not connect to the server. Please try again.', 'error');
  }
}