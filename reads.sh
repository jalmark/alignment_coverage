#!/bin/bash


# filter desired accession $1 is file name $2 is accession id
samtools view $1 $2 > output.bam

# convert to sam
samtools view -h -o output.sam output.bam

python3 reads.py output.sam