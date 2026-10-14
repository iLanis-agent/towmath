# Tow math

The ad names the trailer, the sticker names the payload, and the tongue names the margin.

The tow rating in the ad belongs to a truck with a driver and nothing else. The number that runs out first is usually payload - and the trailer's tongue spends 10-15% of the loaded trailer against it before anyone climbs in.

## The three tools

- **Tongue plan** - the loaded trailer becomes the honest 10-15% tongue band, rounded to the nearest 5 lb.
- **Payload plan** - sticker minus people, cargo and tongue, judged unrounded: margin or the honest over-the-sticker shortfall.
- **Brake plan** - the trailer weight against a labeled 3,000 lb common brake-requirement line, with a named gray zone below it and a "check your state" on every answer.

## Honesty notes

Illustrative planning arithmetic only. Tongue percentages and brake lines are labeled norms; brake laws differ by state and your manual's limits can be stricter. The lowest rating in the chain (truck, hitch, ball, coupler) is the limit. Distribute the load, check the lights, and if sway starts, slow down gently - do not brake hard.

## Files

- `index.html` - the pitch
- `app.html` - the calculators
- `engine.js` - the arithmetic (browser and node)
- `oracle.py` - the same arithmetic, float-for-float, writing `expected.json`
- `test.js` - runs every case in `expected.json` through `engine.js` and compares results and renders exactly

Run the check:

```
python3 oracle.py && node test.js
```
