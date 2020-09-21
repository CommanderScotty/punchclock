import sys
from datetime import datetime

from reporting import *

def punch(punchtype, punchedIn):
    """
    Takes a timestamp, writes it to the clock in or clock out colum of the log file 
    """
    time = datetime.now()
    
    f = open('timeLog.csv', 'a')

    if punchtype == 'in':
        if punchedIn == True:
            raise Exception(f'ERROR: You must punch out before you punch in')
        f.write(f'{time},')
    elif punchtype == 'out':
        if punchedIn == False:
            raise Exception(f'ERROR: You must punch in before you punch out')
        message = input('MESSAGE: ')
        f.write(f'{time},{message}\n')
    elif punchtype == 'log':
        for line in log:
            print(line[:-1])
        data = readCSV('timeLog.csv')
        computeAllDelta(data)
    else:
        raise Exception(f'ERROR: {punchtype} is not a valid option.  Use "in" or "out"')

    f.close()

    if punchtype != 'log':
        print(f'Punching {sys.argv[1]} at {time}')


def readLog(path):
    """
    Reads a file line by line and returns it in an array
    """
    log = []
    with open(path) as f:
        for line in f:
            log.append(line)
        f.close()
    return log


def validateOption(log):
    """
    Returns true if the last line in the log has no \n character
    else, returns false
    """
    if len(log) > 0:
        return '\n' not in log[len(log) - 1]
    else:
        return False


if __name__ == '__main__':
    punchtype = sys.argv[1]
    log = readLog('timeLog.csv')
    punchedIn = validateOption(log)
    punch(punchtype, punchedIn)


