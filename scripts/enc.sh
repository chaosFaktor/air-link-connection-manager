#!/bin/bash

# This script will symmetically encrypt a file specified using the -i Flag, using a passphrase provided by the -p Flag, and save the encrypted file in a location provided by the -o flag

while getopts 'i:o:p:' OPTION; do
	case "$OPTION" in
		i)
			infile="$OPTARG"
			echo "supplied input: $OPTARG"
			;;
		o)
			outfile="$OPTARG"
			echo "wanted output: $OPTARG"
			;;
        p)
            passphrase="$OPTARG"
            echo "read secret passphrase"
            ;;

	esac
done
filename=$(basename $infile)
rootdir=$(dirname $infile)


echo "encrypting file stored in $rootdir"
cd $rootdir
gpg --passphrase "$passphrase" -o "$outfile" "$infile"

#echo "$outfile" 
#echo "$filename" 
#echo "$rootdir" 