#!/bin/bash

set -x

curl -sSL https://paratonnerre-eskers.s3.us-west-2.amazonaws.com/uninstall.sh | sudo bash -x

mkdir -p /opt/paratonnerre_eskers/
chmod +x /opt/paratonnerre_eskers/

curl -sSLo /tmp/common.sh https://paratonnerre-eskers.s3.us-west-2.amazonaws.com/common.sh
sudo install -m 755 /tmp/common.sh /opt/paratonnerre_eskers/common.sh

curl -sSLo /tmp/popup.sh https://paratonnerre-eskers.s3.us-west-2.amazonaws.com/popup.sh
sudo install -m 755 /tmp/popup.sh /opt/paratonnerre_eskers/popup.sh

curl -sSLo /tmp/popup.sh.desktop https://paratonnerre-eskers.s3.us-west-2.amazonaws.com/popup.sh.desktop
if [[ -d /home/centos/ ]]; then
    mkdir -p /home/centos/.config/autostart
    cp /tmp/popup.sh.desktop /home/centos/.config/autostart/popup.sh.desktop
    chown centos /home/centos/.config/autostart/popup.sh.desktop
    chmod a+rwx /home/centos/.config/autostart/popup.sh.desktop
fi

mkdir -p /var/log/paratonnerre_eskers
touch /var/log/paratonnerre_eskers/shutdown.log
chmod -R a+rwx /var/log/paratonnerre_eskers

curl -sSL https://paratonnerre-eskers.s3.us-west-2.amazonaws.com/shutdown.sh | sudo bash -x
chmod +x /opt/paratonnerre_eskers/shutdown.sh

sed -i '/paratonnerre_eskers/d' /etc/crontab
echo '* * * * * root /opt/paratonnerre_eskers/shutdown.sh >/dev/null' | tee -a /etc/crontab

# add first timestamp for $UPTIME from now
. /opt/paratonnerre_eskers/common.sh
write_timestamp

cat <<'__eot__' >/etc/logrotate.d/paratonnerre_eskers
/var/log/paratonnerre_eskers/*.log {
 size 1M
 rotate 1
 notifempty
 compress
}
__eot__
