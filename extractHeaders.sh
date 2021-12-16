#!/bin/bash

# Jalmari Kettunen 15.12.2021
# USAGE: This Bash script must be given 3 arguments:
# 1) NCBI accession ID of the interesting virus genome
# 2) BAM file of interesting sample (full path) as parameters of this Bash script.
# 3) Length of the NCBI reference genome which corresponds NCBI accession ID.
# In the end, reads.py creates file {accession_ID}_data_out.txt.
# This file can be visualized by importing it into R (see R script reads.R).


grep $1 /mnt/c/Users/-/Documents/postGradu/GTEx/Joulu20pipelineUusinta/referenssigenomit/virosaurus90_headers.txt > temp.txt

echo "running geneNames.py"
python3 geneNames.py temp.txt $1


touch "${1}.sam"

echo "These Virosaurus references match the given NCBI accession ID:"
while IFS= read -r line; do
	printf '%s\n' "$line"
	# Filter reads.
	samtools view $2 "$line" >> "${1}.sam"
done < "${1}.txt"

echo "running reads.py"
python3 reads.py $3 "${1}.sam"

# Clean
rm temp.txt
rm "${1}.txt"
rm "${1}.sam"
