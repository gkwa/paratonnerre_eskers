#!/bin/bash

set -x

sed -i '/paratonnerre_eskers/d' /etc/crontab

sudo rm -f /usr/local/bin/popup.sh
sudo rm -f /home/centos/.config/autostart/popup.sh.desktop
sudo rm -f /etc/logrotate.d/paratonnerre_eskers
sudo rm -rf /opt/paratonnerre_eskers/
