import datetime

class Person:
    """
    Attributes:
        _name: str that describes the person's identity
        _position: str that describes the person's status within group (choose b/w 'undergrad', 'masters', 'phd', 'postdoc', 'professor')
        _dates_presented: list of datetime.date instances that describe when said person presented
        _dates_to_present: list of datetime.date instances that describe when said person will present in the future
        _dates_chaired: list of datetime.date instances that describe when said person chaired
        _dates_to_chair: list of datetime.date instances that describe when said person will chair in the future
        _dates_away: list of tuples that describe when (from and (optional)to) the person is away
    """
    def __init__(self, name, position, dates_presented=[], dates_chaired=[], dates_away=[]):
        """creates person

        Args:
            name: str that describes the person's identity
            position: str that describes the person's status within group (choose b/w 'undergrad', 'masters', 'phd', 'postdoc', 'professor')
            dates_presented: list of datetime.date instances that describe when said person presented
            dates_chaired: list of datetime.date instances that describe when said person chaired
            dates_away: list of tuples that describe when (from and (optional)to) the person is away
        """
        self._name = name
        self._position = position
        self._dates_presented = dates_presented
        self._dates_to_present = []
        self._dates_chaired = dates_chaired
        self._dates_to_chair = []
        self._dates_away = dates_away
        self._email = ''

    def __eq__(self, other):
        """ returns true if other is the name of person else false

        Args:
            other: str indicating persons name
        """

        if self.name == other:
            return True
        else:
            return False

    @property
    def name(self):
        return self._name
    @property
    def position(self):
        return self._position
    @property
    def dates_presented(self):
        return self._dates_presented
    @property
    def dates_to_present(self):
        return self._dates_to_present
    @property
    def dates_chaired(self):
        return self._dates_chaired
    @property
    def dates_to_chair(self):
        return self._dates_to_chair
    @property
    def email(self):
        return self._email
    @property
    def dates_away(self):
        return self._dates_away

    def is_away(self, date=datetime.date.today()):
        for date_range in self.dates_away:
            if len(date_range)==1 and date_range[0] <= date:
                return True
            if len(date_range)==2 and date_range[0] <= date <= date_range[1]:
                return True
        else:
            return False

    def add_date_presented(self, newdate):
        """add a new date that person presented

        Args:
            newdate: datetime instance
        """
        # TODO:check if newdate is datetime instance
        if newdate not in self.dates_presented:
            self._dates_presented.append(newdate)
    def remove_date_presented(self, date):
        """remove date that person presented

        Args:
            date: datetime instance
        """
        # TODO: check if date occurs in dates_to_present only once
        if date in self.dates_presented:
            self._dates_presented.remove(date)

    def add_date_to_present(self, newdate):
        """add a new date that person will present

        Args:
            newdate: datetime instance
        """
        # TODO:check if newdate is datetime instance
        if newdate not in self.dates_to_present:
            self._dates_to_present.append(newdate)
    def remove_date_to_present(self, date):
        """remove date that person will present

        Args:
            date: datetime instance
        """
        # TODO: check if date occurs in dates_to_present only once
        if date in self.dates_to_present:
            self._dates_to_present.remove(date)
    def update_date_to_present_to_presented(self, date):
        """moves date from dates_to_present to dates_presented

        """
        if date in self.dates_to_present:
            self.remove_date_to_present(date)
            self.add_date_presented(date)

    def add_date_chaired(self, newdate):
        """add a new date that person chaired

        Args:
            newdate: datetime instance
        """
        # TODO:check if newdate is datetime instance
        if newdate not in self.dates_chaired:
            self._dates_chaired.append(newdate)
    def remove_date_chaired(self, date):
        """remove date that person chaired

        Args:
            date: datetime instance
        """
        # TODO: check if date occurs in dates_to_present only once
        if date in self.dates_chaired:
            self._dates_chaired.remove(date)
    def add_date_to_chair(self, newdate):
        """add a new date that person will chair

        Args:
            newdate: datetime instance
        """
        # TODO:check if newdate is datetime instance
        if newdate not in self.dates_to_chair:
            self._dates_to_chair.append(newdate)
    def remove_date_to_chair(self, date):
        """remove date that person will chair

        Args:
            date: datetime instance
        """
        # TODO: check if date occurs in dates_to_present only once
        if date in self.dates_to_chair:
            self._dates_to_chair.remove(date)
    def update_date_to_chair_to_chaired(self, date):
        """moves date from dates_to_chair to dates_chaired

        Args:
            date: datetime instance
        """
        if date in self.dates_to_chair:
            self.remove_date_to_chair(date)
            self.add_date_chaired(date)

    def add_email(self, email):
        """adds email to person

        Args:
            email: str of person's email
        """
        self._email = email
