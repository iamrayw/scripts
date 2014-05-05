#!/bin/bash

clear;

# generate new random mac address and seve it to T1
T1="$($RANDOM | openssl md5 | sed 's/\(..\)/\1:/g' | cut -b-17)";

T1="$(openssl rand -hex 6 | sed 's/\(..\)/\1:/g; s/.$//')";



# > /dev/null 2>&1
QUERY0="$(ipconfig getpacket en0)";
QUERY1="$(ipconfig getpacket en1)";
MAC0="$(ifconfig en0 | grep ether | awk '{print $2}')";
MAC1="$(ifconfig en1 | grep ether | awk '{print $2}')";

if [ "${#MAC0}" = 17 ]; then
   echo EN0 is active with Mac Address $MAC0
else
   echo EN0 is currently not active
   fi

if [ "${#MAC1}" = 17 ]; then
   echo EN1 is active with Mac Address $MAC1
else
   echo EN1 is currently not active
   fi

if [ "${#MAC0}" = 17 ]; then
   echo Changing you wireless Mac address to $T1;
      ifconfig en0 ether $T1;
      ifconfig en0 down;
      ifconfig en0 up;
      QUERY0="$(ipconfig getpacket en0)";
      MAC0="$(ifconfig en0 | grep ether | awk '{print $2}')"
   fi

if [ "${#MAC1}" = 17 ]; then
   echo Changing you wireless Mac address to $T1;
      ifconfig en1 ether $T1;
      ifconfig en1 down;
      ifconfig en1 up;
      QUERY0="$(ipconfig getpacket en1)";
      MAC0="$(ifconfig en1 | grep ether | awk '{print $2}')"
   fi
