import datetime


def to_int(stringtomakeint):
    try:
        return int(stringtomakeint)
    except:
        return None

def get_value(values, checker):
    try:
        return values[checker]
    except:
        try:
            return values.index(checker)
        except:
            return None

def get_year(month_parse):
    month_dict = {'Jan': 1, 'Feb': 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
                  "Jul": 7, "Aug": 8, "Sep": 9, "Sept": 9, "Oct": 10, "Nov": 11, "Dec": 12}
    for key in month_dict:
        if key in month_parse:
            return month_dict[key]

def get_date_joined(year, month_to_parse):
    return datetime.date(int(year), get_year(month_to_parse), 1)
