Configuring nbgrader
====================

The nbgrader package will be installed with the reference deployment.

To run nbgrader's formgrade application or use its notebook
extensions, additional steps are needed.

Deploy formgrade
----------------

First, edit the :file:`deploy_formgrade.yml` file with the information
for each course you want to start formgrade for. Each course should have a 
unique `nbgrader_course_id` and `nbgrader_port`.

Second, make sure that each main instructor (the `nbgrader_owner` for each
course) has logged into JuptyerHub at least once. This ensures that their
home directory has been created. The home directory of the main instructor
is used for the main nbgrader course files. It is assumed that the main
instructor will be running the nbgrader command line programs.

Third, run the ansible-playbook to deploy formgrade::

	$ ansible-playbook deploy_formgrade.yml

Fourth, SSH into the JupyterHub server::

    $ ssh {user}@{hostname}

Finally, restart jupyterhub and nbgrader by doing::

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
