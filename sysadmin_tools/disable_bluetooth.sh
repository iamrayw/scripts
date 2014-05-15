#!/bin/bash
# disable_bluetooth.sh by iamrayw
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.blued.plist
