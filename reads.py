#!/usr/bin/python
import sys

def main():

    reads = [0] * int(sys.argv[2])

    data = open(sys.argv[1]) 

    for i in data:

        row = i.split("\t")

        start = int(row[3])
        end = int(row[7])

        if(start < end):
            for j in range(start,end+1):
                reads[j] = reads[j]+1


    with open("data_out.txt", "w") as fileOut:
        for item in reads:
            fileOut.write("%d\n" %item)



main()
