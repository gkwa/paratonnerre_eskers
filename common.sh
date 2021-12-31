#!/bin/bash

# time units: minutes
UPTIME=60
CANCEL=20
DELAY=10

UPTIME=60
CANCEL=20
DELAY=10

write_timestamp() {
    echo "I'm still here!"
    timestamp=$(date +%s -d "+$UPTIME minutes")
    friendly=$(date -d "+$UPTIME minutes")
    echo "$timestamp # $friendly" >>/var/log/paratonnerre_eskers/shutdown.log
}
