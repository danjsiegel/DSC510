import csv
import sys
from msds510.avenger import *
from msds510.utils.conversion import *
import operator

def readCSVData(inputCSV):
    with open(inputCSV, 'r') as avg:
        reader = csv.reader(avg)
        header = next(reader)
        for keys in range(len(header)):
            header[keys]=make_nice_name(header[keys])
        print(header)
        listOfDicts = [dict(zip(header, row)) for row in reader] #
        listOfClassesForAvengers = []
        for avenger in listOfDicts:
            listOfClassesForAvengers.append(Avenger(avenger))
if __name__ == "__main__":
    csvToRead = argumentExists(1)
    csvToCreate = argumentExists(2)
    readCSVData(csvToRead)
