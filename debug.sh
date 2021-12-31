#!/bin/bash

[ -f /opt/paratonnerre_eskers/common.sh ] && . /opt/paratonnerre_eskers/common.sh

echo UPTIME=$UPTIME
echo CANCEL=$CANCEL
echo DELAY=$DELAY

ls -la /opt/paratonnerre_eskers/*
ls -la /var/log/paratonnerre_eskers/*
ls -la /home/centos/.config/autostart/*.sh.desktop
ls -la /etc/logrotate.d/paratonnerre_eskers

grep paratonnerre_eskers /etc/crontab
getent group paratonnerre_eskers
systemctl status systemd-shutdownd.service | grep Active:
