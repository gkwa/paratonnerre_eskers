#!/bin/bash

# time units: minutes
UPTIME=60
CANCEL=20
DELAY=20

timestamp() {
    timestamp=$(date +%s -d "+$UPTIME minutes")
    friendly=$(date -d "+$UPTIME minutes")
    echo "$timestamp # $friendly"
}

write_timestamp() {
    echo "I'm still here!"
    timestamp >>/var/log/paratonnerre_eskers/shutdown.log
}
