#!/bin/bash

set -e

if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <styledir> <outputdir> [extra options for variable replacer]"
    exit -1
fi

PATH=`npm bin`:$PATH

styledir=${1%/}
outdir=$2
sname=$outdir/`basename $styledir`.json

vname=`mktemp --suffix=.json`

lessc --variables-output=$vname $styledir/variables.less > /dev/null
variable-replacer --data=$vname $styledir/style.json $sname "${@:3}"

rm $vname
echo "Style written to $sname"
