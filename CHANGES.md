# Dino Gang change list

Tom adds items with `/change-dino: <what to change>`. A scheduled run applies them to the `dev` branch twice a day (about 08:00 and 18:00 UK time). Nothing here goes live until Tom says "release".

## Rules for whoever applies this list (a scheduled run or a live session)
1. Work only on the `dev` branch. Never push to `main`, never merge to `main`, never open a pull request. Every push to `main` spends Netlify deploy credits.
2. Only act on items under **Pending**. Skip anything marked `NEEDS TOM`.
3. Apply each item in `src/` (and `public/` where needed), run `python3 tools/build.py`, check it (open it in Playwright at phone width, or grep/diff for text changes), then commit to `dev` with a message naming the item.
4. Move each finished item to **Done** with the date and a one-line result. If an item is unclear, risky, or would make something worse, leave it in Pending, mark it `NEEDS TOM` and say why. Do not guess.
5. If there are no Pending items, change nothing and finish quickly.
6. Do not edit audio, the Spanish or Portuguese wording, or the A5 PDF unless the item says to.
7. Push `dev` (free) and finish with a short summary: what changed, what needs Tom's decision. The summary is for Tom to read; keep it brief.

## Pending
- [ ] 2026-10-15 UK English spelling. Tom's words: "practise" needs to change to "practice".
  - NEEDS TOM: in UK English "practise" is the verb and "practice" is the noun. The app currently says "practise ten cards" and "Practise again", which are both correct UK English. Changing them to "practice" would make them US-style. Check Tom's meaning before changing. Meanwhile, a full scan for genuine US spellings (color, favorite, center, etc.) is safe to run and report.
- [ ] 2026-10-16 We need a mechanism to toggle the additional words we have added. Little Wandle wall charts and course material only focus on the original A1 and A2 words and sounds. Our additions (the 39 extra picture words) were to build out bulk, but are not explicitly used by the school or Little Wandle.
  - Tom confirmed 2026-10-16: extras OFF by default. Details: so the app matches Little Wandle out of the box, with a "Little Wandle words only / Add extra picture words" toggle on the Word Wizards screen beside Letter first / Word first, saved in prefs. With extras off, Word first still works using each card's original keyword. Also mention it on the About page and in the changelog.

## Done
