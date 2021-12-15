#!/usr/bin/python
import sys

def main():

    inFile = open(sys.argv[1])

    for row in inFile:

        rowList = row.split(';')

        # Remove first > and add trailing ;
        resString = rowList[0]
        resString = resString[1:]
        resString = resString + ";"
        
        print(resString)

    inFile.close()

main()
