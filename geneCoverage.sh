#!/bin/bash

echo "Processing coverage of header $1"


#module load biokit

# filter reads
samtools view $2 $1 > output.sam

python3 singleCoverage.py $1 output.sam

