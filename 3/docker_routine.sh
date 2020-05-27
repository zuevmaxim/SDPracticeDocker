#! /bin/bash

apt update
echo Y | apt install python3

cd /home/m
python3 server.py 5665

