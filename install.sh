#!/bin/bash

set -x

curl -sSL https://raw.githubusercontent.com/TaylorMonacelli/paratonnerre_eskers/master/uninstall.sh | sudo bash -x

curl -sSLo /tmp/shutdown_timeout.sh https://raw.githubusercontent.com/TaylorMonacelli/paratonnerre_eskers/master/shutdown_timeout.sh
sudo install -m 777 /tmp/shutdown_timeout.sh /usr/local/bin/shutdown_timeout.sh

curl -sSLo /tmp/shutdown_timeout.sh.desktop https://raw.githubusercontent.com/TaylorMonacelli/paratonnerre_eskers/master/shutdown_timeout.sh.desktop

if [[ -d /home/centos/ ]]; then
    mkdir -p /home/centos/.config/autostart
    cp /tmp/shutdown_timeout.sh.desktop /home/centos/.config/autostart/shutdown_timeout.sh.desktop
    chown centos /home/centos/.config/autostart/shutdown_timeout.sh.desktop
    chmod a+rwx /home/centos/.config/autostart/shutdown_timeout.sh.desktop
fi

mkdir -p /opt/paratonnerre_eskers/
chmod a+rwx /opt/paratonnerre_eskers/
