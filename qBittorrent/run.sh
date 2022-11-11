#!/bin/bash

if [ -f "/config/rclone-upload.sh" ]; then
	echo
else
	wget -O /config/rclone-upload.sh https://github.com/kissyouhunter/Tools/raw/main/rclone/rclone-upload.sh
	chmod +x /config/rclone-upload.sh
fi

cd /app && python main.py 
