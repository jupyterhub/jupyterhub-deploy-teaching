# Deploy JupyterHub for teaching

[![Google Group](https://img.shields.io/badge/-Google%20Group-lightgrey.svg)](https://groups.google.com/forum/#!forum/jupyter)
[![Documentation Status](http://readthedocs.org/projects/jupyterhub-deploy-teaching/badge/?version=latest)](http://jupyterhub-deploy-teaching.readthedocs.org/en/latest/?badge=latest)

The goal of this repository is to produce a reference deployment of JupyterHub for teaching with nbgrader.

The repository started from [this deployment](https://github.com/calpolydatascience/jupyterhub-deploy-data301) of JupyterHub
for "Introduction to Data Science" at Cal Poly.
It is designed to be a simple and reusable JupyterHub deployment, while following best practices.

The main use case targeted is small to medium groups of trusted users working on a single server.

## Design

Individuals using this repo to deploy JupyterHub should be able to:

* Start from:
  - An empty Ubuntu latest stable server with SSH key based access.
  - A valid DNS name.
  - A formatted and mounted directory to use for user home directories.
  - The assumption that all users of the system will be "trusted," meaning that
    you would given them a user-level shell account on the server.
* Always have SSL/TLS enabled.
* Optionally monitor the state of the server and set email alerts using NewRelic.
  The builtin monitoring of your cloud provider can also be used.
* Specify admin users of JupyterHub.
* Manager users and authentication using either:
  - Regular Unix users and PAM.
  - GitHub OAuth
* Manage the running of jupyterhub and nbgrader using supervisor.
* Specify local drives to be mounted.
* Add the public SSH keys of GitHub users who need to be able to SSH to the server
  as `root` for administration.
* Have a deployment that is as simple as possible:
  - No Docker.
  - Nginx as a frontend proxy, serving static assets, and a termination point for SSL/TLS.
  - A single server.
  - Ansible for config.
  - Optionally use https://letsencrypt.org/ for generating SSL certificates.
* Configure and run nbgrader:
  - The course name.
  - The location of the nbgrader config.
  - The instructors username.
  - Graders' usernames.

End users of the deployment should be able to:

* Use the following Jupyter kernels:
  - Python 3 IPython kernel with the main Python libraries for data science.
  - Bash (https://github.com/takluyver/bash_kernel).
* Sign in using their GitHub or Unix credentials.
* Have a persistent home directory.
* Have outbound network access.

# Instructions

1. Before deploying, for each host:
  - Start the server running latest Ubuntu.
  - Enable passwordless SSH access as `root`.
  - Partition and format any local disks you want to mount.
  - Make sure the server's hostname matches the fully qualified domain name (FQDN).
  - Make sure there is a valid DNS entry for the server.
  - If you not going to use letsencrypt, obtain a trusted SSL certificate and
    key for the server at that FQDN.
  - Install ansible ≥ 2.0:

        pip install ansible>=2

2. Edit the `./hosts` file to lists the FQDN's of the hosts in the jupyterhub_hosts
   group. See `./hosts.example` for an example.
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

# To run nbgrader

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

## Using nbgrader

With the above setup, instructors can start to use nbgrader. This section contains a rough sketch
of what that looks like. For full details see the [nbgrader
documentation](http://nbgrader.readthedocs.org/en/latest/).

To use nbgrader, an instructor will primarily use the nbgrader command line
program. Before doing this, the instructor will need to edit the
`nbgrader_config.py` file with a list of students and assignments as follows:

```python
c.NbGrader.db_assignments = [dict(name="ps1")]
c.NbGrader.db_students = [
    dict(id="bitdiddle", first_name="Ben", last_name="Bitdiddle"),
    dict(id="hacker", first_name="Alyssa", last_name="Hacker"),
    dict(id="reasoner", first_name="Louis", last_name="Reasoner")
]
```

You can also add an `email` field to each student and a `duedate` field to
each assignment. Each time you create a new assignment add it to the config
file.

For each assignment, first create a directory for an assignment's source:

	cd ~/nbgrader/<course>
	mkdir source/<assignment>

Next, copy notebooks into that directory:

	cp ~/Problem1.ipynb ~/nbgrader/<course>/source/<assignment>
	cp ~/Problem2.ipynb ~/nbgrader/<course>/source/<assignment>
	
These notebooks should be prepared using the nbgrader "Create Assignment Celltoolbar". Now create
the assignment:


	nbgrader assign <assignment>
	
That will create the student versions of the notebooks and put them into the
`~/nbgrader/<course>/release/<assignment>` directory with your solutions removed.

Next, release the assignment to students:

	nbgrader release <assignment>
	
At this point, students can fetch the assignment by doing:

	nbgrader fetch --course <course> <assignment>
	
That will give students a copy of the assignment directory with all of the notebooks. When students
are done working the notebooks, they can submit the assignment by doing:

	nbgrader submit --course <course> <assignment>
	
You can collect submitted assignments by doing:

	nbgrader collect <assignment>

This puts the students submitted work into the `~/nbgrader/<course>/submitted/<assignment>` directory. To enter those notebooks into the nbgrader web grading system, run:

	nbgrader autograde <assignment>

By default, this will rerun all of the students notebooks. If you don't want to run them:

	nbgrader autograde --no-execute <assignment>
	
To see the full command line options for nbgrader, run:

	nbgrader <subcommand> --help

Some other things you can do with nbgrader:

* Run `collect` and `autograde` commands for a single student or notebook.
* Collect a single assignment multiple times and regrade all or parts selectively.

