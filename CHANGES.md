# Dino Gang change list

Tom adds items with `/change-dino: <what to change>`. A scheduled run applies them to the `dev` branch twice a day (about 08:00 and 18:00 UK time). Nothing here goes live until Tom says "release".

## Rules for whoever applies this list (a scheduled run or a live session)
1. Work only on the `dev` branch. Never push to `main`, never merge to `main`, never open a pull request. Every push to `main` spends Netlify deploy credits.
2. Only act on items under **Pending**. Skip anything marked `NEEDS TOM`.
3. Apply each item in `src/` (and `public/` where needed), run `python3 tools/build.py`, check it (open it in Playwright at phone width, or grep/diff for text changes), then commit to `dev` with a message naming the item.
4. Move each finished item to **Done** with the date and a one-line result. If an item is unclear, risky, or would make something worse, leave it in Pending, mark it `NEEDS TOM` and say why. Do not guess.
5. If there are no Pending items, change nothing and finish quickly.
6. Do not edit audio, the Spanish or Portuguese wording, or the A5 PDF unless the item says to.
7. All wording in the app, About page, changelog and guide must be UK English (colour, maths, recognise, centre). Note that "practise" is the verb and "practice" is the noun in UK English; both are used correctly today. Do not swap them.
8. Push `dev` (free) and finish with a short summary: what changed, what needs Tom's decision. The summary is for Tom to read; keep it brief.

## Pending
- [ ] 2026-10-17 Reminder for Tom: re-record the "y" audio file.
  - NEEDS TOM: this is waiting on his new recording, so the scheduled run should skip it. Which clip does he mean: the sound (`public/audio/y.mp3`) or the picture word (`public/audio/w-y.mp3`, yoyo)? When he sends it, replace only that one clip with the dino-cut-audio steps.
- [ ] 2026-10-17 Handwriting letters: custom font "Bobby Dowza" (Tom's name for it).
  - NEEDS TOM: not ready for a scheduled run. Plan: Andika-based, with redrawn a, e, f, i, j, m, n, u, y (plain, no tails, small kicks on a, i, n, m, u). Tom approved the proof sheet (v3). Next: stroke paths for Trace and the ball, then build the font (OFL: new name, keep licence text) for Word Wizard cards and the handwriting module. Draft stroke paths for all 26 letters are in `src/hw-paths.json` (not used by the build yet).

- [ ] 2026-10-17 Handwriting module goes on its own page, `/writing`, NOT on the main menu while testing. Build Watch and Trace for the Autumn 1 letters first. NEEDS TOM: waiting on his recording and go-ahead; scheduled runs skip it.
- [ ] 2026-10-17 French module (NEEDS TOM: waiting on his recordings; scheduled runs skip it). 27 French clips per the handoff audio list (bonne journée replaces a second bonjour; s'il vous plaît is the handoff default) plus 3 English clips: have a good day, q-open-06-fr, q-end-04-fr. Then build the pack (`src/language-wizards-fr-pack.json`, from the handoff zip) and add French to All words. Open with Tom: France or Canada, vous or te, native speaker or text-to-speech.

## Decisions (Tom, 2026-10-17)
- French: "bonne journée" (not a second bonjour) and "s'il vous plaît".
- Portuguese handoff is stale: ignore it; the app's Portuguese pack is the source.
- Spanish and Portuguese "good afternoon": keep `l8-good-afternoon-vid.mp4` and the 🌤️ picture.

## Done
- [x] 2026-10-17 Language Wizards: one menu item (cover and top-right menu) opening Spanish Wizards, Portuguese Wizards and All words (was Language Zone). Tested. Not released.
- [x] 2026-10-17 Top-left logo becomes a blue Home icon (label "Home") on every screen except the wizard list; tapping it still goes to the wizard list. Tested on cover, wizard home, session. Not released.
- 2026-10-17 Spring 1 phrases for ear and air changed ("Cheer for the deer", "A fairy on the stairs") because the earlier ones shared words with the Wandle phrases. Deck is not live. Handwriting module proposals are in the workbook sheets Catchphrases, Letter formation, Handwriting font and Handwriting layouts (waiting for Tom to agree before any build).
- 2026-10-16 Centred the hands (done live on dev): 1 to 4 on the palm, 5 and the pairs on their real bounds, checked in light and dark. Also a new share image, public/og-image-v4.jpg (85 KB; the old PNG was 308 KB, just over WhatsApp's roughly 300 KB limit), tags updated on the home page and About page. Only visible after a release. WhatsApp caches old previews, so share dinogang.netlify.app/?v=2 to force a fresh one.
- 2026-10-16 Distance from Little Wandle (done live on dev): mouth hints, the six Autumn 2 catchphrases and the Spring 1 phrases rewritten; toggle renamed "Standard picture words / More picture words" (off by default). Picture words deliberately STAY the same as Little Wandle for familiarity (Tom, 12:53), so do not swap them. About page, A5 PDF, changelog and card comments cite DfE Letters and Sounds (2007) and no longer name Little Wandle. STILL OPEN: replacing Autumn 1 and 2 picture words before any commercial release (needs recordings from Tom).
- 2026-10-16 Extras toggle: Word Wizards now has "Little Wandle words only / Add extra picture words" beside Letter first / Word first, saved in prefs as `xw`, OFF by default. Off: Word first uses each card's original keyword only (checked: no extra picture appeared in 25 starts; extras appear when on). About page and changelog updated.
- 2026-10-16 Number Wizards fingers (both fingers items): replaced bar-style `fingersSVG` with the approved ghost hands (B2 full-hand fill), one hand to 5, two to 10, first hand always blue, second in the colour of n-5, thumb last, accessible label kept, checked in light and dark.
- 2026-10-16 Number Wizards colours and formulas: 6 changed from indigo to purple #8E24AA (NUMCOL and all 6 entries in the number decks). Audited all number cards by script (word, colour, blocks, emoji counts, say text, equations, bonds, missing parts): nothing wrong found. Note: 6 and the purple stripe of 7's rainbow now share a colour, as in the school convention.
- 2026-10-16 UK English check (Tom: "ensure the app is UK English"). Scanned all visible text in the app, About page, changelog and word lists. Already UK English throughout (colours, coloured, recognising, maths, practise as a verb, practice as a noun). No changes needed. One thing noted for Tom: the "truck" picture word for ck is American; UK children often say "lorry" (a recording would be needed).
