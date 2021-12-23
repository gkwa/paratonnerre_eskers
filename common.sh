#!/bin/bash

write_timestamp() {
    echo "I'm still here!"
    d1=$(date +%s -d "+1 hour")
    d2=$(date -d "+1 hour")
    echo "$d1 # $d2" >>/var/log/paratonnerre_eskers/shutdown.log
}
