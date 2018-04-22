import sys
#function to try get arguments that will not crash program if argument out of bounds
def argumentExists(index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]
#Cleaning Funcs
##Clean Headers
def fixHeader(headerToFix):
    corr_category = headerToFix
    corr_category = corr_category.lower()
    corr_category = corr_category.strip('\n').strip('?').rstrip().lstrip()
    corr_category = corr_category.replace('/','_')
    return corr_category
##Clean Individual Record
def cleanRecord(recordToClean, header):
    for keys in header:
        if keys == 'appearances' or keys == 'year':
            recordToClean[keys]=to_int(recordToClean[keys])
        if keys == 'current' or keys.startswith('return') or keys.startswith('death'):
            recordToClean[keys]=to_bool(recordToClean[keys])
        if keys == 'notes':
            recordToClean[keys]=clean_notes(recordToClean[keys])
        if keys == 'years since joining':
            recordToClean[keys] = (2018 - to_int(recordToClean['year']))
###Clean Int Values
def to_int(stringToMakeInt):
    return int(stringToMakeInt)
###Clean Yes No's
def to_bool(stringToMakeBool):
    stringToMakeBool=stringToMakeBool.lower()
    if stringToMakeBool == "yes":
        return True
    elif stringToMakeBool == "no":
        return False
    else:
        return None
###Clean Notes
def clean_notes(notesToClean):
    return notesToClean.strip('\n')
###Add Month Joined
def add_Month_Joined(month):
    monthDict = {'Jan':1, 'Feb':2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
    if month:
        for key in monthDict:
            if key in month:
                return monthDict[key]
    else:
        return None
