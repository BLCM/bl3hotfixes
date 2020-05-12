# Hotfix-Processing Scripts

## `grab_hotfixes.py`

This is the utility which is used to check for EGS+Steam hotfixes and
update this repo as-needed.  It currently runs at 10 after the hour via
cron, on a local box of mine.  It populates the main
`hotfixes_current.json` file in the main dir, and also an individual file
inside `point_in_time`.

It tries to do the right thing when EGS and Steam hotfixes diverge -- so
far, we've only seen that when the Steam hotfix updates lag behind the EGS
updates by some tens of minutes, though they seem to have more or less
straightened out their workflow for updating those, because we haven't seen
that in awhile now.  Currently the EGS hotfixes are considered the "main"
hotfixes, and Steam is compared against those.

`requirements.txt` lists the Python dependencies required to run this util.

## `convert_to_csv.py`

This is my script which pulls all the hotfix info from the main
`point_in_time` directory into a CSV/spreadsheet, which ends up
[living online at Google Sheets](https://drive.google.com/open?id=1kfkC2hJs0hZSr12bvrQlY0GyEH4S_KAI_xIAqnGmKnQ).

It also processes the file `fixup_hotfixes.txt`, which contains hotfixes
which have been pulled into the main game binary directly.  That text file
is currently not auto-generated at all, really.  It's created just by
manually copy+pasting the various `Fixup*` functions found via Ghidra into
local files, and then pulling out anything that looks like a hotfix.  At
some point I may at least write a Ghidra plugin or something to automate
the copying-into-files bits.

The `incorporated` column on the generated CSV means that a hotfix
previously found in one of our `point_in_time` files has been pulled in
directly to the binary, but the *absence* of an `incorporated` hit doesn't
mean that the hotfix's effects haven't been pulled in.  For instance, some
sniper rifle buffs were added in to a hotfix very early on in BL3's
lifecycle, and were pulled into the game binary in March 2020.  Unlike many
of the other incorporated hotfixes, though, they didn't just move it in
wholesale.  Rather, they had some code to go alter the related DataTable
entries directly.

## `csv_investigate.py`

Just a bit of datamining that I was doing against hotfix sets, back when we
were still trying to figure out the new hotfix syntax.  I occasionally
break this out again when I want to do some aggregate data introspection.
