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
- [x] 2026-10-17 Handwriting letters: custom font "Bobby Dowza" built from Andika (a e f i j m n u y redrawn; OFL licence kept in `public/fonts/LICENSE-BobbyDowza.txt`; script `tools/make-bobby-dowza.py`). Now the card font on every card. Tom to review screenshots.
  - Remaining: stroke paths for the other letters (Tom reviewing the sheet; "l" keeps its kick).

- [ ] 2026-10-17 Handwriting module: unlisted test page `/writing/` for the letter "a" only (Watch, Trace, astronaut picture, word audio, description). Not linked from the app. Tom: combined release with French. Other letters wait for his stroke review.
- [ ] 2026-10-17 French Wizards: built and on `dev` (27 word clips plus the 3 English clips). Native-speaker check still to do for ES, PT and FR before anything ships.

- [ ] 2026-10-19 Home button doesn't work (Tom's note). NEEDS TOM: which screen and device? Checked on desktop Chromium at phone width: the logo does take you home from the Languages screen.

## Decisions (Tom, 2026-10-17)
- French: "bonne journée" (not a second bonjour) and "s'il vous plaît".
- Portuguese handoff is stale: ignore it; the app's Portuguese pack is the source.
- Spanish and Portuguese "good afternoon": keep `l8-good-afternoon-vid.mp4` and the 🌤️ picture.

## Done
- 2026-10-19: All 35 letter sounds replaced with EL clips (Tommy D voice, GarageBand-cleaned batches, cut by gaps and counts). Tom's recordings are in git history. NEEDS TOM: listen to all 35; check EL licence.
- 2026-10-18: Number Wizards second half (n3-01 to n3-20) regenerated in ElevenLabs in [energetic] with a pause after the first word (or first sentence for the "missing part" lines). Supersedes the 15-clip bond replacement above. Cut at 0.68 s (20 clips found, as expected). NEEDS TOM: listen.
- 2026-10-18: Number Wizards bond clips n3-01 to n3-08 and n3-13 to n3-17 regenerated in ElevenLabs with a short pause after the first number ("Two [pause] is one and one"); n3-01 and n3-02 use [energetic] instead of [playful]. 15 clips replaced, cut at 0.8 s gaps (13 found, as expected). NEEDS TOM: listen.
- 2026-10-18: Number Wizards counting clips (n1, n2, n3, 55) replaced with Tom's ElevenLabs recording (cut at 0.7 s gaps; count matched exactly). Tom's own recordings are in git history (commit before this one). NEEDS TOM: listen to all 55; check ElevenLabs licence covers commercial use before anything beyond school parents.
- 2026-10-17: French Wizards added to Language Wizards and to All words (Español / Português / Français / All).
- [x] 2026-10-17 Re-recorded the Word Wizards "y" sound: Tom's single take cleaned and repeated three times (`public/audio/y.mp3`). Not released.
- [x] 2026-10-17 Language Wizards: one menu item (cover and top-right menu) opening Spanish Wizards, Portuguese Wizards and All words (was Language Zone). Tested. Not released.
- [x] 2026-10-17 Top-left logo becomes a blue Home icon (label "Home") on every screen except the wizard list; tapping it still goes to the wizard list. Tested on cover, wizard home, session. Not released.
- 2026-10-17 Spring 1 phrases for ear and air changed ("Cheer for the deer", "A fairy on the stairs") because the earlier ones shared words with the Wandle phrases. Deck is not live. Handwriting module proposals are in the workbook sheets Catchphrases, Letter formation, Handwriting font and Handwriting layouts (waiting for Tom to agree before any build).
- 2026-10-16 Centred the hands (done live on dev): 1 to 4 on the palm, 5 and the pairs on their real bounds, checked in light and dark. Also a new share image, public/og-image-v4.jpg (85 KB; the old PNG was 308 KB, just over WhatsApp's roughly 300 KB limit), tags updated on the home page and About page. Only visible after a release. WhatsApp caches old previews, so share dinogang.netlify.app/?v=2 to force a fresh one.
- 2026-10-16 Distance from Little Wandle (done live on dev): mouth hints, the six Autumn 2 catchphrases and the Spring 1 phrases rewritten; toggle renamed "Standard picture words / More picture words" (off by default). Picture words deliberately STAY the same as Little Wandle for familiarity (Tom, 12:53), so do not swap them. About page, A5 PDF, changelog and card comments cite DfE Letters and Sounds (2007) and no longer name Little Wandle. STILL OPEN: replacing Autumn 1 and 2 picture words before any commercial release (needs recordings from Tom).
- 2026-10-16 Extras toggle: Word Wizards now has "Little Wandle words only / Add extra picture words" beside Letter first / Word first, saved in prefs as `xw`, OFF by default. Off: Word first uses each card's original keyword only (checked: no extra picture appeared in 25 starts; extras appear when on). About page and changelog updated.
- 2026-10-16 Number Wizards fingers (both fingers items): replaced bar-style `fingersSVG` with the approved ghost hands (B2 full-hand fill), one hand to 5, two to 10, first hand always blue, second in the colour of n-5, thumb last, accessible label kept, checked in light and dark.
- 2026-10-16 Number Wizards colours and formulas: 6 changed from indigo to purple #8E24AA (NUMCOL and all 6 entries in the number decks). Audited all number cards by script (word, colour, blocks, emoji counts, say text, equations, bonds, missing parts): nothing wrong found. Note: 6 and the purple stripe of 7's rainbow now share a colour, as in the school convention.
- 2026-10-16 UK English check (Tom: "ensure the app is UK English"). Scanned all visible text in the app, About page, changelog and word lists. Already UK English throughout (colours, coloured, recognising, maths, practise as a verb, practice as a noun). No changes needed. One thing noted for Tom: the "truck" picture word for ck is American; UK children often say "lorry" (a recording would be needed).

- 2026-10-19: Letter sounds s, a, t, p replaced with EL test clips (Tommy D voice, cut by sound count 2/3/3/3, trailing ghost dropped). NEEDS TOM: listen; previous recordings are in git history.
