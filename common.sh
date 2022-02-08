#!/bin/bash

DEBUG=0

if [[ $DEBUG == 1 ]]; then
    # debug
    UPTIME=60
    CANCEL=20
    DELAY=5
    SLEEP1=0m
    SLEEP2=0.1s
    SLEEP3=5s
else
    # non-debug
    UPTIME=60
    CANCEL=20
    DELAY=10
    SLEEP1=40m
    SLEEP2=12s
    SLEEP3=1m
fi

timestamp() {
    timestamp=$(date +%s -d "+$UPTIME minutes")
    friendly=$(date -d "+$UPTIME minutes")
    echo "$timestamp # $friendly"
}

write_timestamp() {
    echo "I'm still here!"
    timestamp >>/var/log/paratonnerre_eskers/shutdown.log
}
