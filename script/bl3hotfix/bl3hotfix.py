#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

import re

# Classes and stuff to take GBX-provided hotfixes and turn them into objects
# that we can more easily deal with.  Mostly just used to generate my
# Combined Hotfixes sheets.

key_re = re.compile('^(.*?)(\d+)(\.(\w+))?$')
package_re = re.compile('^\((\d+),(\d+),(\d+),(.*?)\),(.*)$')
four_re = re.compile('^(\(\d+(,\d+)?\)),(\(\d+(,\d+)?\)),(\(\d+(,\d+)?\))$')
digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

class HotfixTypeNotSupported(Exception):
    """
    Custom exception for error handling
    """

class Hotfix(object):

    def __init__(self, key, value, filename, incorporated=False):

        global package_re
        global digits

        # These are convenience attrs for our routines which parse GBX hotfix
        # data, so we can track which hotfixes are active between historical
        # versions
        self.active = True
        self.first_seen = None
        self.last_seen = None
        self.incorporated = incorporated

        # Get key info
        self.set_key_values(key, filename)

        # Get package info
        match = package_re.match(value)
        if not match:
            raise Exception('Unknown value for key "{}" in {}'.format(
                key,
                filename,
                ))
        self.must_be_1 = int(match.group(1))
        self.subtype = int(match.group(2))
        self.notify = int(match.group(3))
        self.pkg_name = match.group(4)
        rest_hotfix = match.group(5)

        if self.must_be_1 != 1:
            raise Exception('First value in package tuple isn\'t 1: {} - key "{}"'.format(
                self.must_be_1,
                key,
                ))

        # Make sure we know how to process the subtype.
        if self.subtype not in {1, 2, 4, 5, 6, 7, 11}:
            raise Exception('Unknown subtype {} for key "{}"'.format(
                self.subtype,
                key,
                ))

        process_rest = True
        self.extra = ''
        self.seven_unknown_1 = ''
        self.seven_unknown_2 = ''
        self.seven_unknown_3 = ''
        self.seven_unknown_4 = ''
        self.four_unknown_int = ''
        self.four_unknown_tuple = ''
        self.five_unknown_int_1 = ''
        self.five_unknown_int_2 = ''
        self.five_unknown_int_3 = ''
        self.five_unknown_obj = ''
        if self.subtype == 1:

            # Subtype of 1 means we don't have an extra field
            (self.obj, self.attr, hf_from_len, rest_hotfix) = rest_hotfix.split(',', 3)

        elif self.subtype == 2 or self.subtype == 6:

            # These have an extra field before the attribute.
            # In Subtype of 2, it's editing a DataTable object, and the extra field is
            # the "key" within the table, seemingly.
            # In Subtype of 6, it seems to reference some other game object, not sure
            # what's up with that.

            (self.obj, self.extra, self.attr, hf_from_len, rest_hotfix) = rest_hotfix.split(',', 4)

        elif self.subtype == 4:

            # These are weird.

            process_rest = False
            (self.obj, self.four_unknown_int, self.extra, rest_hotfix) = rest_hotfix.split(',', 3)
            match = four_re.match(rest_hotfix)
            if not match:
                raise HotfixTypeNotSupported('Error processing hotfix subtype 4: {}'.format(rest_hotfix))
            self.four_unknown_tuple = match.group(1)
            self.from_val = match.group(2)
            self.to_val = match.group(3)
            self.attr = '{}, then {}'.format(
                    self.four_unknown_int,
                    self.four_unknown_tuple,
                    )

        elif self.subtype == 5:

            # These, too, are weird.

            process_rest = False
            (self.obj,
                    self.five_unknown_int_1,
                    self.extra,
                    self.five_unknown_int_2,
                    self.five_unknown_int_3,
                    self.five_unknown_obj) = rest_hotfix.split(',', 5)
            self.from_val = ''
            self.to_val = self.five_unknown_obj
            self.attr = '{}, then {}, then {}'.format(
                    self.five_unknown_int_1,
                    self.five_unknown_int_2,
                    self.five_unknown_int_3,
                    )

        elif self.subtype == 7:

            # This is the weirdest one, no real clue what to do with them
            process_rest = False
            (self.obj,
                    self.seven_unknown_1,
                    self.seven_unknown_2,
                    self.attr,
                    self.seven_unknown_3,
                    self.seven_unknown_4,
                    self.from_val,
                    self.to_val) = rest_hotfix.split(',', 7)
            self.extra = '{},{} then {},{}'.format(self.seven_unknown_1,
                    self.seven_unknown_2,
                    self.seven_unknown_3,
                    self.seven_unknown_4,
                    )

        elif self.subtype == 11:

            # Well, heck, they're all weird by this point.  Really
            # nearly all these vars should be "unknown"
            process_rest = False
            (self.obj,
                    self.attr,
                    self.eleven_unknown_1,
                    self.eleven_unknown_2,
                    self.eleven_unknown_3) = rest_hotfix.split(',', 4)
            self.extra = '{}, then {}'.format(self.eleven_unknown_1, self.eleven_unknown_2)
            self.from_val = ''
            self.to_val = self.eleven_unknown_3

        # If we have a sort-of "ordinary" hotfix, continue processing
        if process_rest:

            if hf_from_len == '':
                hf_from_len = '0'
            hf_from_len = int(hf_from_len)
            # Weird bit of manual finagling we have to do here, to account
            # for some string quotes
            if self.subtype == 6:
                hf_from_len += 2
            self.from_val = rest_hotfix[:hf_from_len]
            self.to_val = rest_hotfix[hf_from_len+1:]

    @staticmethod
    def from_json_obj(json_struct, filename, incorporated=False):
        return Hotfix(json_struct['key'], json_struct['value'], filename, incorporated)

    def set_key_values(self, key, filename):
        """
        Given the specified key, strip out the information contained therein.
        """
        global key_re
        if key is None:
            self.key = '-'
            self.key_operation = '-'
            self.key_num = 0
            self.key_extra = None
        else:
            match = key_re.match(key)
            if not match:
                raise Exception('Unknown key "{}" in {}'.format(key, filename))
            self.key = key
            self.key_operation = match.group(1)
            self.key_num = match.group(2)
            self.key_extra = match.group(4)

    def clear_from(self):
        """
        Clears out our `from` value so the hotfix always activates
        """
        # I'm only confident about this for subtypes 1, 2, and 6.
        if self.subtype in {1, 2, 6}:
            self.from_val = ''

    def to_wire_format(self):
        """
        Outputs a wire-formatted "value" for ourselves
        (Though NOTE: does *not* escape quotes...)
        """

        prefix = '({},{},{},{}),{}'.format(
                self.must_be_1,
                self.subtype,
                self.notify,
                self.pkg_name,
                self.obj,
                )

        if self.subtype == 1:

            suffix = '{},{},{},{}'.format(
                    self.attr,
                    len(self.from_val),
                    self.from_val,
                    self.to_val,
                    )

        elif self.subtype == 2 or self.subtype == 6:

            from_len = len(self.from_val)
            if self.subtype == 6:
                from_len -= 2

            suffix = '{},{},{},{},{}'.format(
                    self.extra,
                    self.attr,
                    from_len,
                    self.from_val,
                    self.to_val,
                    )

        elif self.subtype == 4:

            suffix = '{},{},{},{},{}'.format(
                    self.four_unknown_int,
                    self.attr,
                    self.four_unknown_tuple,
                    self.from_val,
                    self.to_val,
                    )

        elif self.subtype == 7:

            suffix = '{},{},{},{},{},{},{}'.format(
                    self.seven_unknown_1,
                    self.seven_unknown_2,
                    self.attr,
                    self.seven_unknown_3,
                    self.seven_unknown_4,
                    self.from_val,
                    self.to_val,
                    )

        elif self.subtype == 11:

            suffix = '{},{},{},{},{}'.format(
                    self.attr,
                    self.eleven_unknown_1,
                    self.eleven_unknown_2,
                    self.eleven_unknown_3,
                    )

        else:

            raise Exception('Unknown subtype: {}'.format(self.subtype))

        #return '{},{}'.format(prefix, suffix.replace('"', '\\"'))
        return '{},{}'.format(prefix, suffix)

