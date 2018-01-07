# Checklist for a JupyterHub teaching deployment

Documentation for teaching deployment: https://jupyterhub-deploy-teaching.readthedocs.io

Documentation for JupyterHub: https://jupyterhub.readthedocs.io

## Notes

- Does **not** use Docker.
- [NGINX](https://www.nginx.com) as a frontend proxy, for serving static
  assets, and a termination point for SSL/TLS.
- Single Ubuntu server
- [Ansible](https://www.ansible.com/resources) for configuration.

## 1. Prepare the server

- [ ] **Server:** running latest Ubuntu version
- [ ] **SSH:** enable password-less SSH for `ubuntu` user
- [ ] **Local disks:** partition and format
- [ ] **DNS (domain name):** valid entry for server

## 2. Install JupyterHub source

- [ ] **Source:** Clone latest `jupyterhub-deploy-teaching` repo using `--recursive` (needed for `ansible-conda`) submodule

    ```bash
    $ git clone --recursive https://github.com/jupyterhub/jupyterhub-deploy-teaching.git
    ```

## 3. Secure before deployment

- [ ] **cookie secret file:** Create `./security/cookie_secret`

     ```bash
     $ openssl rand -hex 1024 > ./security/cookie_secret
     ```

- [ ] **SSL:**
  * [Let's Encrypt](https://letsencrypt.org/): No additional steps as
    Ansible will install for you.
  * Third Party SSL trusted source: Install SSL private key
    `./security/ssl.key` and certificate as `./security/ssl.crt`.

## 4. Create JupyterHub hosts group

- [ ] **`./hosts` file:** Edit file to lists the FQDN's of the hosts in the
  `jupyterhub_hosts` group.
- [ ] **hostname files:**  Use `./host_vars/hostname.example` as a
  template for creating and editing a hostname file for each host and
  place hostname files in `./host_vars` directory.

## 5. Configure admins

- [ ] List of admins is configured in `jupyterhub_admin_users` in the config
  file. Public SSH keys will be retrieved from GitHub.

## 6. Configure users

- [ ] If using [PAM (Pluggable authentication
  modules)](https://en.wikipedia.org/wiki/Linux_PAM), you will need to
  manually create users using adduser: `adduser --gecos "" username`.

- [ ] If using [GitHub OAuth](https://developer.github.com/v3/oauth/), add
  usernames to `jupyterhub_users` list.

## 7. Add optional services

- [ ] **Monitoring:** New Relic
- [ ] **Analytics:** Google Analytics
- [ ] **Assignment distribution and collection:** nbgrader
- [ ] **Grading:** nbgrader

## 8. Deploy with Ansible

- [ ] **Deploy:** Run `ansible-playbook` for the main deployment.

    ```bash
    $ ansible-playbook -i hosts deploy.yml
    ```

## 9. Verify deployment and reload supervisor

- [ ] **Verify:**  SSH into the server:

    ```bash
    $ ssh root@{hostname}
    ```
    substituting your hostname for {hostname}. For example, ``ssh root@jupyter.org``.

## 10. JupyterLab
