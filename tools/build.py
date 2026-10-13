#!/usr/bin/env python3
"""Build public/index.html and public/sw.js from src/. Run: python3 tools/build.py"""
import json, hashlib, os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(R, "public")
tpl = open(os.path.join(R, "src/ww-template.html"), encoding="utf-8").read()
clips = json.load(open(os.path.join(R, "src/clips.json")))
pack = json.load(open(os.path.join(R, "src/language-wizards-es-pack.json"), encoding="utf-8"))

# Language audio: every id in the pack plus the sentence pieces
for fn in sorted(os.listdir(os.path.join(P, "audio/lang/en"))):
    if fn.endswith(".mp3"): clips["l:" + fn[:-4]] = "audio/lang/en/" + fn
for fn in sorted(os.listdir(os.path.join(P, "audio/lang/es"))):
    if fn.endswith(".mp3"): clips["l:" + fn[:-4]] = "audio/lang/es/" + fn

decks = []
for i, s in enumerate(pack["sets"]):
    cards = []
    for k, c in enumerate(s["cards"]):
        c = dict(c)
        if c.get("video"):
            c["poster"] = "video/posters/" + c["video"].rsplit(".", 1)[0] + ".jpg"
            c["video"] = "video/" + c["video"]
        if c.get("t") == "number": c["n"] = k + 1
        cards.append(c)
    decks.append({"id": s["id"], "wiz": "language", "name": s["name"], "type": s["type"], "tint": 3,
                  "ready": bool(s.get("ready")), "what": s["what"], "info": s["what"], "cards": cards})
for d, s in zip(decks, pack["sets"]):
    assert all(c["audio"]["en"] in [x[2:] for x in clips if x.startswith("l:")] and c["audio"]["es"] in [x[2:] for x in clips if x.startswith("l:")] for c in d["cards"]), d["id"]

assert "var CLIPS = {};" in tpl and "var LANGDECKS = [];" in tpl
frag = tpl.replace("var CLIPS = {};", "var CLIPS = " + json.dumps(clips, separators=(",", ":")) + ";", 1)
frag = frag.replace("var LANGDECKS = [];", "var LANGDECKS = " + json.dumps(decks, ensure_ascii=False, separators=(",", ":")) + ";", 1)
frag = re.sub(r'<title>.*?</title>\s*', '', frag, count=1)
frag = re.sub(r'<link rel="preconnect"[^>]*>\s*<link rel="stylesheet"[^>]*>\s*', '', frag, count=1)

faces = ""
for w in (400, 500, 600, 700):
    faces += "@font-face{font-family:'Fredoka';font-weight:%d;font-display:swap;src:url('fonts/fredoka-latin-%d-normal.woff2') format('woff2')}\n" % (w, w)
for w in (400, 700):
    faces += "@font-face{font-family:'Andika';font-weight:%d;font-display:swap;src:url('fonts/andika-latin-%d-normal.woff2') format('woff2')}\n" % (w, w)
head = ('<!doctype html>\n<html lang="en-GB">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="color-scheme" content="light dark">\n<meta name="theme-color" content="#ff5c93">\n'
        '<title>Dino Gang</title>\n<link rel="manifest" href="manifest.webmanifest">\n'
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
