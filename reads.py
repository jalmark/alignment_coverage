#!/usr/bin/python

# Jalmari Kettunen 16.12.2021
# This Python script takes 2 arguments:
# 1) Length of wanted NCBI virus reference genome (give as integer).
# 2) Name of SAM file. In there, reference genomes has a common prefix (e.g. NC_12345).
# Output is a file that has a single column: number of reads in each position.
# Its length is the given length of virus reference genome.

import sys

def main():
	# Create zero vector, length is the given reference genome length.
	reference = [0] * int(sys.argv[1])
	data = open(sys.argv[2], "r")
	refName = str(sys.argv[2]).rstrip(".sam")

	for i in data:

		row = i.split("\t")
		splitRefName = row[2].split(":")

		# If Virosaurus virus species consists of multiple reference seqs, move start position accordingly.
		if splitRefName[1].startswith("GENE_"):
			geneStart = splitRefName[1].split("_","-")[1]
			start = int(row[3]) + int(geneStart)
			end = start + int(len(row[9]))
		# If not, naively assume perfect linear alignment.
		else:
			start = int(row[3])
			end = start + int(len(row[9]))

		for j in range(start,end+1):
			reference[j] = reference[j]+1


	with open(refName + "_data_out.txt", "w") as fileOut:
		for item in reference:
			fileOut.write("%d\n" %item)

main()

