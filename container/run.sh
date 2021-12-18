#!/bin/bash

# expects timestamp like: 16:50:01
timestamp=$(
    tail -1000 /data/who.log | tac | grep -m1 -A10 centos |
        grep -m1 'load average' | awk '{print $1}'
)

python run.py --timestamp $timestamp
