#!/usr/bin/env python3
"""Build public/index.html and public/sw.js from src/. Run: python3 tools/build.py"""
import json, hashlib, os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(R, "public")
tpl = open(os.path.join(R, "src/ww-template.html"), encoding="utf-8").read()
clips = json.load(open(os.path.join(R, "src/clips.json")))

# Language audio: every clip on disk becomes a key "l:<id>"
for lg in ("en", "es", "pt"):
    d = os.path.join(P, "audio/lang", lg)
    if os.path.isdir(d):
        for fn in sorted(os.listdir(d)):
            if fn.endswith(".mp3"): clips["l:" + fn[:-4]] = "audio/lang/%s/%s" % (lg, fn)

decks = []
WIZ = {"es": ("language", True), "pt": ("portuguese", True)}
for lg in ("es", "pt"):
    pk = json.load(open(os.path.join(R, "src/language-wizards-%s-pack.json" % lg), encoding="utf-8"))
    wiz, live = WIZ[lg]
    for s in pk["sets"]:
        cards = []
        for k, c in enumerate(s["cards"]):
            c = dict(c)
            c["tl"] = c.pop(lg); c["lg"] = lg
            c["audio"] = {"en": c["audio"]["en"], "tl": c["audio"][lg]}
            if c.get("video"):
                c["poster"] = "video/posters/" + c["video"].rsplit(".", 1)[0] + ".jpg"
                c["video"] = "video/" + c["video"]
            if c.get("t") == "number": c["n"] = k + 1
            if not all(("l:" + c["audio"][x]) in clips for x in ("en", "tl")):
                print("SKIPPED (audio missing):", lg, s["id"], c["en"]); continue
            cards.append(c)
        did = s["id"] if lg == "es" else "pt-" + s["id"]
        decks.append({"id": did, "wiz": wiz, "lg": lg, "name": s["name"], "type": s["type"], "tint": 3 if lg == "es" else 4,
                      "ready": live, "what": s["what"], "info": s["what"], "cards": cards})
    if not live:
        miss = [i for i in pk["audioIds"] + pk.get("newEnglishPieces", []) if "l:" + i not in clips]
        print("Portuguese audio still to add:", len(miss))

assert "var CLIPS = {};" in tpl and "var LANGDECKS = [];" in tpl
frag = tpl.replace("var CLIPS = {};", "var CLIPS = " + json.dumps(clips, separators=(",", ":")) + ";", 1)
frag = frag.replace("var LANGDECKS = [];", "var LANGDECKS = " + json.dumps(decks, ensure_ascii=False, separators=(",", ":")) + ";", 1)
frag = re.sub(r'<title>.*?</title>\s*', '', frag, count=1)
frag = re.sub(r'<link rel="preconnect"[^>]*>\s*<link rel="stylesheet"[^>]*>\s*', '', frag, count=1)

faces = ""
for w in (400, 500, 600, 700):
    faces += "@font-face{font-family:'Figtree';font-weight:%d;font-display:swap;src:url('fonts/figtree-latin-%d-normal.woff2') format('woff2')}\n" % (w, w)
for w in (400, 700):
    faces += "@font-face{font-family:'Andika';font-weight:%d;font-display:swap;src:url('fonts/andika-latin-%d-normal.woff2') format('woff2')}\n" % (w, w)
head = ('<!doctype html>\n<html lang="en-GB">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="color-scheme" content="light dark">\n<meta name="theme-color" content="#ff5c93">\n'
        '<title>Dino Gang</title>\n<meta name="description" content="Little learning games for ages 3 to 6: phonics, numbers and first Spanish and Portuguese, played with a grown-up. No accounts, no ads.">\n'
        '<meta property="og:type" content="website">\n<meta property="og:site_name" content="Dino Gang">\n<meta property="og:title" content="Dino Gang">\n'
        '<meta property="og:description" content="Little learning games for ages 3 to 6: phonics, numbers and first Spanish and Portuguese, played with a grown-up.">\n'
        '<meta property="og:url" content="https://dinogang.netlify.app/">\n<meta property="og:image" content="https://dinogang.netlify.app/og-image-v3.png">\n'
        '<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta property="og:image:alt" content="Dino Gang: a friendly green dinosaur waving">\n'
        '<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:image" content="https://dinogang.netlify.app/og-image-v3.png">\n'
        '<link rel="manifest" href="manifest.webmanifest">\n'
        '<link rel="icon" href="icons/icon-192.png">\n<link rel="apple-touch-icon" href="icons/icon-192.png">\n'
        '<style>\n' + faces + '</style>\n')
sw_reg = ("<script>if('serviceWorker' in navigator&&location.protocol!=='file:'){window.addEventListener('load',function(){"
          "navigator.serviceWorker.register('sw.js').catch(function(){});});}</script>\n")
doc = head + frag.replace("</style>", "</style>\n</head>\n<body>", 1) + "\n" + sw_reg + "</body>\n</html>\n"
open(os.path.join(P, "index.html"), "w", encoding="utf-8").write(doc)

# Service worker: precache everything, versioned by content hash
files = []
for root, _, fns in os.walk(P):
    for fn in sorted(fns):
        rel = os.path.relpath(os.path.join(root, fn), P).replace(os.sep, "/")
        if rel in ("sw.js",) or fn.startswith("LICENSE"): continue
        files.append(rel)
files.sort()
h = hashlib.sha1()
for rel in files: h.update(rel.encode()); h.update(open(os.path.join(P, rel), "rb").read())
ver = h.hexdigest()[:10]
sw = open(os.path.join(R, "src/sw.template.js")).read().replace("__VERSION__", ver).replace("__FILES__", json.dumps(["./"] + files))
open(os.path.join(P, "sw.js"), "w").write(sw)
print("built", len(doc) // 1024, "KB index,", len(files), "files, cache", ver)
