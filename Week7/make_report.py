import csv
import sys
from util.util import *

def readCSVData(inputCSV):
    with open(inputCSV, 'r') as avg:
        reader = csv.reader(avg)
        data = list(list(rec) for rec in csv.reader(avg, delimiter=','))
    headers = data[0]
    data.pop(0) #pops off headers
    for rows in data:
        rows[2]=int(rows[2])
    lambsorter(data)
    topAvengers = data[0:10]
    return topAvengers

def markdownWriter(outputMDFile, topTenAvengers):
    with open(outputMDFile, 'w') as mdWriter:
        for record in range(len(topTenAvengers)):
            mdWriter.writelines(("#",str((record+ 1))+". ", topTenAvengers[record][1], '\n\n'))
            mdWriter.writelines(("*Number of Appearances:", str(topTenAvengers[record][2]), '\n'))
            mdWriter.writelines(("*Year Joined:", str(topTenAvengers[record][7]), '\n'))
            mdWriter.writelines(("*Years Since Joining:", str(topTenAvengers[record][8]), '\n'))
            mdWriter.writelines(("*URL:", topTenAvengers[record][0], '\n\n'))
            mdWriter.writelines(("## Notes\n\n"+topTenAvengers[record][20], '\n\n'))

if __name__ == "__main__":
    inputCSV = argumentExists(1)
    outPutMarkdown = argumentExists(2)
    if inputCSV and outPutMarkdown:
        top = readCSVData(inputCSV)
        markdownWriter(outPutMarkdown, top)
