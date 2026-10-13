# Dino Gang

Little learning games for ages 3 to 6, played with a grown-up beside the child.

- **Word Wizards**: phonics sounds, spellings and tricky words.
- **Number Wizards**: counting, seeing numbers, number bonds.
- **Language Wizards**: first Spanish (Spain). Live. A fluent-speaker check of the Spanish is still outstanding.

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

## Open items
- Native-speaker check of the Spanish (spelling, accents, pronunciation, Spain variant).
- Spanish audio licence and attribution (the Spanish clips may come from a text-to-speech service).
- Picture licence (video stills made with Midjourney) and EYFS wording to verify.
