function getCsrfToken() {
  // Prefer meta tag (always present)
  const meta = document.querySelector('meta[name="csrf-token"]');
  if (meta && meta.content) return meta.content;

  // Fallback: read cookie
  const name = 'csrftoken';
  return document.cookie.split('; ').reduce((acc, c) => {
    const [k, v] = c.split('=');
    return k === name ? decodeURIComponent(v) : acc;
  }, '');
}

async function api(url, options = {}) {
  const opts = { credentials: 'same-origin', ...options };
  opts.headers = { 'Content-Type': 'application/json', ...(opts.headers || {}) };
  // Add CSRF for unsafe methods
  const method = (opts.method || 'GET').toUpperCase();
  if (['POST','PUT','PATCH','DELETE'].includes(method)) {
    opts.headers['X-CSRFToken'] = getCsrfToken();
  }
  const res = await fetch(url, opts);
  if (!res.ok) {
    const msg = await res.text();
    throw new Error(`${res.status} ${res.statusText}: ${msg}`);
  }
  // Some endpoints (DELETE) return 204 no content
  if (res.status === 204) return null;
  return res.json();
}

window.Api = { get: (u)=>api(u),
                post: (u,b)=>api(u,{method:'POST',body:JSON.stringify(b)}),
                del: (u)=>api(u,{method:'DELETE'}) };
