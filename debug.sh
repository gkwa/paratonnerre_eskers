#!/bin/bash

. /opt/paratonnerre_eskers/common.sh

echo UPTIME=$UPTIME
echo CANCEL=$CANCEL
echo DELAY=$DELAY

ls -la /opt/paratonnerre_eskers/*
ls -la /var/log/paratonnerre_eskers/*
ls -la /home/centos/.config/autostart/*.sh.desktop

grep paratonnerre_eskers /etc/crontab
