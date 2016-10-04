Design goals
============

Instructors and maintainers
---------------------------

When using this repository to deploy JupyterHub and nbgrader, individuals
should be able to have a deployment that is as simple as possible:

- No Docker use.
- `NGINX <https://www.nginx.com>`_ as a frontend proxy, serving static
  assets, and a termination point for SSL/TLS.
- A single server.
- `Ansible <https://www.ansible.com/resources>`_ for configuration.
- Optionally, use `Let's Encrypt  <https://letsencrypt.org/>`_  for
  generating SSL certificates.

JupyterHub
~~~~~~~~~~

* Start from:

  - An empty Ubuntu latest stable server with SSH key based access.
  - A valid DNS name.
  - A formatted and mounted directory to use for user home directories.
  - The assumption that all users of the system will be "trusted," meaning
    that you would given them a user-level shell account on the server.

* Always have SSL/TLS enabled.
* Specify local drives to be mounted.
* Manage the running of jupyterhub and nbgrader using supervisor.
* Optionally, monitor the state of the server and set email alerts using
  `NewRelic <https://newrelic.com/>`_. The built-in monitoring of your cloud
  provider may also be used.
* Specify admin users of JupyterHub.
* Add the public SSH keys of GitHub users who need to be able to ``ssh`` to
  the server as ``root`` for administration.
* Manage users and authentication using either:

  - Regular Unix users and `PAM (Pluggable authentication modules) <https://en.wikipedia.org/wiki/Linux_PAM>`_
  - `GitHub OAuth <https://developer.github.com/v3/oauth/>`_

nbgrader
~~~~~~~~
* Run nbgrader and configure:

  - The course name.
  - The instructors username.
  - Graders' usernames.
  - The location of the nbgrader config.

Students
--------
End users of this deployment should be able to:

* Use the following Jupyter kernels.

  - `Python version 3 <https://docs.python.org/3/>`_ using the IPython kernel
    with the main Python libraries for data science.
  - Bash kernel <https://github.com/takluyver/bash_kernel>

* Sign in using their GitHub or Unix credentials.
* Have a persistent home directory.
* Have outbound network access.

.. _`Let's Encrypt <https://letsencrypt.org/>`:
