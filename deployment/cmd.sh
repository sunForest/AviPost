#!/bin/bash

set -e

if [ "$ENV" = 'ADMIN' ]; then
   echo "setup api server ..."
   export DJANGO_SETTINGS_MODULE="avipost.settings.prod"
   python avipost/manage.py migrate 
   python avipost/manage.py loaddata avipost/contrib/management/commands/usersDev.json
   python avipost/manage.py loaddata avipost/contrib/management/commands/app.json
   python avipost/manage.py loaddata avipost/contrib/management/commands/token.json
else
   echo "running production server..."
   supervisord -c /etc/supervisord.conf -n
fi