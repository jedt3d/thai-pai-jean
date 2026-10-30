const CACHE='tpj-v1';
const FILES=['./','index.html','style.css','app.js','data.js','assets/icon.svg','manifest.webmanifest','guide-th.md','Yunnan_Photo_Trip_2026.kml'];
self.addEventListener('install',event=>{event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(FILES)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',event=>{event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith('tpj-')&&k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',event=>{if(event.request.method!=='GET'||new URL(event.request.url).origin!==self.location.origin)return;event.respondWith(fetch(event.request).then(response=>{if(response.ok){const copy=response.clone();event.waitUntil(caches.open(CACHE).then(c=>c.put(event.request,copy)))}return response}).catch(()=>caches.match(event.request).then(r=>r||(event.request.mode==='navigate'?caches.match('./'):Response.error()))))});
