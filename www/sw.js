// ওয়েব সংস্করণ: কম্পিউটারে "অ্যাপ হিসেবে ইনস্টল" চালু রাখতে। কোনো কিছু ক্যাশ করে না — সবসময় সর্বশেষ সংস্করণ।
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil(self.clients.claim()));
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET' || e.request.mode !== 'navigate') return;
  e.respondWith(fetch(e.request).catch(() => new Response('<!doctype html><meta charset="utf-8"><title>সহগ গণিত একাডেমি</title><body style="font-family:sans-serif;text-align:center;padding:40px">ইন্টারনেট সংযোগ নেই। সংযোগ চালু করে আবার চেষ্টা করুন।</body>', { headers: { 'Content-Type': 'text/html; charset=utf-8' } })));
});
