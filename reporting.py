import csv
from datetime import datetime, timedelta

def readCSV(path):
    rows = []
    with open(path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)

    return rows

def printArray(arr):
    for line in arr:
        print(line)

def computeDelta(row):
    intime = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')
    outime = datetime.now()
    if row[1] != '':
        outime = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f')
    return outime - intime

def computeAllDelta(data):
    deltas = []
    total = timedelta()
    for entry in data:
        delta = computeDelta(entry)
        print(delta)
        deltas.append(delta)
    
    for delta in deltas:
        total += delta
    print(f'Total Time to Date: {total}')


if __name__ == '__main__':
    data = readCSV('timeLog.csv')

    print(computeDelta(data[0]))

    computeAllDelta(data)


