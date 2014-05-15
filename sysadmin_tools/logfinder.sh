#!/bin/bash
#This script should be run with a parameter (the tar file you want to find)
# example
# $ bash ./locate.sh somedate somefile
if [ "$1" = ""]
	else
	then echo "Must run script with date and file name"
		date=$1
		logfile=$2
	find /some/directory/all.$date.tar.gz  -type f -name "*.tar.gz" -printf [%f]\\n -exec tar -ztvf {} \; | grep -iE "[\[]|*$logfile.log"
fi
exit