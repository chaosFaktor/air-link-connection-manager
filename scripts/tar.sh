#!/bin/bash

# This script will take a folder specified using the -i Flag, and create a gzip-compressed tar archive which location is specified using the -o flag

while getopts 'i:o:' OPTION; do
	case "$OPTION" in
		i)
			infile="$OPTARG"
			echo "supplied input: $OPTARG"
			;;
		o)
			outfile="$OPTARG"
			echo "wanted output: $OPTARG"
			;;

	esac
done
echo "creating compressed tar-archive"
filename=$(basename $infile)
rootdir=$(dirname $infile)


cd $rootdir
tar -cvf "$outfile" "$filename" 

#echo "$outfile" 
#echo "$filename" 
#echo "$rootdir" 