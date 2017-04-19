#!/bin/bash
. $(dirname "$0")/env

docker run --rm -it --cap-add SYS_ADMIN jupyterhub-deploy-test
