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
        data = [Avenger(dict(zip(header, row))) for row in reader]
        for avenger in data:
            print('Name/Alias: {}'.format(avenger.name_alias()))
            print('URL: {}'.format(avenger.url()))
            print('Is Current?: {}'.format(avenger.is_current()))
            print('Gender: {}'.format(avenger.gender()))
            print('Year Joined: {}'.format(avenger.joinYear()))
            #print('Date Joined: {}'.format(avenger.date_joined()))
            #print('Days Since Joined: {}'.format(avenger.days_since_joining()))
            #print('Years Since Joined: {}'.format(avenger.years_since_joining()))
            print('Notes: {}'.format(avenger.notes()))
            print('__str__: {}'.format(avenger))
            print('__repr__: {}'.format(avenger.__repr__()))

if __name__ == "__main__":
    csvToRead = argumentExists(1)
    csvToCreate = argumentExists(2)
    readCSVData(csvToRead)
