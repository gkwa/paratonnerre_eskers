#!/bin/bash

. /opt/paratonnerre_eskers/common.sh
CANCEL_TIME=20 #MINUTES

start_timer() {
    sleep 50m

    i=0
    while sleep $(($CANCEL_TIME*60/100))s; do
        echo $((i++))
    done | zenity --progress --width=300 --height=200 --title="Autoshutdown in $CANCEL_TIME minutes" --auto-close \
        --text="To conserve resources we will auto-shutdown this host in $CANCEL_TIME minutes. To extend your time for another hour, cancel this popup."
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
