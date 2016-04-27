"""Save usernames and uids."""

import pwd
import os
import json

data = []
users = pwd.getpwall()
for user in users:
    username = user.pw_name
    uid = user.pw_uid
    home_dir = os.path.abspath(os.path.join('.', username))
    if os.path.isdir(home_dir) and home_dir == user.pw_dir:
        data.append((username, uid))
        print("Saving user: {}:{}".format(username, uid))

with open('./saved_users.txt', 'w') as f:
    json.dump(data, f)
