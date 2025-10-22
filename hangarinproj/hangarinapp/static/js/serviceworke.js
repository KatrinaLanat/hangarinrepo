const CACHE_NAME = 'hangarin-cache-v1';

// Files to precache initially (update with any new main static files)
const urlsToPreCache = [
  '/',
  '/static/css/bootstrap.min.css',
  '/static/js/main.js',
  '/static/images/icon-192.png',
  '/static/images/icon-512.png'
];

// Install Service Worker and precache initial files
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(urlsToPreCache);
    })
  );
  self.skipWaiting();
});

// Activate Service Worker and clean up old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))
      );
    })
  );
  self.clients.claim();
});

// Fetch requests: cache first, then network
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(cachedResponse => {
      if (cachedResponse) return cachedResponse;

      return fetch(event.request).then(networkResponse => {
        // Only cache valid responses
        if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
          return networkResponse;
        }

        const responseClone = networkResponse.clone();
        caches.open(CACHE_NAME).then(cache => {
          cache.put(event.request, responseClone);
        });
        return networkResponse;
      });
    }).catch(() => {
      // Fallback to homepage if offline
      if (event.request.mode === 'navigate') {
        return caches.match('/');
      }
    })
  );
});
