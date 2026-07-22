# AGENTS Guide

This repository contains static resume templates. Keep changes simple, visual, and file-local.

## Project Snapshot
- Type: static HTML templates with embedded CSS.
- Tooling: no build, test, lint, or package manager setup.
- Main files:
  - `chinni_resume_variant2.html`
  - `jessika_generic_resume_self_contained.html`
  - `jessika_generic_resume_with_icons.html`
  - `jessika_resume.html`
  - `resume.html.html`

## How To Work Here
- Edit the target HTML file directly; styles live in each file's `<style>` block.
- Preserve existing layout patterns (grid main/sidebar, section cards, chip/pill elements).
- Prefer updating CSS variables in `:root` for theme changes before editing many selectors.
- Keep class names lowercase and hyphenated to match current style.
- If you change shared visual patterns, mirror updates across relevant variants.

## External Dependencies
- Fonts are loaded from Google Fonts via `<link>` in `<head>`.
- Icons are loaded from Font Awesome CDN.
- Do not remove CDN links unless you also remove their usage in markup/CSS.

## Validation Checklist
- Open edited file in a browser and verify desktop + mobile layout.
- Confirm icons and webfonts load correctly.
- Check print/PDF output (`Ctrl+P`) for page breaks and overflow.

## Known Pitfalls
- `resume.html.html` has a double extension; treat it as intentional unless asked to rename.
- Font Awesome version differs across files (6.5.1 vs 6.5.2); keep consistency if you touch icon sets.
- There is no centralized stylesheet, so cross-file consistency is manual.

## Useful Local Commands (Optional)
- Start quick static server from this folder:
  - `python -m http.server 8000`
- Then preview files at `http://localhost:8000/`.
