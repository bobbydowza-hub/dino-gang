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
(none)
- [ ] 2026-10-16 Number Wizards fingers: centre the single hand for 1 to 4. Tom: "make sure that on the single hand, the hand diagram for 1 to 4 is centred (I think it's off centre because it's compensating for the thumb on hand 5)."
  - Note (not blocking): Tom is right. In `fingersSVG` the one-hand viewBox is "4 8 124 130" for every n from 1 to 5, which is centred on the 5-hand including its thumb (content about x 14 to 120). For 1 to 4 there is no thumb, so the palm (x 34 to 120, centre 77) sits about 11 units right of centre. Fix: for 1 to 4 use a viewBox centred on x = 77 (for example "15 8 124 130"); leave 5 as it is. For 6 to 10, centre the pair on its real content bounds too (when the second hand has no thumb the pair sits slightly left of centre). Check the result in a screenshot for 1, 3, 4, 5, 7 and 10, light and dark.

## Done
- 2026-10-16 Extras toggle: Word Wizards now has "Little Wandle words only / Add extra picture words" beside Letter first / Word first, saved in prefs as `xw`, OFF by default. Off: Word first uses each card's original keyword only (checked: no extra picture appeared in 25 starts; extras appear when on). About page and changelog updated.
- 2026-10-16 Number Wizards fingers (both fingers items): replaced bar-style `fingersSVG` with the approved ghost hands (B2 full-hand fill), one hand to 5, two to 10, first hand always blue, second in the colour of n-5, thumb last, accessible label kept, checked in light and dark.
- 2026-10-16 Number Wizards colours and formulas: 6 changed from indigo to purple #8E24AA (NUMCOL and all 6 entries in the number decks). Audited all number cards by script (word, colour, blocks, emoji counts, say text, equations, bonds, missing parts): nothing wrong found. Note: 6 and the purple stripe of 7's rainbow now share a colour, as in the school convention.
- 2026-10-16 UK English check (Tom: "ensure the app is UK English"). Scanned all visible text in the app, About page, changelog and word lists. Already UK English throughout (colours, coloured, recognising, maths, practise as a verb, practice as a noun). No changes needed. One thing noted for Tom: the "truck" picture word for ck is American; UK children often say "lorry" (a recording would be needed).
