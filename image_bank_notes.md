# Image bank from TMBL Annual Report 2026 (116 pages, 26 substantial photos found)

All files in photos/ are extracted directly from annual-report-2026.pdf, at their
original embedded resolution (not the cropped versions used in finished slides).
Filename = pg<N>-000.png, where N is the PDF page number it came from.

## Already used in finished slides (crop logic documented in case you need to redo)
- pg41-000.png — slide 1 background (golden hills, soft sky). Cropped to a 16:9
  horizontal band, NOT stretched: full width, height = width/1.778, offset to show
  mostly sky at top, hills/treeline at bottom third.
- pg91-000.png — slide 14 background (mountain lake, pink sunrise). Cropped to
  5:5.625 portrait for a half-slide panel: full width, height = width/0.889.
- pg18-000.png, pg13-000.png, pg27-000.png — slide 4 rows 2–3 (desk meeting,
  aerial coastal road). Cropped to 1.5:1 landscape thumbnails.
- pg23-000.png — slide 4 row 1 (two women in conversation, research-interview
  feel). Swapped in to replace pg18 here specifically because it visually
  resembles primary research/interviews, which is what "customer journey maps"
  actually are.
- pg10-000.png, pg19-000.png, pg21-001.png — were used in an earlier slide 6
  card-grid draft (now replaced by a shape-built table on the user's request,
  so these three are currently unused, available for slides 7/11).

## Cataloged but not yet used, by theme
**Landscape/nature** (portrait source, crop to horizontal bands for full-bleed use):
pg1, pg2, pg4, pg5, pg34, pg35, pg40, pg89, pg90

**Member/staff interaction** (service, advisor, broker contexts):
pg9 (counter service), pg13 (already used)

**Community/social** (DIY, word-of-mouth, younger segments):
pg16, pg17-001, pg17-003, pg15

**Leadership headshots** (lower priority for this deck):
pg7-000, pg7-001

## Logos
- amb_logo_transparent.png — real AMB logo, colored (blue gradient leaf mark +
  dark text), background removed to transparent. Use on LIGHT backgrounds.
  Extracted and pixel-sampled directly from the annual report at 400dpi, this is
  the authentic logo, not a redrawn approximation.
- white_logo.png — the original white reversed logo already in the source deck.
  Use on DARK/navy backgrounds.

## Update: slides 2, 3, 5, 7, 8, 9, 10, 11, 12, 13
Used since the notes above (build scripts in build/, run build/run.sh to regenerate):
- pg16-000: slide 7 left photo (DIY). pg9-000: slide 7 right photo (broker). Navy lower-third ramp baked in.
- pg4-001, pg4-005, pg4-002 (small 258x141 originals): slide 11 medallions (20%, 55%, 15%), circle sizes scaled to budget share.
- pg1-000: slide 2 right-bleed strip. pg89-000: slide 3 "issue" card. pg34-000: slide 5 photo behind white stat card.
- pg18-000: slide 8 card header. pg10-000: slide 9 banner (shows a Ray White sign, consider swapping).
- Slide 4 redone in report-highlights style (pg5-000 tall photo right, pg23, pg13, pg27 rows).
- Slides 10, 12, 13 are photo-free (hairlines, accent rule, edge-bleed panel).
- pg21-001 is a greyscale mask, not a photo. Do not use.
- Still untouched: pg2, pg5, pg15, pg17-001/002/003, pg19, pg21-000, pg35, pg40, pg90, pg4-003/004, pg7.

## Update: makeover of slides 2, 6, 8, 9, 10, 11, 12, 13
- branding/ holds the three AMB files supplied by the user plus derived transparent versions (leaves, white logo, white mark, faint mark).
- Slide 2: leaf-pattern header band. Slide 8: pattern behind the two stats. Slide 9: faded pattern background, white logo on navy ribbon. Slide 10: white mark on ribbon. Slide 13: faint white mark watermark on the ROI panel.
- Slide 7 DIY photo is now pg13-000 (so slide 4 row 2 now uses pg4-003). pg16-000 is free again.
- Outbound requests to image sites are blocked in this sandbox, so no new images were downloaded.
