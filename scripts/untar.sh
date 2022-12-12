#!/bin/bash

# This script will take a tar-archive specified using the -i Flag, and unpack it into a directory specified using the -o flag

while getopts 'i:o:' OPTION; do
	case "$OPTION" in
		i)
			infile="$OPTARG"
			echo "supplied input: $OPTARG"
			;;
		o)
			outdir="$OPTARG"
			echo "wanted output: $OPTARG"
			;;

	esac
done
echo "Unpacking tar-archive"
filename=$(basename $infile)
rootdir=$(dirname $infile)


cd $rootdir
if [ ! -d "$out" ]; then
    echo "creating directory(s): $outdir"
    mkdir -p "$outdir"
fi
tar -xf "$filename" -C "$outdir"

#echo "$outdir" 
#echo "$filename" 
#echo "$rootdir" 