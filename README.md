# Deploy JupyterHub for teaching DATA 301

This repository contains the code being used to deploy JupyterHub for DATA 301,
"Introduction to Data Science," at Cal Poly.

# Design

Individuals using this repo to deploy JupyterHub should be able to:

* Start from:
  - An empty Ubuntu latest stable server with SSH key based access.
  - A valid DNS name.
  - A formatted and mounted directory to use for user home directories.
  - A formatted and mounted directory to use for datasets.
  - The assumption that all users of the system will be "trusted," meaning that
    you would given them a user-level shell account on the server.
* Always have TLS enabled.
* Have idle notebook servers culled on some time interval.
* Limit the RAM usage of individual notebook servers.
* Monitor the state of the server and set email alerts.
* Specify admin users of JupyterHub.
* Configure nbgrader:
  - The course id.
  - The location of the nbgrader config.
* Have all user directories automatically created.
* Ensure that jupyterhub and nbgrader are always running.
* Start, stop and restart jupyterhub and nbgrader by logging on to the server?
* Run this deployment for a single course (in the nbgrader sense).
* Have a deployment that is as simple as possible:
  - No Docker for now.
  - Nginx as a frontend proxy and termination point for TLS.
  - On a single server.
  - Ansible for config.
* Launch the server in a single command.

Admin users of the deployment should be able to:

* Access the JupyterHub control panel and all of its functionality, including
  starting and stopping user notebook severs and adding users by GitHub usernames.
* [?] Install additional apt and Python packages and language kernels.
* [?] Access the global data directory with rwx permissions.

End users of the deployment should be able to:

* Use the Python 3 IPython kernel and main Python libraries for data science.
* Sign in using their GitHub username and password.
* Have a persistent home directory.
* Access the global data directory with r permissions.
* Have outbound network access.

# Instructions

1. Before deploying:
  - Server must be up and running latest Ubuntu.
  - Hostname should match the fully qualified domain name (FQDN).
  - There should be a valid DNS entry for the server.
  - You should have a trust SSL certificate and key for the server at that FQDN.
2. Set the hostname
3. Install the SSL certificates into the security directory.
4. Generate a JupyterHub cookie secret using `openssl rand -hex 1024` and save it into
   `security/cooke_secret`.
5. Set the list of usernames.
6. Create a GitHub app and copy.

Optionally

1. Create a NewRelic account and get your license key.
2. Create a Google Analytics account and get your account number.
 
  
  
  

