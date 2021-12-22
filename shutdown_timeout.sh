#!/bin/bash

write_timestamp() {
    echo "I'm still here!"
    d1=$(date +%s -d "+1 hour")
    d2=$(date -d "+1 hour")
    echo "$d1 # $d2" >>/var/log/paratonnerre_eskers/shutdown.log
}

start_timer() {
    i=0
    while sleep 36; do
        echo $((i++))
    done | zenity --progress --width=300 --height=200 --title="Autoshutdown in 1h" --auto-close \
        --text="To conserve resources we will auto-shutdown this host in an hour. To extend your time for another hour, cancel this popup."
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
