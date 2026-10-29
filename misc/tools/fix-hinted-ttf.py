#!/usr/bin/env python
"""
Fixes up TrueType fonts after hinting them with ttfautohint.

Sets head.flags bit 3 ("force ppem to integer values"), which hinted fonts
should always have, so that Windows rounds PPEM values when rendering.
Same as `gftools fix-hinting`.

Usage: fix-hinted-ttf.py <font.ttf> ...  (fonts are modified in place)
"""
import sys
from fontTools.ttLib import TTFont

for path in sys.argv[1:]:
  font = TTFont(path, recalcBBoxes=False, recalcTimestamp=False)
  if "fpgm" not in font:
    sys.exit(f"{path}: not a hinted font (no fpgm table)")
  font["head"].flags |= 1 << 3
  font.save(path)
