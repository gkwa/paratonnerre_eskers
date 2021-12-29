#!/bin/bash

. /opt/paratonnerre_eskers/common.sh

start_timer() {
    sleep ${UPTIME}m

    i=0
    while sleep $(($CANCEL*60/100))s; do
        echo $((i++))
    done | zenity --progress --width=300 --height=200 --title="Autoshutdown in $CANCEL minutes" --auto-close \
        --text="To conserve resources we will auto-shutdown this host in $CANCEL minutes. To extend your time for another hour, cancel this popup."
    retVal=$?

    if [ $retVal -ne 0 ]; then
        write_timestamp
    else
        echo "I've moved on"
    fi
}

main() {
    write_timestamp
    while true; do
        start_timer
        sleep 1m
    done
}

main
