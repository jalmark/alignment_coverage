#!/usr/bin/python

# Jalmari Kettunen 16.12.2021
# This Python script take 2 arguments:
# 1) Length of wanted NCBI virus reference genome (give as integer).
# 2) Name of SAM file. There, reference genomes has a common prefix (e.g. NC_12345).

import sys

def main():
	reference = [0] * int(sys.argv[1])
	data = open(sys.argv[2], "r")
	refName = str(sys.argv[2]).rstrip(".sam")

	for i in data:

		row = i.split("\t")
		splitRefName = row[2].split(":")

		if splitRefName[1].startswith("GENE_"):
			geneStart = splitRefName[1].split("_","-")[1]
			start = int(row[3]) + int(geneStart)
			end = start + int(len(row[9]))
		else:
			start = int(row[3])
			end = start + int(len(row[9]))
			#print("Start is %d  and end is %d" %(start,end))

		for j in range(start,end+1):
			reference[j] = reference[j]+1


	with open(refName + "_data_out.txt", "w") as fileOut:
		for item in reference:
			fileOut.write("%d\n" %item)

main()

