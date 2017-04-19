# dockerfile for testing this repo on CI
FROM williamyeh/ansible:ubuntu14.04-onbuild

ARG DOMAIN
RUN echo "127.0.0.1 $DOMAIN" >> /etc/hosts

CMD ansible-playbook --connection=local deploy.yml