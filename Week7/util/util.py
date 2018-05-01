import sys
#function to try get arguments that will not crash program if argument out of bounds
def argumentExists(index):
	'''This function takes argv positions and attempts to return them.
	In the event that an argument is out of bounds of the array, it will return a null string and prevent the program from crashing.
	Arguments are argv positions
	'''
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]

##lambda to sort list and also to return. Sorts in place and also gives you a copy if wanted
def lambsorter(listtosort):
	'''This function sorts a list of lists ascendingly based on the 3rd member. 
	It also returns the list in the event that is needed, otherwise it will sort the mutable object. 
	Arguments: mutable list
	'''
    listtosort.sort(key=lambda x: x[2], reverse=True)
    return listtosort
#Cleaning Funcs
##Clean Headers
def fixHeader(headerToFix):
	'''This function tranforms a list into lowercase, removes whitespace, and \n, ?, \,_ characters'''
    corr_category = headerToFix
    corr_category = corr_category.lower()
    corr_category = corr_category.strip('\n').strip('?').rstrip().lstrip()
    corr_category = corr_category.replace('/','_')
    return corr_category
##Clean Individual Record
def cleanRecord(recordToClean, header):
	'''This function transforms record data into the correct type'''
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
	'''This function returns an int from a string'''
    return int(stringToMakeInt)
###Clean Yes No's
def to_bool(stringToMakeBool):
	'''This function returns a true false or none based on the input of yes or no or empty string'''
    stringToMakeBool=stringToMakeBool.lower()
    if stringToMakeBool == "yes":
        return True
    elif stringToMakeBool == "no":
        return False
    else:
        return None
###Clean Notes
def clean_notes(notesToClean):
	'''This function strips off the newline character'''
    return notesToClean.strip('\n')
###Add Month Joined
def add_Month_Joined(month):
	'''This function checks to see if a month abbrevation is in the dictionary and returns either an integer representation or none'''
    monthDict = {'Jan':1, 'Feb':2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
    if month:
        for key in monthDict:
            if key in month:
                return monthDict[key]
    else:
        return None
