import datetime

def getmonth(monthtoparse):
    '''
    :param monthtoparse: month in which avenger joined
    :return: the numerical reference of the month
    '''
    monthdict = {'Jan': 1, 'Feb': 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
    for key in monthdict:
        if key in monthtoparse:
            return monthdict[key]
def datediffcalculator(joinDate):
    '''
    :param joinDate: Date to calculate time elapsed since
    :return: Time elapsed since joinDate
    '''
    today = datetime.datetime.now().date()
    difference = today - joinDate
    return difference

def getDJ(inMonth, inYear):
    try:
        returnYear = datetime.date(int(inYear), getmonth(inMonth), 1)
    except:
        return
    else:
        return returnYear
