#!/bin/bash 
echo "This script is to be used for generating SSH certificates only."

read -p "Bits (default: 8192): " bits

	if [ -z "$bits" ]; then
	    bits=8192
	fi
	 
read -p "Encryption Type (default: rsa): " enc
	 
if [ -z "$enc" ]; then
    enc="rsa"
fi
 
read -p "File (default: $HOME/.ssh/id_$enc): " path

if [ -z "$path" ]; then
    path="$HOME/.ssh/id_$enc"
fi
 
if [ -e "$path" ]; then
    read -p "$path already exists...delete? (Y/n): " ans

   case "$ans" in
      N|n)
          echo "File must be deleted first."
          exit 1
       ;;

        Y|y|*)
            rm -rf $path
        ;;
    esac
fi
 
stty -echo
read -p "Passphrase: " pp
stty echo

if [ "${#pp}" -lt 4 ]; then
    echo -e "\nPassphrase must be greater than 4 characters."
    exit 1
fi
 
echo -e -n "\nGenerating a $bits bit $enc SSH key file in $path..."
 
ssh-keygen -q -b $bits -t $enc -N $pp -f "$path"
 
if [ -e "$path" ]; then
    echo "SUCCESS"
    else
    echo "FAIL"
fi 
exit 0
