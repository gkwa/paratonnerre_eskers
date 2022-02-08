#!/bin/bash

. /opt/paratonnerre_eskers/common.sh

title="Autoshutdown in $CANCEL minutes"
msg="To conserve resources we will auto-shutdown this host in $CANCEL minutes. To extend your time for another hour, cancel this popup."

start_timer() {
    sleep $SLEEP1

    i=0
    while sleep $SLEEP2; do
        echo $((i++))
    done | zenity --progress --width=300 --height=200 --title="$title" --auto-close --text="$msg"
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
        sleep $SLEEP3
    done
}

main
