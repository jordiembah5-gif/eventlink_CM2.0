// ── SHARED ────────────────────────────────────────────────────
function toggleNav() {
  const nav = document.getElementById('navLinks');
  if (nav) nav.classList.toggle('open');
}

const FALLBACK_IMG = 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=600&auto=format&fit=crop&q=70';

function buildEventCard(e) {
  const img = e.icon && !e.icon.startsWith('images/') ? e.icon : FALLBACK_IMG;
  return `
    <article class="event-card" data-category="${(e.category || '').toLowerCase()}">
      <div class="event-card-image">
        <img src="${img}" alt="${e.name}" loading="lazy" onerror="this.src='${FALLBACK_IMG}'">
      </div>
      <div class="event-card-body">
        <div class="event-card-category">${e.category || 'Event'}</div>
        <div class="event-card-title">${e.name}</div>
        <div class="event-card-meta">
          <span><i class="fas fa-map-marker-alt"></i>${e.location}</span>
          <span><i class="fas fa-calendar-alt"></i>${e.date}</span>
          <span><i class="fas fa-user"></i>${e.created_by || 'Organiser'}</span>
        </div>
      </div>
      <div class="event-card-footer">
        <span class="badge badge-green">Free</span>
        <button class="btn btn-green btn-sm" onclick="joinEvent('${e.name}', '${e.id}')">
          Get ticket <i class="fas fa-ticket-alt"></i>
        </button>
      </div>
    </article>`;
}

// ── LOAD EVENTS ───────────────────────────────────────────────
let allEvents = [];

document.addEventListener('DOMContentLoaded', async () => {
  // Read URL params for pre-filling search
  const params   = new URLSearchParams(window.location.search);
  const searchQ  = params.get('search') || '';
  const catQ     = params.get('category') || 'all';

  const searchEl = document.getElementById('searchInput');
  const catEl    = document.getElementById('categoryFilter');
  if (searchEl && searchQ) searchEl.value = searchQ;
  if (catEl && catQ !== 'all') catEl.value = catQ;

  await loadEvents();

  if (searchQ || catQ !== 'all') filterEvents();
});

async function loadEvents() {
  const grid = document.getElementById('eventGrid');
  if (!grid) return;

  try {
    const res  = await fetch('/api/events');
    const data = await res.json();
    allEvents  = data.events || [];

    renderEvents(allEvents);
  } catch {
    grid.innerHTML = `
      <div style="grid-column:1/-1;text-align:center;padding:60px 20px;color:#8C908A;">
        <i class="fas fa-exclamation-circle" style="font-size:32px;margin-bottom:12px;display:block;"></i>
        Could not connect to the server. Make sure the backend is running.
      </div>`;
  }
}

function renderEvents(events) {
  const grid     = document.getElementById('eventGrid');
  const noResult = document.getElementById('noResults');

  if (events.length === 0) {
    grid.innerHTML = '';
    if (noResult) noResult.style.display = 'block';
    return;
  }

  if (noResult) noResult.style.display = 'none';
  grid.innerHTML = events.map(buildEventCard).join('');
}

// ── FILTER ────────────────────────────────────────────────────
function filterEvents() {
  const search   = (document.getElementById('searchInput')?.value || '').toLowerCase().trim();
  const category = (document.getElementById('categoryFilter')?.value || 'all');

  const filtered = allEvents.filter(e => {
    const text  = (e.name + ' ' + e.location + ' ' + e.category).toLowerCase();
    const matchS = !search || text.includes(search);
    const matchC = category === 'all' || (e.category || '').toLowerCase() === category;
    return matchS && matchC;
  });

  renderEvents(filtered);
}

// Category pill clicks
function setCategory(cat, el) {
  document.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
  el.classList.add('active');
  const sel = document.getElementById('categoryFilter');
  if (sel) sel.value = cat;
  filterEvents();
}

// ── RSVP / JOIN EVENT ─────────────────────────────────────────
async function joinEvent(eventName, eventId) {
  const email = localStorage.getItem('currentUser');

  if (!email) {
    localStorage.setItem('pendingRSVP', eventId);
    localStorage.setItem('redirectAfterLogin', '/events');
    window.location.href = '/register';
    return;
  }

  try {
    const res  = await fetch(`/api/events/${eventId}/rsvp`, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify({ email })
    });
    const data = await res.json();

    if (res.ok) {
      document.getElementById('qrMessage').textContent = `You're registered for "${eventName}". Show this QR code at the entrance.`;
      const qrData = encodeURIComponent(`EventLink CM | Event: ${eventName} | User: ${email}`);
      document.getElementById('qrImage').src = `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=${qrData}`;
      document.getElementById('qrModal').classList.add('open');
    } else {
      const msg = data.detail || 'Could not register for this event.';
      // Check if already registered
      if (msg.toLowerCase().includes('already')) {
        alert('You are already registered for this event!');
      } else {
        alert(msg);
      }
    }
  } catch {
    alert('An error occurred. Please check your connection and try again.');
  }
}

function closeModal() {
  document.getElementById('qrModal')?.classList.remove('open');
}

// Close modal on overlay click
document.addEventListener('click', e => {
  if (e.target.id === 'qrModal') closeModal();
});