"""Create saved users with the same home directories and uids."""
import pwd
import os, sys
from subprocess import check_call
import json

fname = './saved_users.txt'

if not os.path.isfile(fname):
    print('No saved users found')
    sys.exit()

with open(fname, 'r') as f:
    users = json.loads(f.read())    

for username, uid in users:
    home_dir = os.path.abspath(os.path.join('.', username))
    try:
        udata = pwd.getpwnam(username)
    except KeyError:
        if os.path.isdir(home_dir):
            cmd = ['adduser', '-q', '--uid', str(uid),
                   '--no-create-home', '--home', home_dir,
                   '--gecos', '""', '--disabled-password', username]
        else:
            cmd = ['adduser', '-q', '--uid', str(uid),
                   '--home', home_dir,
                   '--gecos', '""', '--disabled-password', username]
        print('Creating user: {}'.format(' '.join(cmd)))
        try:
            check_call(cmd)
        except CalledProcessError:
            print('Error in creating user: {}'.format(' '.join(cmd)))
    else:
        if udata.pw_uid == uid and udata.pw_dir == home_dir:
            print('User already exists: {}'.format(username))
        else:
            print("User exists, but uid or home dir don't match", uid, udata.pw_uid, home_dir, udata.pw_dir)
