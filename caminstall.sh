#!/bin/bash
# caminstall.sh
# Install camera dependencies.
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi
echo 'Installing pi camera dependencies.'
apt-get update
apt-get -y install python-picamera
echo 'Now you need to enable the camera using sudo raspi-config'
