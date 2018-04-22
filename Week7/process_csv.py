import sys
import csv
from util.util import *

def readRows(inputCSV):
    with open(inputCSV,'r') as read:
        readCSV = csv.DictReader(read)
        readCSV.fieldnames = [fixHeader(header) for header in readCSV.fieldnames]
        readCSV.fieldnames.append('month_joined')
        listOfOrderedDics = []
        for row in readCSV:
            row['month_joined']=add_Month_Joined(row["full_reserve avengers intro"])
            listOfOrderedDics.append(row)
        return readCSV.fieldnames, listOfOrderedDics

def processedCSV(output, headers, input):
    with open(output, 'w', newline='') as written:
        dw = csv.DictWriter(written, fieldnames=headers)
        firstRow = {}
        for i in headers:
            firstRow[i] = i
        dw.writerow(firstRow)
        for row in input:
            cleanRecord(row, headers)
            dw.writerow(row)

if __name__ == "__main__":
    csvToRead = argumentExists(1)
    csvToCreate = argumentExists(2)
    if csvToRead and csvToCreate:
        getCSV = readRows(csvToRead)
        processedCSV(csvToCreate, getCSV[0], getCSV[1])
