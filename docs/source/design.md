## Design goals

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