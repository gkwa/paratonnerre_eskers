#!/bin/bash

. /opt/paratonnerre_eskers/common.sh

now=$(date +%s)
shutdown_time=$(tail -1 /var/log/paratonnerre_eskers/shutdown.log | awk '{print $1}')

if [ $now -ge $shutdown_time ]; then
    if [ -f /run/systemd/shutdown/scheduled ]; then
        echo shutdown already scheduled
    else
        echo scheduling shutdown for $DELAY minutes from now
        shutdown +$DELAY
    fi 
else
    if [ -f /run/systemd/shutdown/scheduled ]; then
        shutdown -c
        echo shutdown canceled, will shutdown in $((($shutdown_time - $now)/60+$DELAY)) minutes
    else
        echo will shutdown in $((($shutdown_time - $now)/60+$DELAY)) minutes
    fi 
fi
