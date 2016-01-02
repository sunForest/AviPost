#!/bin/bash

set -e

if [ "$ENV" = 'ADMIN' ]; then
   echo "setup api server ..."
   python avipost/manage.py migrate --settings=avipost.settings.prod
   python avipost/manage.py loaddata avipost/contrib/management/commands/user.json --settings=avipost.settings.prod
   python avipost/manage.py loaddata avipost/contrib/management/commands/app.json --settings=avipost.settings.prod
else
   echo "running production server..."
   supervisord -c /etc/supervisord.conf -n
fi