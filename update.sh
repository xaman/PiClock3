#!/bin/bash
USER_AND_DOMAIN="pi@raspberrypi.local"
PROJECT_PATH="/home/pi/PiClock3/"
EXECUTE_MAIN="./main.py"

rsync -avzP --delete -e ssh . $USER_AND_DOMAIN:$PROJECT_PATH
ssh $USER_AND_DOMAIN killall python3
ssh $USER_AND_DOMAIN "cd $PROJECT_PATH && $EXECUTE_MAIN &"