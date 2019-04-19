#!/usr/bin/env bash
iters=$1
outfile=$2
module=$3
func=$5
echo $(date) $module.$func >> $outfile
python3 -m timeit -n $iters "import $module" "$module.$func" >> $outfile 
tail -n 15 $outfile
