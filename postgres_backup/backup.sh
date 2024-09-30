#!/bin/bash

# Create a new backup
pg_dump -U djkallet -F t djkallet > /home/djkallet/publicwsgi/backup/mainsite_$(date +%F_%R).tar

# Keep only the 3 most recent backups and delete older ones
cd /home/djkallet/publicwsgi/backup && ls -t | tail -n +4 | xargs rm -f
