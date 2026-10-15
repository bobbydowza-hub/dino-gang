/* Offline cache for Dino Gang. Everything is cached on first visit; no tracking, no network calls to other sites. */
var CACHE = "dinogang-__VERSION__";
var FILES = __FILES__;
self.addEventListener("install", function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(FILES); }).then(function () { return self.skipWaiting(); }));
});
self.addEventListener("activate", function (e) {
  e.waitUntil(caches.keys().then(function (ks) {
    return Promise.all(ks.filter(function (k) { return k.indexOf("dinogang-") === 0 && k !== CACHE; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});
function ranged(req, res) {
  var m = /bytes=(\d*)-(\d*)/.exec(req.headers.get("range") || "");
  return res.blob().then(function (b) {
    var size = b.size, s = m[1] ? parseInt(m[1], 10) : 0, en = m[2] ? parseInt(m[2], 10) : size - 1;
    if (!m[1] && m[2]) { s = size - parseInt(m[2], 10); en = size - 1; }
    en = Math.min(en, size - 1);
    return new Response(b.slice(s, en + 1), { status: 206, statusText: "Partial Content", headers: {
      "Content-Type": res.headers.get("Content-Type") || "video/mp4", "Content-Range": "bytes " + s + "-" + en + "/" + size, "Content-Length": String(en - s + 1) } });
  });
}
self.addEventListener("fetch", function (e) {
  var req = e.request;
  if (req.method !== "GET" || new URL(req.url).origin !== location.origin) return;
  var aboutPage = req.mode === "navigate" && /\/about\/?$/.test(new URL(req.url).pathname);
  e.respondWith(caches.open(CACHE).then(function (c) {
    return c.match(aboutPage ? "about.html" : req, { ignoreSearch: true }).then(function (hit) {
      if (!hit && req.mode === "navigate") hit = null;
      var go = hit ? Promise.resolve(hit) : c.match("./").then(function (r) { return req.mode === "navigate" && r ? r : fetch(req); });
      return go.then(function (res) { return req.headers.get("range") && res && res.status === 200 ? ranged(req, res) : res; });
    });
  }));
});
