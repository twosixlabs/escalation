#!/bin/sh
source venv/bin/activate
flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - --log-level debug --timeout 60 --workers 2 server:app

