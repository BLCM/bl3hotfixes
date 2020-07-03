#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import re
import subprocess

# Extracts hotfix-lookin' things from the Mac BL3 binary.  This has the
# possibility to give us some bad data, I suppose, since it doesn't actually
# understand the file structure, but it turns out to be *better* than
# extracting via Ghidra decompilations, 'cause Ghidra's got a hardcoded max
# string limit, which ends up truncating longer hotfixes.  (My automated
# Ghidra-decompilation script doesn't actually even *notice* these truncated
# hotfixes, thanks to the comment Ghidra puts after 'em.)  So, we'll just
# do this for now.

filename = '/home/pez/legendary/Borderlands3/OakGame/Binaries/Mac/Borderlands3.app/Contents/MacOS/Borderlands3'
output = 'fixup_hotfixes.txt'
hotfix_re = re.compile(r'^\(\d+,\d+,\d+,\w*\),/.*$')

# this requires py3.7
seen = set()
cp = subprocess.run(['/usr/bin/strings', '-e', 'B', filename], capture_output=True, encoding='utf8')
with open(output, 'w') as df:
    for line in cp.stdout.split("\n"):
        match = hotfix_re.match(line)
        if match:
            if line not in seen:
                seen.add(line)
                print(line, file=df)
print('Wrote {} hotfixes to {}'.format(len(seen), output))
