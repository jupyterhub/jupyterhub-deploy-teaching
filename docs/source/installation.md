# Installation

1. Before deploying, for each host:
  - Start the server running latest Ubuntu.
  - Enable passwordless SSH access as `root`.
  - Partition and format any local disks you want to mount.
  - Make sure the server's hostname matches the fully qualified domain name (FQDN).
  - Make sure there is a valid DNS entry for the server.
  - If you not going to use letsencrypt, obtain a trusted SSL certificate and
    key for the server at that FQDN.
2. Edit the `./hosts` file to lists the FQDN's of the hosts in the jupyterhub_hosts
   group.
2. For each host, create a file in `./host_vars` with the name of the host, starting
   from `./host_vars/hostname.example`.
3. Create a `./security/cookie_secret` file by doing:

	openssl rand -hex 1024 > ./security/cookie_secret

4. If you are not using letsencrypt, install your SSL private key and certificate as
   `./security/ssl.crt` and `./security/ssl.key`.
5. Run `ansible-playbook` for the main deployment:

	ansible-playbook deploy.yml

6. SSH to the server and reload supervisor:

	supervisorctl reload


# Configuring nbgrader

The main nbgrader package will be installed in the above deployment. However, to run
nbgrader's formgrade application or use its notebook extensions, additional steps are
needed.

Each user who wants to use the notebook extension will need to run:

	nbgrader extension activate

After the main instructor (`nbgrader_owner`) has logged into the system, run the
following command to deploy formgrade:

	ansible-playbook deploy_formgrade.yml

Then SSH to the server and restart jupyterhub and nbgrader by doing:

	supervisorctl reload

## Notes

* To limit the deployment to certain hosts, add the `-l hostname` to these commands:

    ansible-playbook -l hostname deploy.yml

* The logs for `jupyterhub` are in `/var/log/jupyterhub`.
* The logs for `nbgrader` are in `/var/log/nbgrader`.
* If you are not using GitHub OAuth, you will need to manually create users using
  `adduser`: `adduser --gecos "" username`.
* Change the ansible configuration by editing `./ansible_cfg`.
* To manage the jupyterhub and nbgrader services by SSH to the server and run
  `supervisorctl jupyterhub [start|stop|restart]`

## Saving and restoring users

In some situations, you may remount your user's home directories into a new instance that
doesn't have their user accounts, but has their home directories. When recreating the
same users it is important that they all have the same uids so the new users have
ownership of the home directories.

**This is only relevant when using GitHub OAuth for users and authentication.**

To save the list of usernames and uids in `{{homedir}}/saved_users.txt`:

    ansible-playbook saveusers.yml

Then, when you run deploy.yml, it will look for this file and if it exists, will create
those users with those exact uids and home directories.

You can also manually create the users by running:

	python3 create_users.py

in the home directory.
