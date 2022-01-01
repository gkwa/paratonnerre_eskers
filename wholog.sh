#!/bin/bash

mkdir -p /var/log/paratonnerre_eskers
{ 
    echo "date: $(date +%s) # $(date)"
    /usr/bin/w
} >>/var/log/paratonnerre_eskers/wholog.log
