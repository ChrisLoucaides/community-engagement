# Limit Break — Join Our Community (OBS Browser Source)

A brand-matched full-screen promo for the Smash Bros. Cyprus community, as a
single self-contained HTML file. The logo, Barlow Condensed subsets, and both
QR codes are embedded, so there are no external files, no CDN and no network
access needed at showtime.

| File | What it is |
| --- | --- |
| `join-our-community.html` | The finished scene. Point OBS at this one. |
| `scene.src.html` | Editable source template. |
| `build.py` | Regenerates `join-our-community.html` from the template + assets. |
| `assets/limit-break-logo.png` | Logo, shared with `transition-scenes-limit-break`. |
| `assets/fonts/BarlowCondensed-*.woff2` | Latin subsets, weights 700/800/900. |
| `assets/SmashCY Discord.png` | Discord invite QR code. |
| `assets/SmashCY Twitter (1).png` | X (Twitter) profile QR code. |
| `preview/join-our-community.png` | Still of the scene, straight out of the page at 1920×1080. |

## The composition

Built on the `limit-break-bgd` brand guidelines — cyan `#00D4FF` → magenta
`#EE00CC` on `#08081A`, display type in Barlow Condensed — and reuses the same
background treatment as `transition-scenes-limit-break`:

- **Background** — two blurred brand colour fields drifting and breathing, a
  centre glow, a drifting grid overlay, cyan scanlines, a vignette, and a
  sparse ember particle field.
- **Corner brackets** — cyan at the top, magenta at the bottom.
- **Logo + kicker** — small Limit Break mark, "SMASH BROS. CYPRUS" kicker in a
  cyan→magenta gradient.
- **Headline** — "JOIN OUR COMMUNITY" in the same top-lit gloss + travelling
  shine treatment as the hold scenes.
- **QR cards** — two cards side by side, each with a glowing gradient-brand
  border (cyan for Discord, magenta for X/Twitter), a full white quiet zone
  around the QR so it stays scannable, and a label + caption underneath.

Everything fades and rises in over the first ~2s on load; motion stays out of
the QR cards themselves so they hold rock-steady on screen.

## OBS setup

1. `Sources` → `+` → **Browser**.
2. **Local file** — tick it, and pick `join-our-community.html`.
3. **Width / Height** — `1920` × `1080` (match your canvas).
4. **Use custom frame rate** — 60 if your stream is 60fps, otherwise leave it.
5. **Shutdown source when not visible** — tick it, to free the GPU while the
   scene is off screen.
6. **Refresh browser when scene becomes active** — tick it, so the intro
   animation replays every time you cut to it.

The page is opaque, so nothing behind it in the scene shows through.

Sizing is resolution-independent: every measurement is in `rem`, and `1rem` is
pinned to the smaller of 1/192 viewport width and 1/108 viewport height. A
1920×1080 source gives `1rem = 10px`; any other size scales the whole
composition to match.

## Options (query string)

The **Local file** picker can't take `?...` on the end — it's a file chooser.
To use these, untick **Local file** and put a full URL in the **URL** field
instead (forward slashes):

```
file:///C:/Users/Christos/Documents/ELS/TournamentStreamHelper-5.971/layout/community-engagement/join-our-community.html?particles=140
```

Refresh the browser cache after changing it.

| Param | Default | Meaning |
| --- | --- | --- |
| `particles` | `70` | Ember count, 0–400. `0` turns the field off. |
| `seek` | – | Freezes the whole scene at a given millisecond, e.g. `?seek=4200`. Used to render `preview/`; also handy for grabbing a thumbnail still. |

## Updating the QR codes or wording

1. Drop new QR images into `assets/`, keeping the filenames (or update the
   paths in `build.py`).
2. Edit the headline, kicker, or card labels/captions directly in
   `scene.src.html`.
3. Re-run:

```
python build.py
```

To regenerate the preview still (needs Chrome):

```
chrome --headless=new --window-size=1920,1080 --virtual-time-budget=6000 ^
  --screenshot=preview/join-our-community.png ^
  "file:///.../join-our-community.html?seek=4200"
```

`seek` exists because CSS animations don't advance under Chrome's
`--virtual-time-budget` — without it a headless screenshot catches the page at
frame zero, with everything still faded out.
