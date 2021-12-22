#!/bin/bash

set -x

curl -sSL https://raw.githubusercontent.com/TaylorMonacelli/paratonnerre_eskers/master/uninstall.sh | sudo bash -x

curl -sSLo /tmp/shutdown_timeout.sh https://raw.githubusercontent.com/TaylorMonacelli/paratonnerre_eskers/master/shutdown_timeout.sh
sudo install -m 755 /tmp/shutdown_timeout.sh /usr/local/bin/shutdown_timeout.sh

curl -sSLo /tmp/shutdown_timeout.sh.desktop https://raw.githubusercontent.com/TaylorMonacelli/paratonnerre_eskers/master/shutdown_timeout.sh.desktop

if [[ -d /home/centos/ ]]; then
    mkdir -p /home/centos/.config/autostart
    cp /tmp/shutdown_timeout.sh.desktop /home/centos/.config/autostart/shutdown_timeout.sh.desktop
    chown centos /home/centos/.config/autostart/shutdown_timeout.sh.desktop
    chmod a+rwx /home/centos/.config/autostart/shutdown_timeout.sh.desktop
fi

mkdir -p /opt/paratonnerre_eskers/
chmod a+rwx /opt/paratonnerre_eskers/

mkdir -p /var/log/paratonnerre_eskers
chmod a+rwx /var/log/paratonnerre_eskers
mkdir -p /opt/paratonnerre_eskers/who
cat <<'__eot__' >/opt/paratonnerre_eskers/who/who.sh
#!/bin/bash

shutdown_time=$(tail -1 /var/log/paratonnerre_eskers/shutdown.log)
now=$(date +%s)
if [ $now -ge $shutdown_time ]; then
    if [ ! -f /run/systemd/shutdown/scheduled ]; then
        shutdown +15
    fi 
fi
__eot__
chmod +x /opt/paratonnerre_eskers/who/who.sh
sed -i '/opt.paratonnerre_eskers.who.who.sh/d' /etc/crontab
echo '* * * * * root /opt/paratonnerre_eskers/who/who.sh' | tee -a /etc/crontab

cat <<'__eot__' >/etc/logrotate.d/paratonnerre_eskers
/var/log/paratonnerre_eskers/*.log {
 size 10M
 rotate 5
 notifempty
 compress
}
__eot__
