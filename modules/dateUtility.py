import datetime

def getYear(monthParse):
    monthDict = {'Jan':1, 'Feb':2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sept":9, "Oct":10, "Nov":11, "Dec":12}
    for key in monthDict:
        if key in monthParse:
            return monthDict[key]

def get_date_joined(year, monthToParse):
    return datetime.date(int(year), getYear(monthToParse), 1)

def days_since_joined(year, monthToParse):
    joindate = get_date_joined(year, monthToParse)
    today = datetime.datetime.now().date()
    difference = today - joindate
    difference = int(difference/datetime.timedelta(days=1))
    return difference
if __name__ == "__main__":
    testGetYear = getYear('14-Jan')
    print("Testing getYear with arg (14-Jan):", testGetYear)
    testGetDateJoined= get_date_joined('2013', '13-Nov')
    print("Testing get_date_joined args: ('2013', '13-Nov'):", testGetDateJoined)
    testDaysSince = days_since_joined('2013', '13-Nov')
    print("Testing days_since_joined with args ('2013', '13-Nov'):", testDaysSince)

