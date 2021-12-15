#!/usr/bin/python

# Jalmari Kettunen 15.12.2021
# This Python script takes 2 arguments:
# 1) Name of file that has Virosaurus 90 FASTA headers in it.
# 2) NCBI accession ID of the interesting virus genome.
# This script cleans those FASTA headers

import sys

def main():

    inFile = open(sys.argv[1])

    outFile = open(sys.argv[2],"w")

    for row in inFile:
	# Take only first member of split and remove the first character from it (which is '>').
        resString = row.split(' ')[0][1:]

        #print(resString)
        outFile.write(resString + "\n")

    inFile.close()
    outFile.close()


main()
