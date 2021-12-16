#!/usr/bin/python

# Jalmari Kettunen 16.12.2021
# This Python script takes 2 arguments:
# 1) Name of file that has Virosaurus 90 FASTA headers in it.
# 2) NCBI accession ID of the interesting virus genome. Will be in the name of the output file.
# This script transforms those FASTA headers into needed format and writes them in the output file.
# Name of the output file is {accession_ID}.txt.

import sys

def main():

    inFile = open(sys.argv[1], "r")

    outFile = open(sys.argv[2] + ".txt","w")

    for row in inFile:
	# Take only first member of split and remove the first character from it (which is '>').
        resString = row.split(' ')[0][1:]

        #print(resString)
        outFile.write(resString + "\n")

    inFile.close()
    outFile.close()


main()
