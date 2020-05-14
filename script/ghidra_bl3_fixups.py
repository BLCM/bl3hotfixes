#Generates decompilations of Fixup* routines for BL3
#@author apocalyptech
#@category Apocalyptech
#@keybinding 
#@menupath Apocalyptech.BL3 Fixup Extractor
#@toolbar

from __future__ import print_function
import os
import re
import datetime

# May need to adjust this timeout to suit.  This value is good enough for me.
# The biggest one is FixupOnCharacterLoad; nearly all the rest would be okay
# with a much smaller timeout.
decompile_timeout = 360

# This should be fine as-is; all but FixupOnCharacterLoad are fine with the
# default of 50MB, but up to 400MB is too small.  (Didn't try 500.)
max_payload_size = 600

# Adjust to suit, of course.
output_dir = '/home/pez/git/b2patching/bl3hotfixes/script/ghidra'

# Adjust to suit, of course.
hotfix_file = 'fixup_hotfixes.txt'

func_re = re.compile(r'[a-zA-Z0-9]\(\);$')

def decompile_func(di, func):
    """
    Given the DecompInterface `di` and the Function `func`, decompile it,
    save its decompilation to disk, and loop through the decompilation
    looking for more fixup-related functions to also decompile.  Will
    return a set of all extra functions that were found.
    """
    global func_re
    global monitor
    global output_dir
    global decompile_timeout
    extra_funcs = set()
    print(' - {}...'.format(func.getName()))
    res = di.decompileFunction(func, decompile_timeout, monitor)
    if res.decompileCompleted():
        decompiled = res.getDecompiledFunction()
        with open(os.path.join(output_dir, '{}.cpp'.format(func.getName())), 'w') as df:
            code = decompiled.getC()
            df.write(code)

            # Search for extra functions that this func links to.
            # I can't imagine there's not a *much* more elegant way to do this,
            # but whatever.
            for line in code.split("\n"):
                match = func_re.search(line)
                if match:
                    stripped = line.strip()
                    if '__' in line \
                            or 'LOCK' in line \
                            or ' = ' in line \
                            or '/*' in line \
                            or 'Quaternion' in line \
                            or 'Create()' in line \
                            or 'StaticClass' in line \
                            or 'ToString' in line \
                            or stripped.lower().startswith('fixup'):
                        continue
                    extra_funcs.add(stripped[:-3].encode('latin1'))
    else:
        print('   ERROR: Could not decompile function: {}'.format(res.getErrorMessage().strip()))
    return extra_funcs

# Report on start
print('Starting on: {}'.format(datetime.datetime.now()))

# Create our output dir if it doesn't already exist
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Create a decompilation interface
di = ghidra.app.decompiler.DecompInterface()
options = di.getOptions()
if not options:
    options = ghidra.app.decompiler.DecompileOptions()
options.setMaxPayloadMBytes(max_payload_size)
di.setOptions(options)
di.openProgram(currentProgram)

# Loop through functions to create an initial set of functions to
# decompile.
print('Finding initial Fixup functions...')
funcset = set()
func = getFirstFunction()
while func:
    if func.getName().lower().startswith('fixup'):
        funcset.add(func.getName())
    func = getFunctionAfter(func)

# Now keep looping through our "funcset" until it's empty;
# each run through the function list might add more.  This seems
# awfully inefficient, but I couldn't find any "get function(s)
# by name" function, so this multi-runthrough will have to do.
# (Actually, I lie: there *is* a `getFunction(str)` available,
# but it's marked as deprecated since functions aren't necessarily
# uniquely-named, thanks to namespaces.  I wasn't able to find
# anything that'd, like, return a list of *all* functions matching
# a given name, though.)  I suppose I could've just created a dict
# when creating that initial list...
decompiled = set()
proc_round = 1
while len(funcset) > 0:
    print('Processing functions, round {}...'.format(proc_round))
    funcset_copy = funcset.copy()
    func = getFirstFunction()
    while func:
        if func.getName() in funcset:
            funcset.remove(func.getName())
            if func.getName() not in decompiled:
                decompiled.add(func.getName())
                funcset |= decompile_func(di, func)
        func = getFunctionAfter(func)
    proc_round += 1
    # Guard against an infinite loop
    if funcset == funcset_copy:
        print('ERROR: Aborting run, funcset remanied unchanged: {}'.format(funcset))
        break

print('Finished processing hotfixes after {} round(s) at: {}'.format(proc_round-1, datetime.datetime.now()))

# Now go ahead and generate our hotfixes file
print('Generating extracted-hotfix file...')
output_hotfixes = []
for filename in os.listdir(output_dir):
    if filename.endswith('.cpp'):
        full_file = os.path.join(output_dir, filename)
        with open(full_file) as df:
            for line in df:
                line = line.strip()
                if line.startswith('L"(') and line.endswith('"'):
                    output_hotfixes.append(line[2:-1].replace('\\"', '"').replace('\\\'', '\''))
with open(os.path.join(output_dir, hotfix_file), 'w') as odf:
    for hotfix in sorted(output_hotfixes):
        print(hotfix, file=odf)

# Done!
print('Done!')

