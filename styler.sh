#!/bin/bash

set -e

PATH=`npm bin`:$PATH

styledir=$1
outdir=$2
sname=$outdir/`basename $styledir`.json

vname=`mktemp --suffix=.json`

lessc --variables-output=$vname $styledir/variables.less > /dev/null
variable-replacer --data=$vname $styledir/style.json $sname

rm $vname
echo "Style written to $sname"
