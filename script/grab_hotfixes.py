#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import sys
import git
import json
import appdirs
import requests
import datetime

hotfix_url = 'https://discovery.services.gearboxsoftware.com/v2/client/epic/pc/oak/verification'
output_dir = '/home/pez/git/b2patching/bl3hotfixes'

# Get our cache dir, and create if it doesn't exist
cache_dir = appdirs.user_cache_dir('bl3hotfixes', 'Apocalyptech')
if not os.path.isdir(cache_dir):
    os.makedirs(cache_dir)
if not os.path.isdir(cache_dir):
    raise Exception('Couldn\'t create cache dir: {}'.format(cache_dir))

# Get our current hotfix data, if we can
hotfix_cache = os.path.join(cache_dir, 'hotfixes.json')
cur_hotfixes = None
if os.path.exists(hotfix_cache):
    with open(hotfix_cache) as df:
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
    raise Exception('Could not find hotfixes!')

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

# Do the write, if we have to
if do_write:

    # First write the new file to the cache
    print('Writing new hotfix cache to {}'.format(hotfix_cache))
    with open(hotfix_cache, 'w') as df:
        df.write(hotfixes)

    # Now also write out the hotfixes to a new repo file
    now = datetime.datetime.utcnow()
    hotfix_filename = now.strftime('hotfixes_%Y_%m_%d_-_%H_%M_%S.json')
    print('Writing new hotfixes to {}'.format(hotfix_filename))
    with open(os.path.join(output_dir, hotfix_filename), 'w') as df:
        df.write(hotfixes)

    # Do the git interaction
    print('Pushing to git')
    repo = git.Repo(output_dir)
    repo.git.add('--', hotfix_filename)
    repo.git.commit('-a', '-m', 'Auto-update with new hotfixes')
    repo.git.push()
