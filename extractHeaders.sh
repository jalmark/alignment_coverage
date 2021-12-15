#!/bin/bash

# Jalmari Kettunen 15.12.2021
# USAGE: Give 1) NCBI accession ID of the interesting virus genome and 2) BAM file of interesting sample (full path) as parameters of this Bash script.


#args=$#
# create output file
#touch temp.txt
#for (( i=3; i<=$args; i+=1 ))    # loop from 1 to N (where N is number of args)
#do
grep $1 /mnt/c/Users/-/Documents/postGradu/GTEx/Joulu20pipelineUusinta/referenssigenomit/virosaurus90_headers.txt > temp.txt
#done


python3 geneNames.py temp.txt $1

rm temp.txt

while read line; do
	echo $2
	# Processing coverage of header $line
	# Filter reads.
	samtools view $1 $2 > output.sam
	python3 reads.py $1 $2 output.sam
	rm output.sam

done < $1
