#!/usr/bin/env/python3
# Created by SaxDev

# Exercise file naming conventions:
# category_note_[parameter_parameter]
# Examples:
# longTone_G
# majorScale_F_2octaves
# minorScale_db_harmonic_thirds_fullrange

import mingus.core.notes as notes
from mingus.containers import NoteContainer
from mingus.containers import Bar
import mingus.extra



def longTone(n):
    b = Bar(key=n, meter=(4, 4))
    b.place_notes(n, 1.0)
    mingus.extra.lilypond.from_Bar(b)
    mingus.extra.lilypond.to_png(b, "firstTest")



