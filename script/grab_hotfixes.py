#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Borderlands 3 Hotfix Monitor (grab_hotfixes.py)
# Copyright (C) 2019 CJ Kucera
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the development team nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL CJ KUCERA BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import re
import sys
import git
import json
import appdirs
import requests
import datetime

# The format marker in here will be filled in by `stores`, below
hotfix_url = 'https://discovery.services.gearboxsoftware.com/v2/client/{}/pc/oak/verification'
cache_base_file = 'hotfixes-{}.json'
output_dir = '/home/pez/git/b2patching/bl3hotfixes'
#output_dir = '/home/cj/git/bl3/bl3hotfixes'
point_in_time_base = 'point_in_time'
point_in_time_dir = os.path.join(output_dir, point_in_time_base)
current_file = 'hotfixes_current.json'

# We're supporting multiple stores' hotfixes now.  Keep in mind that the *first*
# one will be considered the "master."  That's what'll be put into the "current"
# hotfix file, and the one put into the point-in-time dir without any store-
# specific suffix.  All other stores' hotfixes will only be written out as
# point-in-time hotfixes if they differ from the first one.
stores = ['epic', 'steam']

def get_hotfix(store, hotfix_url, cache_file):
    """
    Routine to grab hotfixes in the format we want, given a hotfix URL.  Returns
    a tuple containing the store name, hotfix data, and a boolean specifying
    whether or not the new hotfix data should be written out to the "live"
    location.  (The cache file will be updated automatically.)  The store name
    is basically just passed through from the argument, for convenience.
    """

    # Get our current hotfix data, if we can
    cur_hotfixes = None
    if os.path.exists(cache_file):
        with open(cache_file) as df:
            cur_hotfixes = df.read()

    # Grab hotfixes (and other data) from server
    r = requests.get(hotfix_url)
    verification = json.loads(r.text)

    # Loop through to find 'Micropatch', which is the one we want
    hotfixes_new = None
    for service in verification['services']:
        if service['service_name'] == 'Micropatch':
            hotfixes_new = service
            break

    # If we didn't get hotfixes, error.
    if not hotfixes_new:
        raise Exception('Could not find hotfixes in {}'.format(hotfix_url))

    # Format them
    hotfixes = json.dumps(hotfixes_new, indent='  ')

    # Check to see if we need to write out a new hotfix file
    do_write = False
    if cur_hotfixes:
        if hotfixes != cur_hotfixes:
            #print('Hotfixes have changed')
            do_write = True
        else:
            #print('Hotfixes are unchanged')
            pass
    else:
        #print('No original hotfixes')
        do_write = True

    # Write the new file to our cache
    if do_write:
        print('Writing new hotfix cache to {}'.format(cache_file))
        with open(cache_file, 'w') as df:
            df.write(hotfixes)

    # ... and return
    return (store, hotfixes, do_write)

# Get our cache dir, and create if it doesn't exist
cache_dir = appdirs.user_cache_dir('bl3hotfixes', 'Apocalyptech')
if not os.path.isdir(cache_dir):
    os.makedirs(cache_dir)
if not os.path.isdir(cache_dir):
    raise Exception('Couldn\'t create cache dir: {}'.format(cache_dir))

# Read in hotfixes
hotfixes = []
for store in stores:
    hotfixes.append(get_hotfix(
        store,
        hotfix_url.format(store),
        os.path.join(cache_dir, cache_base_file.format(store)),
        ))

# Process our "main" hotfix, if we have to
do_git = False
now = datetime.datetime.utcnow()
(main_store, main_hotfixes, main_do_write) = hotfixes[0]
if main_do_write:

    # We're definitely adding new files
    do_git = True

    # Now also write out the hotfixes to a new repo file
    hotfix_filename = now.strftime('hotfixes_%Y_%m_%d_-_%H_%M_%S.json')
    print('Writing new {} hotfixes to {}'.format(main_store, hotfix_filename))
    with open(os.path.join(point_in_time_dir, hotfix_filename), 'w') as df:
        df.write(main_hotfixes)

    # Now write to our 'current' file
    print('Writing new {} hotfixes to {}'.format(main_store, current_file))
    with open(os.path.join(output_dir, current_file), 'w') as df:
        df.write(main_hotfixes)

# Now process any othe stores' hotfixes
extra_files = []
for (other_store, other_hotfixes, other_do_write) in hotfixes[1:]:
    if main_hotfixes != other_hotfixes:

        if other_do_write:
            other_filename = now.strftime('hotfixes_%Y_%m_%d_-_%H_%M_%S_-_{}.json'.format(other_store))
            print('Writing new {} hotfixes to {}'.format(other_store, other_filename))
            with open(os.path.join(point_in_time_dir, other_filename), 'w') as df:
                df.write(other_hotfixes)

            # Hotfixes differ!  We'll write out a point-in-time for this,
            # though in the event that this store hasn't changed, we'll
            # write out a text file instead of JSON.
            do_git = True
        else:
            # Really stupid check against writing repeated hotfix-diversion notifications out there.  GBX
            # seems to be doing it a lot lately and we end up with hourly notifications.  This check would
            # fall apart if we ever have more than just egs + steam to check.
            last_dirent = list(sorted(os.scandir(point_in_time_dir), key=lambda d: d.stat().st_mtime))[-1]
            if re.match(f'^hotfixes_\d+_\d+_\d+_-_\d+_\d+_\d+_-_{other_store}(.*_difference_notice)?.txt$', last_dirent.name):
                # Actually, I don't even want to get notified about it
                #print(f'Found a previous {other_store} no-change notification, not writing out another')
                continue
            else:
                other_filename = now.strftime('hotfixes_%Y_%m_%d_-_%H_%M_%S_-_{}.txt'.format(other_store))
                print('Writing {} no-change notification to {}'.format(other_store, other_filename))
                with open(os.path.join(point_in_time_dir, other_filename), 'w') as df:
                    print('{} hotfixes have not changed since the last update, though'.format(other_store), file=df)
                    print('they now differ from the {} hotfixes'.format(main_store), file=df)

                # Hotfixes differ!  We'll write out a point-in-time for this,
                # though in the event that this store hasn't changed, we'll
                # write out a text file instead of JSON.
                do_git = True

        # Add this to our list of files
        extra_files.append(other_filename)

# Do the git interaction, if anything was written
if do_git:
    print('Pushing to git')
    repo = git.Repo(output_dir)
    repo.git.pull()
    if main_do_write:
        repo.git.add('--', os.path.join(point_in_time_base, hotfix_filename))
        repo.git.add('--', current_file)
    for extra_file in extra_files:
        repo.git.add('--', os.path.join(point_in_time_base, extra_file))
    repo.git.commit('-a', '-m', now.strftime('Auto-update with new hotfixes - %Y-%m-%d %H:%M:%S'))
    repo.git.push()

