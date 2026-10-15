# Dino Gang

Little learning games for ages 3 to 6, played with a grown-up beside the child.

- **Word Wizards**: phonics sounds, spellings and tricky words.
- **Number Wizards**: counting, seeing numbers, number bonds.
- **Spanish Wizards**: first Spanish (Spain). Live. A fluent-speaker check is still outstanding.

- **Portuguese Wizards**: first European Portuguese. Live. Audio is text-to-speech; a fluent-speaker check is still outstanding.

No accounts, no tracking, no ads. Progress and pompoms stay on the device. Works offline after the first visit.

## How it is built
Static site. `public/` is what gets hosted (Netlify publishes it, see `netlify.toml`).

```
src/ww-template.html            the app (HTML, CSS, JS)
src/clips.json                  sound/word/number clip keys -> audio files
src/language-wizards-es-pack.json   Language Wizards content
src/sw.template.js              offline cache
tools/build.py                  builds public/index.html and public/sw.js
public/audio, video, fonts      media (fonts are self-hosted, no Google requests)
```

After changing anything in `src/` or `public/`, run `python3 tools/build.py` and commit the result.

## Working without spending deploys
Every push to `main` is a Netlify production deploy and uses credits, so day-to-day work happens on the `dev` branch, which Netlify skips (see `ignore` in `netlify.toml`).

- Work and commit on `dev`. Preview locally: `cd public && python3 -m http.server 8000`, then open http://localhost:8000.
- Release only when ready: `git checkout main && git merge --ff-only dev && git push origin main`, then `git checkout dev`. That is one deploy, however many changes it contains.
- In Netlify, keep branch deploys and deploy previews switched off (Site configuration, Build and deploy, Branches and deploy contexts).

## Open items
- Native-speaker check of the Spanish (spelling, accents, pronunciation, Spain variant).
- Spanish audio licence and attribution (the Spanish clips may come from a text-to-speech service).
- Picture licence (video stills made with Midjourney) and EYFS wording to verify.
