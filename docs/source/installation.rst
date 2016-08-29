Installation Guide
==================

Prerequisites
-------------

- Start a server running latest Ubuntu version.

- Enable password-less SSH access for :command:`ubuntu` user.

- Partition and format any local disks you want to mount.

- Verify a valid DNS entry for the server.

- Choose an SSL certificate source. Use either of these options:

  * `Let's Encrypt <https://letsencrypt.org/>`_
  * obtain a trusted SSL certificate and key for the server at that FQDN.

- Checkout the latest version of the repository including the ``ansible-conda`` submodule::

    $ git clone --recursive https://github.com/jupyterhub/jupyterhub-deploy-teaching.git

Create the hosts group
----------------------

1. Edit the :file:`./hosts` file to lists the FQDN's of the hosts in the
   ``jupyterhub_hosts`` group.

2. Create for each host a file in :file:`./host_vars` directory with the
   name of the host, starting from :file:`./host_vars/hostname.example`.

Secure your deployment
----------------------

1. Create a cookie secret file, :file:`./security/cookie_secret`, using::

    $ openssl rand -hex 1024 > ./security/cookie_secret

   For additional information, see the `cookie secret file <https://jupyterhub.readthedocs.io/en/latest/getting-started.html#cookie-secret>`_ section in the JupyterHub documentation.

2. If you are using `Let's Encrypt <https://letsencrypt.org/>`_, skip this step.
   Otherwise, install your SSL private key :file:`./security/ssl.key` and
   certificate as :file:`./security/ssl.crt`.

Deploy with Ansible
-------------------

1. Run :file:`ansible-playbook` for the main deployment::

    $ ansible-playbook deploy.yml

Verify your deployment
----------------------

1. SSH into the server::

    $ ssh root@{hostname}
    
substituting your hostname for {hostname}. For example, ``ssh root@jupyter.org``.

2. Reload supervisor::

    $ supervisorctl reload
