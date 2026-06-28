# Textarea Auto-Height Fix: scrollHeight Approach

**Date:** 2026-06-28  
**Files changed:** `docs/js/skulpt.js`, `docs/css/skulpt.css`, `CONTENT-GENERATION-GUIDELINES.md`

---

## Problem

All Skulpt lab textareas had a fixed `height: 260px` set in CSS. Short programs
(3–5 lines) had too much empty space; long programs (20+ lines) required scrolling.
A first attempt at auto-sizing used a line-count formula (`lineCount × 22 + 24 px`)
but still left several blank rows at the bottom of the textarea for programs like
the 27-line stop-sign example.

Two bugs combined to cause the over-sizing:

1. **Trailing newline inflation** — every textarea in the markdown source has a
   `\n` immediately before `</textarea>`. `value.split('\n')` counts this as an
   extra empty line, inflating the calculated height by one full line-height.

2. **Incorrect line-height estimate** — the formula assumed 22 px per line, but
   the browser renders Courier New at 14 px with an actual line-height of roughly
   17–18 px. The 4 px over-estimate per line compounded across 27 lines produced
   ~108 px of extra blank space (≈ 6 blank rows).

---

## Solution

Replace the manual formula with `scrollHeight`, which lets the browser measure
the exact pixel height of the textarea content at its actual font metrics.

### Step 1 — Strip trailing newlines before measuring

```javascript
var saved = code.value;
code.value = code.value.replace(/\n+$/, '');  // remove trailing blank line(s)
```

The original value is saved and restored immediately after measurement so the
**Reset** button still works correctly.

### Step 2 — Collapse the textarea and read scrollHeight

```javascript
code.style.height = '0px';
code.style.height = Math.max(120, code.scrollHeight + 4) + 'px';
code.value = saved;
```

- Setting `height: 0px` (inline style, overrides CSS) forces the browser to
  make all content overflow, so `scrollHeight` reflects the full content height.
- `scrollHeight` returns **content height + padding** but does **not** include
  borders. Adding `+4` compensates for the 2 px top + 2 px bottom border under
  `box-sizing: border-box`.
- `Math.max(120, ...)` guarantees a minimum height of 120 px for very short
  programs (1–4 lines).

### Step 3 — Remove fixed height from CSS

`skulpt.css` was changed from `height: 260px` to `min-height: 120px`. The CSS
minimum acts as a fallback if JavaScript is slow or unavailable; the JS inline
style always takes over and sets the exact height.

---

## Result

| Program | Lines | Old height | New height (approx) |
|---------|-------|-----------|---------------------|
| Hello World (3 lines) | 3 | 260 px | 120 px (min) |
| Simple square (9 lines) | 9 | 260 px | ~182 px |
| Stop sign (27 lines) | 27 | 260 px | ~510 px |
| Colored square (18 lines) | 18 | 260 px | ~346 px |

The textarea now fits exactly the initial code with no blank rows, no scrollbar,
and students can still drag the resize handle to expand it if they add more lines.

---

## Why scrollHeight is better than a formula

| Approach | Handles wrapping? | Accurate line-height? | Trailing-newline safe? |
|----------|------------------|----------------------|----------------------|
| `lineCount × 22 + 24` | No | No (estimate) | No |
| `scrollHeight` (trimmed) | Yes | Yes (browser measures) | Yes (trimmed before read) |

The `scrollHeight` approach is immune to font changes, browser zoom differences,
and long lines that wrap inside the textarea — all cases where a px-per-line
formula would give the wrong answer.
