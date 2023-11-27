#!/bin/bash

# Add your cron job as root
echo "* * * * * cd /data/ && tar -cf /backups/backup.tar *" | crontab -

# Start cron in the background
service cron start

# Run your application as nbctfuser
exec gosu nbctfuser /data/venv/bin/flask run --host 0.0.0.0 -p 1337
