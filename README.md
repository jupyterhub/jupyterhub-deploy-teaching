# Deploy JupyterHub for teaching

[![Google Group](https://img.shields.io/badge/-Google%20Group-lightgrey.svg)](https://groups.google.com/forum/#!forum/jupyter)
[![Documentation Status](http://readthedocs.org/projects/jupyterhub-deploy-teaching/badge/?version=latest)](http://jupyterhub-deploy-teaching.readthedocs.org/en/latest/?badge=latest)

The goal of this repository is to produce a reference deployment of JupyterHub
for teaching with nbgrader.

The repository started from [this deployment](https://github.com/calpolydatascience/jupyterhub-deploy-data301) of JupyterHub
for "Introduction to Data Science" at Cal Poly.
It is designed to be a simple and reusable JupyterHub deployment, while
following best practices.

The main use case targeted is **small to medium groups of trusted users
working on a single server**.

## Design goal of this reference deployment

Create a JupyterHub teaching reference deployment that is simple yet
functional:

- Use a single server.
- Use Nginx as a frontend proxy, serving static assets, and a termination
  point for SSL/TLS.
- Configure using Ansible scripts.
- Use (optionally) https://letsencrypt.org/ for generating SSL certificates.
- Does not use Docker or containers

## Prerequisites

To *deploy* this JupyterHub reference deployment, you should have:

- An empty Ubuntu server running the latest stable release
- Local drives to be mounted
- A formatted and mounted directory to store user home directories
- A valid DNS name
- SSL certificate
- Ansible 2.1+ installed for JupyterHub configuration (`pip install "ansible>=2.1"`)

For *administration* of the server, you should also:

- Specify the admin users of JupyterHub.
- Allow SSH key based access to server and add the public SSH keys of GitHub
  users who need to be able to SSH to the server as `root` for administration.

For *managing users and services* on the server, you will:

- Create "Trusted" users on the system, meaning that you would give them a
  user-level shell account on the server
- Authenticate and manage users with either:
  * Regular Unix users and PAM.
  * GitHub OAuth
- Manage the running of jupyterhub and nbgrader using supervisor.
- Monitor the state of the server (optional feature) using NewRelic or your
  cloud provider.

## Installation

Follow the detailed instructions in the [Installation Guide](http://jupyterhub-deploy-teaching.readthedocs.org/en/latest/installation.html).

The basic steps are:
- Create the hosts group with Fully Qualified Domain Names (FQDNs) of the hosts
- Secure your deployment with SSL
- Deploy with Ansible ``ansible-playbook deploy.yml``
- Verify your deployment and reboot the Hub ``supervisorctl reload``

## Configuring nbgrader

The nbgrader package is installed when JupyterHub is installed using the
steps in the Installation Guide.

View the [documentation for detailed configuration steps](http://jupyterhub-deploy-teaching.readthedocs.org/en/latest/configure-nbgrader.html). The basic steps to
configure formgrade or nbgrader's notebook extensions are:

- activate the extension ``nbgrader extension activate``
- log into JupyterHub
- run ansible script ``ansible-playbook deploy_formgrade.yml``
- SSH into JupyterHub
- reboot the Hub and nbgrader ``supervisorctl reload``

## Using nbgrader

With this reference deployment, instructors can start to use nbgrader.
The [Using nbgrader section](http://jupyterhub-deploy-teaching.readthedocs.org/en/latest/use-nbgrader.html)
of the reference deployment documentation gives brief instructions about
creating course assignments, releasing them to students, and grading student
submissions.

For full details about nbgrader and its features, see the [nbgrader documentation](http://nbgrader.readthedocs.org/en/latest/).

## Notes

### Ansible configuration and deployment

Change the ansible configuration by editing ``./ansible_cfg``.

To limit the deployment to certain hosts, add ``-l hostname`` to the
Ansible deploy commands:

``ansible-playbook -l hostname deploy.yml``

### Authentication
If you are not using GitHub OAuth, you will need to manually create users
using adduser: ``adduser --gecos "" username``.

### Logs
The logs for jupyterhub are in ``/var/log/jupyterhub``.

The logs for nbgrader are in ``/var/log/nbgrader``.

### Starting, stopping, and restarting the Hub
To manage the jupyterhub and nbgrader services by SSH to the server
and run: ``supervisorctl jupyterhub [start|stop|restart]``
