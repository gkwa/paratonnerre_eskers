#!/bin/bash

ls -la /opt/paratonnerre_eskers/*
ls -la /var/log/paratonnerre_eskers/*
ls -la /home/centos/.config/autostart/*.sh.desktop
ls -la /usr/local/bin/popup.sh

grep paratonnerre_eskers /etc/crontab
