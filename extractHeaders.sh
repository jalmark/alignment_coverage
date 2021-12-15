#!/bin/bash

# Output file name as first parameter
# USAGE: Give accessions as command line parameters
# Will result in text file that contains all fasta-headers for these accessions

module load biokit

args=$#

# create output file
touch temp.txt

for (( i=3; i<=$args; i+=1 ))    # loop from 1 to N (where N is number of args)
do
    grep ${!i} /scratch/project_2001960/indexes/bt2VirosaurusIndices/virosaurus90_humanViruses_headers.txt >> temp.txt
done


python3 geneNames.py temp.txt $1

rm temp.txt

while read line; do
    echo $line
    # Processing coverage of header $line
    # filter reads
    samtools view $2 $line > output.sam
    python3 singleCoverage.py $line output.sam


done < $1

