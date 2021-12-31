#!/bin/bash

sudo rm -rf /opt/paratonnerre_eskers/
sudo rm -rf /var/log/paratonnerre_eskers
sudo rm -f /etc/logrotate.d/paratonnerre_eskers
sudo rm -f /home/centos/.config/autostart/popup.sh.desktop
sudo rm -f /home/centos/.config/autostart/shutdown_timeout.sh.desktop

sed -i /paratonnerre_eskers/d /etc/crontab

if grep --silent paratonnerre_eskers <<<$(getent group); then
    gpasswd --delete centos paratonnerre_eskers
    getent passwd | grep --quiet ^paratonnerre_eskers: && userdel --remove paratonnerre_eskers
fi

grep --silent paratonnerre_eskers <<<$(getent group) && groupdel paratonnerre_eskers
