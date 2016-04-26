# Deploy JupyterHub for teaching

[![Google Group](https://img.shields.io/badge/-Google%20Group-lightgrey.svg)](https://groups.google.com/forum/#!forum/jupyter)
[![Documentation Status](http://readthedocs.org/projects/jupyterhub-deploy-teaching/badge/?version=latest)](http://jupyterhub-deploy-teaching.readthedocs.org/en/latest/?badge=latest)

The goal of this repository is to produce a reference deployment of JupyterHub for teaching with nbgrader.

The repository started from [this deployment](https://github.com/calpolydatascience/jupyterhub-deploy-data301) of JupyterHub
for "Introduction to Data Science" at Cal Poly.
It is designed to be a simple and reusable JupyterHub deployment, while following best practices.

The main use case targeted is small to medium groups of trusted users working on a single server.

## Design Goal

Have a deployment that is as simple as possible:

- Use a single server.
- Use Nginx as a frontend proxy, serving static assets, and a termination
  point for SSL/TLS.
- Configure using Ansible scripts.
- Use (optionally) https://letsencrypt.org/ for generating SSL certificates.
- Does not use Docker or containers

## Prequisites

To *deploy* this JupyterHub reference deployment, you should have:

- An empty Ubuntu server running the latest stable release
- Local drives to be mounted
- A formatted and mounted directory to store user home directories
- A valid DNS name
- SSL certificate
- Ansible 2.0+ installed for JupyterHub configuration

For *administration* of the deployment, you should also:

- Specify the admin users of JupyterHub.
- Allow SSH key based access to server and add the public SSH keys of GitHub
  users who need to be able to SSH to the server as `root` for administration.

For *managing users and services* on the server, you will have:

- "Trusted" users on the system, meaning that you would give them a
  user-level shell account on the server
- Authenticate and manage users with either:
  * Regular Unix users and PAM.
  * GitHub OAuth
- Manage the running of jupyterhub and nbgrader using supervisor.
- Monitor the state of the server (optional feature) using NewRelic or your
  cloud provider.

## Installation

Follow the instructions in the [Installation Guide]_





_[Installation Guide](http://jupyterhub-deploy-teaching.readthedocs.org/en/latest/installation.html)