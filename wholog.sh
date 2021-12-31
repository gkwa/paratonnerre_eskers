#!/bin/bash

. /opt/paratonnerre_eskers/common.sh

mkdir -p /var/log/paratonnerre_eskers
ts=$(timestamp)

{ 
    echo date: $ts
    /usr/bin/w
} >>/var/log/paratonnerre_eskers/wholog.log
