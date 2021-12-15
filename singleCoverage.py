#!/usr/bin/python
import sys

def main():
    
    fileName = sys.argv[1]


    splittedFN = fileName.split("_")
    nucleotideRange = splittedFN[1]
    
    coords = nucleotideRange.split("-")
    start = coords[1]
    end = coords[0]
    
    length = int(start)-int(end)

    if length > 0:
	
        bamData = open(sys.argv[2])

        readList = []*length
        
        for row in bamData:
            rivi=row.split("\t")
            
            if(len(rivi)>3):
                print(rivi[3]+" "+rivi[7])
        print("Length of reference sequence: " +str(length) +" bp")

    #inFile = open(sys.argv[1])
    
    #outFile = 




main()
