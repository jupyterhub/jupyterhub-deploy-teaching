# Repository Contents

## Ansible application

### ansible.cfg

Custom configuration settings for the Ansible application
- We use to customize root access, root privileges, and ssh connection length.

### ansible-conda

Git submodule for `ansible-conda` application

## Inventory (Ansible)

### hosts.inventory

Inventory file of servers (hosts) being managed by Ansible

## Playbooks (Ansible)

### deploy.yml (a.k.a. site.yml in Ansible jargon)

### deploy_formgrade.yml

### saveusers.yml

## Variables (Ansible)

### group_vars

### host_vars

## Roles (Ansible)

### bash

### common

### cull_idle

### formgrade

### jupyterhub

### nbgrader

### newrelic

### nginx

### python

### r

### saveusers

### supervisor


## Development

### .gitignore

### .gitmodules

### LICENSE

### README.md

## Documentation

### readthedocs.yml

Settings for readthedocs services

### docs

Directory containing sphinx documentation for the reference deployment.
