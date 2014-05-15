#!/bin/bash
# extracttar.sh by iamrayw
# This script should be run with a parameter (the tar file you want to extract, directory, and logfile)
# Script will extract file within tarball
# example
# $ bash ./extract.sh tarball secondparameter somefile
# $ bash ./extract.sh <tarball file> <directory> <file>
if [ "$1" = "" ]
   then echo "Must run script with tar file name"
   else
         tarfile=$1
         directory=$2
         file=$3
         tar xf $tarfile */$directory/$file
fi
exit
