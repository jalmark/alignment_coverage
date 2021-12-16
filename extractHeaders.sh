#!/bin/bash

# Jalmari Kettunen 15.12.2021
# USAGE: This Bash script must be given 3 arguments:
# 1) NCBI accession ID of the interesting virus genome
# 2) BAM file of interesting sample (full path) as parameters of this Bash script.
# 3) Length of the NCBI reference genome which corresponds NCBI accession ID.

args=$#
# create output file
#touch temp.txt
#for (( i=3; i<=$args; i+=1 ))    # loop from 1 to N (where N is number of args)
#do
grep $1 /mnt/c/Users/-/Documents/postGradu/GTEx/Joulu20pipelineUusinta/referenssigenomit/virosaurus90_headers.txt > temp.txt
#done


python3 geneNames.py temp.txt $1

rm temp.txt

while read line; do
	echo line
	# Filter reads.
	samtools view $2 line >> "{$1}.sam"
done < "{$1}.txt"

python3 reads.py $3 "{$1}.sam"
