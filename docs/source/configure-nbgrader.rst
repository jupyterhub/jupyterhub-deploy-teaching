Configuring nbgrader
====================

The nbgrader package will be installed with the reference deployment.

To run nbgrader's formgrade application or use its notebook
extensions, additional steps are needed.

Configuring the extension
-------------------------
Each user who wants to use the notebook extension will need to run::

    $ nbgrader extension activate

Deploy formgrade
----------------
Log into JupyterHub as the main instructor (`nbgrader_owner`).

Run the ansible-playbook to deploy formgrade::

	$ ansible-playbook deploy_formgrade.yml

SSH into the server::

    $ ssh {user}@{hostname}

Restart jupyterhub and nbgrader by doing::

    $ supervisorctl reload


Configuration notes
-------------------

* To limit the deployment to certain hosts, add the ``-l hostname`` to the
  commands::

    $ ansible-playbook -l hostname deploy.yml

* The logs for `jupyterhub` are in :file:`/var/log/jupyterhub`.
* The logs for `nbgrader` are in :file:`/var/log/nbgrader`.
* If you are not using GitHub OAuth, you will need to manually create users using
  `adduser`::

    $ adduser --gecos "" username

* Change the ansible configuration by editing :file:`./ansible_cfg`.
* To manage the jupyterhub and nbgrader services by SSH to the server and run::

    $ supervisorctl jupyterhub { start, stop, restart }

Troubleshooting: Saving and restoring users
-------------------------------------------

In some situations, you may remount your user's home directories into a new instance that
doesn't have their user accounts, but has their home directories. When recreating the
same users it is important that they all have the same uids so the new users have
ownership of the home directories.

**This is only relevant when using GitHub OAuth for users and authentication.**

To save the list of usernames and uids in `{{homedir}}/saved_users.txt`::

    $ ansible-playbook saveusers.yml

Then, when you run deploy.yml, it will look for this file and if it exists, will create
those users with those exact uids and home directories.

You can also manually create the users by running::

	$ python3 create_users.py

in the home directory.
