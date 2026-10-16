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
- [ ] 2026-10-16 We need a mechanism to toggle the additional words we have added. Little Wandle wall charts and course material only focus on the original A1 and A2 words and sounds. Our additions (the 39 extra picture words) were to build out bulk, but are not explicitly used by the school or Little Wandle.
  - Tom confirmed 2026-10-16: extras OFF by default. Details: so the app matches Little Wandle out of the box, with a "Little Wandle words only / Add extra picture words" toggle on the Word Wizards screen beside Letter first / Word first, saved in prefs. With extras off, Word first still works using each card's original keyword. Also mention it on the About page and in the changelog.
- [ ] 2026-10-16 Number Wizards: is there a better image to depict the fingers? (Tom says he likes the counting imagery in Number Wizards otherwise.)
  - Note (not blocking): fingers are currently drawn by `fingersSVG` as simple bars of different heights. Try a friendlier hand: rounded fingers, a palm and a thumb, one hand for 1 to 5 and two hands for 6 to 10, raised fingers coloured and the rest folded or faint. Keep the accessible label ("3 fingers up"). Draw it as original artwork; do not copy any character or show a face.
- [ ] 2026-10-16 Number Wizards: check the colours and formulas. Tom shared two Numberblocks reference images showing the colour convention schools use for 1 to 10: 1 red, 2 orange, 3 yellow, 4 green, 5 light blue, 6 purple, 7 rainbow, 8 magenta, 9 grey, 10 white with a red outline.
  - Note (not blocking): current `NUMCOL` matches except 6, which is indigo (#3949AB) and should be a clearer purple (try #8E24AA or #7E57C2, keeping contrast with 5 and 8 and checking dark mode). Use the colour convention only; no Numberblocks characters, faces or names in the app. "Formulas" means the number sentences and bonds: check every `say` text and bond (for example "Five and two more is seven"), block rows and totals for numbers 1 to 10, and the bonds to 5 and 10, then report anything wrong in the Done entry.
- [ ] 2026-10-16 Number Wizards fingers: FINAL DESIGN APPROVED by Tom ("ghost hands" with a full-hand fill). Replaces the bar-style `fingersSVG`. Supersedes the two options in the earlier fingers item above; do that item as part of this one.
  - Look: see `design/fingers/approved-ghost-hands-full-fill.png` (shows 3, 5, 8, 10). Reference drawing code (Python, rough): `design/fingers/hand_mockup.py`, option "B2". Port it into JS in `fingersSVG`.
  - Rules: one hand for 1 to 5, two hands for 6 to 10. Raised fingers are filled with the number's colour; folded fingers are hidden behind the palm (tucked in). The palm is white, EXCEPT when all five fingers are up: then the whole hand (palm too) fills with that colour. Fingers go up in the order index, middle, ring, little finger, then thumb last, so 4 is four fingers and 5 adds the thumb.
  - Colours: the first hand (for 6 to 10) is always the colour of 5 (blue); the second hand uses the colour of the extra amount (n minus 5), so 8 is a blue hand plus a yellow hand of three, 10 is two blue hands. For 1 to 5 use that number's colour (5 = blue, so a full hand fills blue). Use the corrected purple for 6 (see the colours item).
  - Keep the accessible label ("3 fingers up", "1 finger up"), dark-mode contrast (outline #272650 on light, a light outline on dark), and the sizing used by the existing hint line. Original artwork only: no faces, no Numberblocks characters. No skin tones, by design.

## Done
- 2026-10-16 UK English check (Tom: "ensure the app is UK English"). Scanned all visible text in the app, About page, changelog and word lists. Already UK English throughout (colours, coloured, recognising, maths, practise as a verb, practice as a noun). No changes needed. One thing noted for Tom: the "truck" picture word for ck is American; UK children often say "lorry" (a recording would be needed).
