function showMsg(el, text, type) {
  el.textContent = text;
  el.className = 'alert ' + (type === 'success' ? 'alert-success' : 'alert-error');
  el.style.display = 'block';
}

async function registerUser(event) {
  event.preventDefault();

  const name            = document.getElementById('name').value.trim();
  const email           = document.getElementById('email').value.trim();
  const password        = document.getElementById('password').value;
  const confirmPassword = document.getElementById('confirmPassword').value;
  const gender          = document.getElementById('gender').value;
  const msgEl           = document.getElementById('message');

  if (password !== confirmPassword) {
    showMsg(msgEl, 'Passwords do not match.', 'error');
    return;
  }
  if (password.length < 6) {
    showMsg(msgEl, 'Password must be at least 6 characters.', 'error');
    return;
  }

  try {
    const res  = await fetch('/api/register', {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify({ name, email, password, gender })
    });
    const data = await res.json();

    if (res.ok) {
      showMsg(msgEl, 'Account created! Taking you in…', 'success');
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
      }, 900);
    } else {
      showMsg(msgEl, data.detail || 'Registration failed. Please try again.', 'error');
    }
  } catch {
    showMsg(msgEl, 'Could not connect to the server. Please try again.', 'error');
  }
}