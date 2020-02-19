#!/bin/bash

NAME="OSINT_System"                              #Name of the application (*)
DJANGODIR=/home/rapics/OSINT/OSINT_System             # Django project directory (*)


echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/rapics/OSINT/OSINT_System/venv/bin/activate

# Start your OSINT Project
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/rapics/OSINT/OSINT_System/venv/bin/python /home/rapics/OSINT/OSINT_System/manage.py runserver 0:8000
#exec /var/www/OSINT/OSINT_System/manage.py run_huey
