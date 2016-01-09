#!/bin/bash

set -e

if [ "$ENV" = 'ADMIN' ]; then
   echo "setup api server ..."
   export DJANGO_SETTINGS_MODULE="avipost.settings.prod"
   python avipost/manage.py migrate 
   python avipost/manage.py fixture _oauth
   python avipost/manage.py fixture _users --par dev,dev_token
else
   echo "running production server..."
   supervisord -c /etc/supervisord.conf -n
fi