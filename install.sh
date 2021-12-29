#!/bin/bash

set -x

curl -sSL https://raw.githubusercontent.com/TaylorMonacelli/paratonnerre_eskers/master/uninstall.sh | sudo bash -x

mkdir -p /opt/paratonnerre_eskers/

curl -sSLo /tmp/common.sh https://raw.githubusercontent.com/TaylorMonacelli/paratonnerre_eskers/master/common.sh
sudo install -m 755 /tmp/common.sh /opt/paratonnerre_eskers/common.sh

curl -sSLo /tmp/popup.sh https://raw.githubusercontent.com/TaylorMonacelli/paratonnerre_eskers/master/popup.sh
sudo install -m 755 /tmp/popup.sh /opt/paratonnerre_eskers/popup.sh

curl -sSLo /tmp/popup.sh.desktop https://raw.githubusercontent.com/TaylorMonacelli/paratonnerre_eskers/master/popup.sh.desktop
if [[ -d /home/centos/ ]]; then
    mkdir -p /home/centos/.config/autostart
    cp /tmp/popup.sh.desktop /home/centos/.config/autostart/popup.sh.desktop
    chown centos /home/centos/.config/autostart/popup.sh.desktop
    chmod a+rwx /home/centos/.config/autostart/popup.sh.desktop
fi

chmod a+rwx /opt/paratonnerre_eskers/

mkdir -p /var/log/paratonnerre_eskers
chmod a+rwx /var/log/paratonnerre_eskers

touch /var/log/paratonnerre_eskers/shutdown.log
chmod a+rwx /var/log/paratonnerre_eskers/shutdown.log

cat <<'__eot__' >/opt/paratonnerre_eskers/shutdown.sh
#!/bin/bash

now=$(date +%s)
shutdown_time=$(tail -1 /var/log/paratonnerre_eskers/shutdown.log | awk '{print $1}')

if [ $now -ge $shutdown_time ]; then
    echo scheduling shutdown for soonish
    shutdown +20
else
    echo blocking shutdown
    if [ -f /run/systemd/shutdown/scheduled ]; then
        shutdown -c
    fi 
fi
__eot__
chmod +x /opt/paratonnerre_eskers/shutdown.sh
sed -i '/paratonnerre_eskers/d' /etc/crontab
echo '* * * * * root /opt/paratonnerre_eskers/shutdown.sh' | tee -a /etc/crontab

. /opt/paratonnerre_eskers/common.sh
write_timestamp

cat <<'__eot__' >/etc/logrotate.d/paratonnerre_eskers
/var/log/paratonnerre_eskers/*.log {
 size 1M
 rotate 3
 notifempty
 compress
}
__eot__
