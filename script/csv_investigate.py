#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

import re
import csv
import sys

num_re = re.compile('.*_(\d+)$')

with open('hotfixes_combined.csv', 'rt') as df:
    reader = csv.DictReader(df)
    for row in reader:
        if row['type'] == '1' or row['type'] == '2':

            # Unrelated: does any underscore'd number end in 0?
            if False:
                match = num_re.match(row['object'])
                if match:
                    if match.group(1) == '0':
                        print(row['object'])

            # Check to see what kind of 'detail' object names don't match the base object name
            if False:
                lastbit = row['object'].split('/')[-1]
                if ':' in lastbit:
                    (lastbit, fancy) = lastbit.split(':')
                else:
                    fancy = None
                (base_obj, detail_obj) = lastbit.split('.')
                if (detail_obj != base_obj
                        and detail_obj != 'Default__{}'.format(base_obj)
                        and detail_obj != 'Default__{}_C'.format(base_obj)
                        and detail_obj != '{}_C'.format(base_obj)):
                    print(row['object'])

            # Find after-colon bits which have more than one dot
            if False:
                lastbit = row['object'].split('/')[-1]
                if 'PersistentLevel' not in row['object'] and ':' in lastbit:
                    (lastbit, fancy) = lastbit.split(':')
                    fancyparts = fancy.split('.')
                    if len(fancyparts) > 2:
                        print(row['object'])

            # Find challenge components
            if False:
                if 'CrewChallengeComponent' in row['object']:
                    print('{} - {} - {}'.format(
                        row['object'],
                        row['attr'],
                        row['package'],
                        ))

            # Finding Default__*:Foo hotfixes which use object-redirection in the attr field
            if True:
                if 'Default__' in row['object'] and ':' in row['object'] and '..' in row['attr']:
                    print('{} - {} - {} - {}'.format(
                        row['object'],
                        row['attr'],
                        row['from'],
                        row['to'],
                        ))

            # Finding hotfixes which have more than one `Default__` (which, I think, don't actually exist)
            # (this actually morphed to just look for `Default` in the second part, 'cause I was right...
            if False:
                parts = row['object'].split('Default__')
                if len(parts) > 1:
                    if 'Default' in parts[-1]:
                        print(row['object'])

        elif row['type'] == '6':

            # Looking into type 6 data
            if False:
                print(row['from'])
                data = row['from'][1:-1]
                for idx, triple in enumerate(data.split('|')):
                    nums = [float(n) for n in triple.split(',')]

