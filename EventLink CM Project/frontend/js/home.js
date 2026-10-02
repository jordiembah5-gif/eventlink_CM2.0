// ── SHARED UTILITIES ──────────────────────────────────────────

// Mobile nav toggle
function toggleNav() {
  const nav = document.getElementById('navLinks');
  if (nav) nav.classList.toggle('open');
}

// ── HOME PAGE LOGIC ───────────────────────────────────────────

document.addEventListener('DOMContentLoaded', () => {
  // If already logged in, redirect to user home
  if (localStorage.getItem('currentUser')) {
    window.location.href = '/user-home';
    return;
  }
  // Load a preview of events on the home page
  loadHomeEvents();
});

async function loadHomeEvents() {
  const grid = document.getElementById('homeEventGrid');
  if (!grid) return;

  try {
    const res  = await fetch('/api/events');
    const data = await res.json();
    const events = data.events.slice(0, 3); // show only first 3

    if (events.length === 0) {
      grid.innerHTML = `
        <div style="grid-column:1/-1;text-align:center;padding:60px 20px;color:#8C908A;">
          <i class="fas fa-calendar-times" style="font-size:40px;color:#E4E6E2;margin-bottom:16px;display:block;"></i>
          <p>No events yet. <a href="/create-event" style="color:#2DB67D;">Be the first to host one!</a></p>
        </div>`;
      return;
    }

    grid.innerHTML = events.map(e => buildEventCard(e)).join('');
  } catch {
    grid.innerHTML = `<div style="grid-column:1/-1;text-align:center;padding:40px;color:#8C908A;">Could not load events right now.</div>`;
  }
}

// Build a reusable event card HTML string
function buildEventCard(e) {
  const fallbackImg = 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=600&auto=format&fit=crop&q=70';
  const img = e.icon && !e.icon.startsWith('images/') ? e.icon : fallbackImg;
  return `
    <article class="event-card" data-category="${e.category || ''}">
      <div class="event-card-image">
        <img src="${img}" alt="${e.name}" loading="lazy" onerror="this.src='${fallbackImg}'">
      </div>
      <div class="event-card-body">
        <div class="event-card-category">${e.category || 'Event'}</div>
        <div class="event-card-title">${e.name}</div>
        <div class="event-card-meta">
          <span><i class="fas fa-map-marker-alt"></i>${e.location}</span>
          <span><i class="fas fa-calendar-alt"></i>${e.date}</span>
        </div>
      </div>
      <div class="event-card-footer">
        <span class="event-card-rsvp badge badge-green">Free</span>
        <button class="btn btn-green btn-sm" onclick="joinEvent('${e.name}', '${e.id}')">
          Register <i class="fas fa-arrow-right"></i>
        </button>
      </div>
    </article>`;
}

function searchFromHome() {
  const query    = (document.getElementById('homeSearch')?.value || '').trim();
  const category = document.getElementById('homeCategory')?.value || 'all';
  let url = '/events';
  const params = [];
  if (query)          params.push('search=' + encodeURIComponent(query));
  if (category !== 'all') params.push('category=' + encodeURIComponent(category));
  if (params.length)  url += '?' + params.join('&');
  window.location.href = url;
}