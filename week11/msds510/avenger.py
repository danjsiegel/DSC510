import datetime
from utils.date import *
from utils.conversion import *


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
        self.appearancesInComics = int(self.data['appearances'])
        self.current_status = self.bool_parser(self.data['current'])
        self.avengerGender = self.data['gender']
        self.notesData = (self.data['notes'].strip('\n'))
        self.joinYear = int(self.data['year'])
        self.dateJoined = getDJ(self.data['full_reserve_avengers_intro'], self.joinYear)
        diff = datediffcalculator(self.dateJoined)
        self.days = int(diff/datetime.timedelta(days=1))
        self.yearsSince = int(diff/datetime.timedelta(days=365))

    def bool_parser(self, toboolvalue):
        if toboolvalue == 'YES':
            return True
        elif toboolvalue == 'No':
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
        return self.appearancesInComics

    def is_current(self):
        """
        Returns:
            bool: Is the member currently active on an avengers affiliated team? (True/False)
        """
        return self.current_status

    def gender(self):
        """
        Returns:
            str: The recorded gender of the character
        """
        return self.avengerGender

    def year(self):
        """
        Returns:
            int: The year the character was introduced as a full or reserve member of the Avengers
        """
        print('join year ', self.joinYear)
        #return self.joinYear

    def date_joined(self):
        """
        Returns:
            datetime.date: The date the character joined
        """
        return self.dateJoined

    def days_since_joining(self):
        """
        Returns:
            int: The number of integer days since the character joined
        """
        return self.days

    def years_since_joining(self):
        """
        Returns:
            int: The number of integer years since the character joined
        """
        return self.yearsSince

    def notes(self):
        """STRIP OFF TRAILING NEWLINES AND SPACES
        Returns:
            str: Descriptions of deaths and resurrections.
        """
        return self.notesData

    def __str__(self):
        """
        Returns:
            str: A human-readable value for this character
        """
        return '%s' % self.name

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
