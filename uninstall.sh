#!/bin/bash

set -x

sudo rm -rf /opt/paratonnerre_eskers/
sudo rm -rf /var/log/paratonnerre_eskers

sudo rm -f /etc/logrotate.d/paratonnerre_eskers
sed -i '/paratonnerre_eskers/d' /etc/crontab

sudo rm -f /home/centos/.config/autostart/popup.sh.desktop
sudo rm -f /home/centos/.config/autostart/shutdown_timeout.sh.desktop
sudo rm -f /usr/local/bin/popup.sh
