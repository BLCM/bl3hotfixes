#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import re
import csv
import json
import collections
from bl3hotfix.bl3hotfix import Hotfix, HotfixTypeNotSupported

hf_dir = '../point_in_time'
filename_combined = 'hotfixes_combined.csv'
filename_latest = 'hotfixes_latest.csv'

class HotfixFile(object):

    def __init__(self, filename, global_hotfixes):

        # The dict where we'll store our data.  Remember the order they came in.
        self.hotfixes = collections.OrderedDict()

        # Grab the timestamp from the filename
        match = re.match('^.*hotfixes_(\d{4})_(\d{2})_(\d{2})(_-_(\d{2})_(\d{2})_(\d{2}))?(_-_(.+))?\.json$', filename)
        if not match:
            raise Exception('Filename not understood: {}'.format(filename))

        if match.group(4):
            self.timestamp = '{}-{}-{} {}:{}'.format(
                    match.group(1), match.group(2), match.group(3),
                    match.group(5), match.group(6),
                    )
        else:
            self.timestamp = '{}-{}-{}'.format(
                    match.group(1), match.group(2), match.group(3),
                    )
        if match.group(7):
            self.label = match.group(8)
        else:
            self.label = None

        # Open and process the hotfix file
        self.seen_values = set()
        with open(filename) as df:
            micropatch = json.load(df)
            for hotfix in micropatch['parameters']:

                # This check only protects us against duplicate hotfixes within the same file
                if hotfix['value'] in self.hotfixes:
                    continue
                
                # Make sure we know we've seen this value in here
                self.seen_values.add(hotfix['value'])

                # This is where we check the global hotfix dict
                if hotfix['value'] in global_hotfixes:

                    global_hotfixes[hotfix['value']].active = True
                    global_hotfixes[hotfix['value']].last_seen = self.timestamp

                    # We should also update with the latest key that we've seen, since that
                    # might change from version to version.  We'll just store whatever the
                    # last-seen one was, I guess.  That seems the most useful, and IMO it's
                    # not worth trying to export historical information about that.
                    global_hotfixes[hotfix['value']].set_key_values(hotfix['key'], filename)

                else:

                    # Parse the hotfix
                    try:
                        hf = Hotfix.from_json_obj(hotfix, filename)
                        self.hotfixes[hotfix['value']] = hf
                        global_hotfixes[hotfix['value']] = hf
                        hf.first_seen = self.timestamp
                        hf.last_seen = self.timestamp
                    except HotfixTypeNotSupported as e:
                        print(str(e))
                        continue

                    # Just some debugging
                    if False:
                        if hf.key_type == 'SparkLevelPatchEntry' and hf.pkg_name == '':
                            print('Level patch without package name: {}, {}'.format(filename, hf.key))

            # Since we're dealing with global_hotfixes in here already anyway,
            # let's go ahead and deactivate global hotfixes which we haven't
            # seen locally right now, rather than out in the non-class loop
            old_values = set(global_hotfixes.keys()) - self.seen_values
            for value in old_values:
                global_hotfixes[value].active = False

def pluralize(label, suffix, count, singular_suffix=None):
    if count == 1:
        if singular_suffix:
            return '{}{}'.format(label, singular_suffix)
        else:
            return label
    else:
        return '{}{}'.format(label, suffix)

# Load all the files
files = []
global_hotfixes = collections.OrderedDict()
for filename in sorted(os.listdir(hf_dir)):
    if filename.endswith('.json') and filename != 'hotfixes_current.json':
        full_filename = os.path.join(hf_dir, filename)
        hf_file = HotfixFile(full_filename, global_hotfixes)
        files.append(hf_file)

        print('{}: {} {} added'.format(
            filename,
            len(hf_file.hotfixes),
            pluralize('hotfix', 'es', len(hf_file.hotfixes)),
            ))

def write_row(writer, hf, last_seen_file=None):
    if last_seen_file and hf.last_seen == last_seen_file.timestamp:
        last_seen = ''
    else:
        last_seen = hf.last_seen
    writer.writerow([
        hf.key_operation,
        hf.key,
        hf.active,
        hf.subtype,
        hf.notify,
        hf.pkg_name,
        hf.obj,
        hf.extra,
        hf.attr,
        hf.from_val,
        hf.to_val,
        hf.first_seen,
        last_seen,
        ])

# Write out our combined CSV
operations = set()
with open(filename_combined, 'w') as odf:

    writer = csv.writer(odf)
    writer.writerow([
        'operation',
        'latest_name',
        'active',
        'type',
        'notify',
        'package',
        'object',
        'variable',
        'attr',
        'from',
        'to',
        'first_seen',
        'last_seen',
        ])

    for hf in global_hotfixes.values():

        # Also, incidentally, keep track of all operations we see
        operations.add(hf.key_operation)

        # Do the writes
        write_row(writer, hf, last_seen_file=files[-1])

print('')
        
# Write out *just* our most recent set of hotfixes, too.  Easier to import
# into our nicer spreadsheet versions that way.
with open(filename_latest, 'w') as odf:
    writer = csv.writer(odf)
    for hf in files[-1].hotfixes.values():
        write_row(writer, hf)

# Reports
if True:
    print('Total of {} {} written to {}'.format(
        len(global_hotfixes),
        pluralize('hotfix', 'es', len(global_hotfixes)),
        filename_combined,
        ))
    print('{} {} written to {}'.format(
        len(files[-1].hotfixes),
        pluralize('hotfix', 'es', len(files[-1].hotfixes)),
        filename_latest,
        ))
    print('')

if True:
    print('Hotfix operations:')
    for operation in sorted(operations):
        print(' * {}'.format(operation))
    print('')
