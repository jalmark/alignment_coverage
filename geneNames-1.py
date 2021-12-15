#!/usr/bin/python
import sys

def main():

    inFile = open(sys.argv[1])

    outFile = open(sys.argv[2],"w")

    for row in inFile:

        rowList = row.split(';')

        # Remove first > and add trailing ;
        resString = rowList[0]
        resString = resString[1:]
        resString = resString + ";"
        
        #print(resString)
        outFile.write(resString)
        outFile.write("\n")

    inFile.close()
    outFile.close()


main()
