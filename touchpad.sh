#!/bin/bash

read touchpaddevice <<< $( xinput | sed -nre '/TouchPad|Touchpad/s/.*id=([0-9]*).*/\1/p' )
state=$( xinput list-props "$touchpaddevice" | grep "Device Enabled" | grep -o "[01]$" )

if [ "$state" -eq '1' ]; then
    xinput --disable "$touchpaddevice" && notify-send -i emblem-nowrite "Touchpad" "Disabled"
else
    xinput --enable "$touchpaddevice" && notify-send -i input-touchpad "Touchpad" "Enabled"
fi

