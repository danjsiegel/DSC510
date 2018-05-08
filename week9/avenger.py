import datetime
class Avenger:
    def __init__(self, record):
        """
        Initializes the object with a dictionary-based record.

        Args:
            record (dict): Dictionary-based record of Avenger data
        """
        self.data = record
        self.assignedURL = self.data['url']
        self.name = self.data['name_alias']
    def boolParser(self, toBoolValue):
        if toBoolValue == 'YES':
            return True
        elif toBoolValue == 'No':
            return False
        else:
            return None
    def url(self):
        """

        Returns:
            str: The URL of the comic character on the Marvel Wikia

        """

        return self.assignedURL

    def name_alias(self):
        """

        Returns:
            str: The full name or alias of the character

        """

        return self.name

    def appearances(self):
        """

        Returns:
            int: The number of comic books that character appeared in as of April 30

        """
        return int(self.data['appearances'])

    def is_current(self):
        """

        Returns:
            bool: Is the member currently active on an avengers affiliated team? (True/False)

        """
        return self.boolParser(self.data['current'])
    def gender(self):
        """

        Returns:
            str: The recorded gender of the character

        """
        return self.data['gender']
    def year(self):
        """

        Returns:
            int: The year the character was introduced as a full or reserve member of the Avengers

        """
        return int(self.data['year'])
    def getMonth(self, monthToParse):
        monthDict = {'Jan':1, 'Feb':2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        for key in monthDict:
            if key in monthToParse:
                return monthDict[key]
    def date_joined(self):
        """

        Returns:
            datetime.date: The date the character joined

        """
        return datetime.date(int(self.data['year']), self.getMonth(self.data['full_reserve_avengers_intro']),1)

    def dateDiffCalculator(self):
        joinDate = self.date_joined()
        today = datetime.datetime.now().date()
        difference = today - joinDate
        return difference
    def days_since_joining(self):
        """

        Returns:
            int: The number of integer days since the character joined

        """
        days = self.dateDiffCalculator()
        days = int(days/datetime.timedelta(days=1))
        return days
    def years_since_joining(self):
        """

        Returns:
            int: The number of integer years since the character joined

        """
        days = self.dateDiffCalculator()
        days = int(days/datetime.timedelta(days=365))
        return days
    def notes(self):
        """STRIP OFF TRAILING NEWLINES AND SPACES

        Returns:
            str: Descriptions of deaths and resurrections.

        """
        return (self.data['notes'].strip('\n'))
    def __str__(self):
        """

        Returns:
            str: A human-readable value for this character

        """
        return self.name

    def __repr__(self):
        """

        Returns:
            str: String representation of object.  Useful for debugging.
        """
        return 'Avenger(name_alias=%s, url=%s)' % (self.name, self.assignedURL)

if __name__ == '__main__':
    pym_record = {
        'appearances': '1269',
        'current': 'YES',
        'death1': 'YES',
        'death2': '',
        'death3': '',
        'death4': '',
        'death5': '',
        'full_reserve_avengers_intro': 'Sep-63',
        'gender': 'MALE',
        'honorary': 'Full',
        'name_alias': 'Henry Jonathan "Hank" Pym',
        'notes': 'Merged with Ultron in Rage of Ultron Vol. 1. A funeral was held. \n',
        'probationary_introl': '',
        'return1': 'NO',
        'return2': '',
        'return3': '',
        'return4': '',
        'return5': '',
        'url': 'http://marvel.wikia.com/Henry_Pym_(Earth-616)',
        'year': '1963',
        'years_since_joining': '52'
    }

    hank_pym = Avenger(pym_record)
    print('Name/Alias: {}'.format(hank_pym.name_alias()))
    print('URL: {}'.format(hank_pym.url()))
    print('Is Current?: {}'.format(hank_pym.is_current()))
    print('Gender: {}'.format(hank_pym.gender()))
    print('Year Joined: {}'.format(hank_pym.year()))
    print('Date Joined: {}'.format(hank_pym.date_joined()))
    print('Days Since Joined: {}'.format(hank_pym.days_since_joining()))
    print('Years Since Joined: {}'.format(hank_pym.years_since_joining()))
    print('Notes: {}'.format(hank_pym.notes()))
    print('__str__: {}'.format(hank_pym))
    print('__repr__: {}'.format(hank_pym.__repr__()))
