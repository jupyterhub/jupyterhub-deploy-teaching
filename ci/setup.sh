#!/bin/bash
. $(dirname "$0")/env

# stage test host config
echo -e "[jupyterhub_hosts]\n$DOMAIN" > "$ROOT/hosts"
cp "$CI/host_vars.test" "$ROOT/host_vars/$DOMAIN"

# generate fake security
security="$ROOT/security"
test -d "$security" || mkdir "$security"
openssl rand -hex 1024 > "$security/cookie_secret"
test -f "$security/ssl.crt" || openssl req -x509 -days 2 -newkey rsa:2048 -nodes -out "$security/ssl.crt" -keyout "$security/ssl.key" -subj "/C=no/ST=Oslo/O=Min/CN=$DOMAIN"

docker build -t jupyterhub-deploy-test --build-arg DOMAIN=$DOMAIN "$ROOT"
