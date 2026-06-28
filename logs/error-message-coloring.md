# Error Message Coloring Feature

**Date:** 2026-06-28
**Status:** Complete

## Summary

Skulpt output now shows normal `print()` output in black and error messages in red.
This makes it immediately obvious to students when their program crashed vs. ran cleanly.

## What Changed

### `docs/css/skulpt.css`

- Changed the `color` on `[id="output"]` from `#c0392b` (red) to `#222` (near-black).
  Previously ALL output — including successful `print()` calls — appeared in red, which was a bug.
- Replaced a pre-element-level `.skulpt-error` class rule with a simple `.skulpt-error { color: #c0392b; }` rule
  that targets inline `<span>` elements, enabling per-line color without affecting surrounding text.

### `docs/js/skulpt.js`

- Added `_skulptEscape(text)` helper that HTML-encodes `&`, `<`, `>` so `print()` output is safe to inject via `innerHTML`.
- Switched all output clearing and writing from `textContent` to `innerHTML` (run, reset, and the output callback).
- Normal output is now appended as plain escaped HTML — appears black (inherits from the `<pre>`).
- Error messages are now **appended** (not replacing) as `<span class="skulpt-error">…</span>` — appears red.
  The old approach replaced all content with the error, destroying any print output that preceded the crash.

## Key Behavior

| Scenario | Output |
|----------|--------|
| Successful `print()` calls | Black text |
| Runtime error with no prior output | Red error message only |
| `print()` calls followed by a crash | Black lines, then red error appended below |

The interleaved case (black + red in the same output box) is what enables the debugging demo page.

## Demo Page

`docs/skulpt/10-debugging.md` — "Reading Output and Error Messages"

Three labs:
1. Clean program — all black output
2. Program that prints two lines then crashes on an undefined variable — black then red
3. Print-checkpoint debugging technique — students uncomment a broken line to watch where checkpoints stop

Added to `mkdocs.yml` nav under "Beginning Python - Skulpt (self-hosted)" as "Reading Errors".
