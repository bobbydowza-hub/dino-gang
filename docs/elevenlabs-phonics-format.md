# ElevenLabs phonics paste format (Tom's working draft, 2026-10-18)

Status: **test format, still being played with** (not perfect). Tom's own test format for letter sounds in ElevenLabs (Eleven v4, his instant voice clone "Tommy D - Dino Master"). Saved for reference. Not yet used for any clip in the app. Keep Tom's own recordings of the letter sounds unless he approves generated ones.

Each sound is written as IPA between slashes, with `[pause]` tags and full stops between repeats, then `...` lines to separate clips. Tom's text, with two blank lines before each `...` as in the number script (agreed 2026-10-18) and the `/mm/` removed from the "m" line:

```
/s/[pause]/s/[pause]. [pause]/s/[pause]. [pause][pause][pause]


...


...


...
/m/[pause]/m/[pause]./m/[pause].[pause]


...


...


...
/t/[pause]/t/[pause]/t/[pause][pause][pause][pause]


...


...


...
/y/[pause]/y/[pause][pause]/y/[pause][pause]
```

## Notes
- The sound is repeated three times per clip, with different pauses after each repeat (this is deliberate in Tom's draft, as far as I can tell; the pattern differs per sound: `s` uses `. [pause]` between repeats, `t` has four pauses at the end, `y` uses double pauses).
- Two blank lines before each `...`, as in the number script. Still measure the gaps before cutting (see the dino-eleven-audio skill: the count must match exactly).
- Short prompts are less consistent in ElevenLabs (their v3 guide), and pure sounds tend to pick up an added "uh". Listen to every clip.
- Sources: ElevenLabs pronunciation docs (IPA in slashes for Eleven v4; phoneme tags only on eleven_flash_v2).
