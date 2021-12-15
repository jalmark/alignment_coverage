#!/usr/bin/python
import sys

def main():
	reads = [0] * int(sys.argv[2])

	data = open(sys.argv[1], "r")

	for i in data:

        	row = i.split("\t")

        	start = int(row[3])
        	end = start + int(len(row[9]))
        	#print("Start is %d  and end is %d" %(start,end))

        	#if start < end:
        	for j in range(start,end+1):
            		reads[j] = reads[j]+1


	with open("data_out.txt", "w") as fileOut:
		for item in reads:
			fileOut.write("%d\n" %item)

main()

