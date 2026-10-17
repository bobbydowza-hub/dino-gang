#!/usr/bin/env python3
"""Build public/index.html and public/sw.js from src/. Run: python3 tools/build.py"""
import json, hashlib, os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(R, "public")
tpl = open(os.path.join(R, "src/ww-template.html"), encoding="utf-8").read()
clips = json.load(open(os.path.join(R, "src/clips.json")))

# Language audio: every clip on disk becomes a key "l:<id>"
for lg in ("en", "es", "pt", "fr"):
    d = os.path.join(P, "audio/lang", lg)
    if os.path.isdir(d):
        for fn in sorted(os.listdir(d)):
            if fn.endswith(".mp3"): clips["l:" + fn[:-4]] = "audio/lang/%s/%s" % (lg, fn)

# Extra picture words: audio/words/<grapheme>-<word>.mp3 becomes clip "x:<grapheme>-<word>"; a word is used only if its clip exists
wd = os.path.join(P, "audio/words")
if os.path.isdir(wd):
    for fn in sorted(os.listdir(wd)):
        if fn.endswith(".mp3"): clips["x:" + fn[:-4]] = "audio/words/" + fn
wx = json.load(open(os.path.join(R, "src/word-extras.json"), encoding="utf-8"))
wordx = {}
for g, lst in wx.items():
    if g.startswith("_"): continue
    ok = [{"w": w, "p": e, "k": "x:%s-%s" % (g, w)} for w, e in lst if ("x:%s-%s" % (g, w)) in clips]
    if ok: wordx[g] = ok
core, was = wx.get("_core", {}), wx.get("_was", {})
for g, word in core.items():
    xk = "x:%s-%s" % (g, word)
    if xk not in clips: print("CORE WORD HAS NO RECORDING:", g, word); continue
    old = clips.get("w:" + g)
    clips["w:" + g] = clips[xk]
    wordx[g] = [e for e in wordx.get(g, []) if e["w"] != word]
    if g in was and old:
        clips["w:was:" + g] = old
        wordx[g].append({"w": was[g][0], "p": was[g][1], "k": "w:was:" + g})
print("Extra picture words in use:", sum(len(v) for v in wordx.values()), "of", sum(len(v) for k, v in wx.items() if not k.startswith("_")))

decks = []
WIZ = {"es": ("language", True), "pt": ("portuguese", True), "fr": ("french", True)}
for lg in ("es", "pt", "fr"):
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
        did = s["id"] if lg == "es" else lg + "-" + s["id"]
        decks.append({"id": did, "wiz": wiz, "lg": lg, "name": s["name"], "type": s["type"], "tint": {"es": 3, "pt": 4, "fr": 1}[lg],
                      "ready": live, "what": s["what"], "info": s["what"], "cards": cards})
    if not live:
        miss = [i for i in pk["audioIds"] + pk.get("newEnglishPieces", []) if "l:" + i not in clips]
        print("Portuguese audio still to add:", len(miss))

assert "var CLIPS = {};" in tpl and "var LANGDECKS = [];" in tpl
frag = tpl.replace("var CLIPS = {};", "var CLIPS = " + json.dumps(clips, separators=(",", ":")) + ";", 1)
cl = json.load(open(os.path.join(R, "src/changelog.json"), encoding="utf-8"))
frag = frag.replace("var CHANGELOG = [];", "var CHANGELOG = " + json.dumps(cl, ensure_ascii=False, separators=(",", ":")) + ";", 1)
frag = frag.replace("var WORDX = {};", "var WORDX = " + json.dumps(wordx, ensure_ascii=False, separators=(",", ":")) + ";", 1)
frag = frag.replace("var LANGDECKS = [];", "var LANGDECKS = " + json.dumps(decks, ensure_ascii=False, separators=(",", ":")) + ";", 1)
frag = re.sub(r'<title>.*?</title>\s*', '', frag, count=1)
frag = re.sub(r'<link rel="preconnect"[^>]*>\s*<link rel="stylesheet"[^>]*>\s*', '', frag, count=1)

faces = ""
for w in (400, 500, 600, 700):
    faces += "@font-face{font-family:'Figtree';font-weight:%d;font-display:swap;src:url('fonts/figtree-latin-%d-normal.woff2') format('woff2')}\n" % (w, w)
for w in (400, 700):
    faces += "@font-face{font-family:'Andika';font-weight:%d;font-display:swap;src:url('fonts/andika-latin-%d-normal.woff2') format('woff2')}\n" % (w, w)
for w in (400, 700):
    faces += "@font-face{font-family:'Bobby Dowza';font-weight:%d;font-display:swap;src:url('fonts/bobbydowza-latin-%d-normal.woff2') format('woff2')}\n" % (w, w)
head = ('<!doctype html>\n<html lang="en-GB">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="color-scheme" content="light dark">\n<meta name="theme-color" content="#ff5c93">\n'
        '<title>Dino Gang</title>\n<meta name="description" content="Little learning games for ages 3 to 6: phonics, numbers and first Spanish and Portuguese, played with a grown-up. No accounts, no ads.">\n'
        '<meta property="og:type" content="website">\n<meta property="og:site_name" content="Dino Gang">\n<meta property="og:title" content="Dino Gang">\n'
        '<meta property="og:description" content="Little learning games for ages 3 to 6: phonics, numbers and first Spanish and Portuguese, played with a grown-up.">\n'
        '<meta property="og:url" content="https://dinogang.netlify.app/">\n<meta property="og:image" content="https://dinogang.netlify.app/og-image-v4.jpg">\n'
        '<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta property="og:image:alt" content="Dino Gang: a friendly green dinosaur waving">\n'
        '<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:image" content="https://dinogang.netlify.app/og-image-v4.jpg">\n'
        '<link rel="manifest" href="manifest.webmanifest">\n'
        '<link rel="icon" href="icons/icon-192.png">\n<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">\n'
        '<style>\n' + faces + '</style>\n')
sw_reg = ("<script>if('serviceWorker' in navigator&&location.protocol!=='file:'){window.addEventListener('load',function(){"
          "navigator.serviceWorker.register('sw.js').catch(function(){});});}</script>\n")
doc = head + frag.replace("</style>", "</style>\n</head>\n<body>", 1) + "\n" + sw_reg + "</body>\n</html>\n"
open(os.path.join(P, "index.html"), "w", encoding="utf-8").write(doc)

open(os.path.join(P, "about.html"), "w", encoding="utf-8").write(open(os.path.join(R, "src/about.html"), encoding="utf-8").read())

# Unlisted handwriting test page: /writing/ (not linked from the app; Tom has the URL). Letter "a" only for now.
os.makedirs(os.path.join(P, "writing"), exist_ok=True)
hw = json.load(open(os.path.join(R, "src/hw-paths.json"), encoding="utf-8"))
ha = {"strokes": hw["a"]["strokes"], "dots": [list(d) for d in hw["a"].get("dots", [])]}
open(os.path.join(P, "writing", "index.html"), "w", encoding="utf-8").write(
    open(os.path.join(R, "src/writing.html"), encoding="utf-8").read().replace("__LETTER__", json.dumps(ha)))

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
