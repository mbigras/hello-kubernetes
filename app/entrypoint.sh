#!/bin/bash
# Script entrypoint.sh runs your app with Gunicorn.
#
# Consider the following input environment variables.
#
# 1. PORT - the port your app should listen on; default: 8080.
# 2. ADDRESS - the address your app should listen on; default: 127.0.0.1

exec gunicorn app:app --bind ${ADDRESS:-127.0.0.1}:${PORT:-8080}
