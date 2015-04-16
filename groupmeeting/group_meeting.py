import datetime
import copy
import random

class Person:
    def __init__(self, name, position, dates, isaway=False):
        """creates person

        Args:
            name: str that describes the person's identity
            position: str that describes the person's status within group (choose b/w 'undergrad', 'masters', 'phd', 'postdoc', 'professor')
            dates: list of datetime.date instances that describe when said person presented
        """
        self._name = name
        self._position = position
        self._dates = dates
        self._future = []
        self._isaway = isaway

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
    def dates(self):
        return self._dates
    @property
    def future(self):
            return self._future
    @property
    def is_away(self):
        return self._isaway

    def add_date(self, newdate):
        """add a new date that person presented

        Args:
            newdate: datetime instance
        """
        # TODO:check if newdate is datetime instance
        # TODO:check if newdate not in self._dates
        self._dates.append(newdate)

    def add_future(self, newdate):
        """add a new date that person will present

        Args:
            newdate: datetime instance
        """
        # TODO:check if newdate is datetime instance
        # TODO:check if newdate not in self._dates
        self._future.append(newdate)
    def remove_future(self, date):
        """remove date from future

        Args:
            date: datetime instance
        """
        # TODO: check if date occurs in future only once
        if date in self.future:
            self._future.remove(date)
    def update_future_to_past(self, date):
        """moves date from future to past

        """
        # TODO: check if date is in future
        self.remove_future(date)
        self.add_date(date)



class GroupMeetings:
    def __init__(self, persons):
        """ adds all the people involved in the group meetings

        Args:
            persons: list of Person instances
        """
        self._presenters = persons
        # TODO:check if no contradicting information (more than one person present on the same day)
        self._past = {date:{'presenter':person.name, 'title':'', 'file':''} for person in persons for date in person.dates}
        self._future = {}

    @property
    def presenters(self):
        return [presenter.name for presenter in self._presenters]
    @property
    def past_presentations(self):
        dates = sorted(i for i in self._past)
        pretty = [copy.deepcopy(self._past[i]) for i in dates]
        for i,date in zip(pretty,dates): # CHECK: is i a reference to self._past?
            i['date'] = date
        return pretty
    @property
    def future_presentations(self):
        dates = sorted(i for i in self._future)
        pretty = [copy.deepcopy(self._future[i]) for i in dates]
        for i,date in zip(pretty,dates): # CHECK: is i a reference to self._past?
            i['date'] = date
        return pretty

    def find_person(self, name):
        """returns Person instance with name
        """
        for person in self._presenters:
            if person==name:
                return person

    def add_title(self, date, title):
        """ adds title to the self._past

        Args:
            date: instance of datetime
            title: str
        """
        # TODO:check if name is right
        # TODO:check if date is right
        if date in self._past:
            self._past[date]['title'] = title  # TODO: use setter?

    def add_past(self, date, presenter, title='', fileinp=''):
        """ adds to past presentations

        Args:
            date: instance of datetime
            presenter: str of person's name
            title: str
            fileinp: str
        """
        if date < datetime.date.today():
            if date not in self._past: # NOTE: not sure about this one (can there be more than one presentations per day?)
                self._past[date] = {'presenter':presenter, 'title':title, 'file':fileinp}  # TODO: use setter?
                for person in self._presenters:
                    if person == 'presenter':
                        person.add_date(date)
                        break # NOTE: assume no duplicates in presenters

    def set_future_random_one(self, date):
        """ randomly set one person to date

        Args:
            date: instance of datetime
        """
        # check if date is already assigned
        if date in self._future:
            return None

        weeks_since = []
        for person in self._presenters:
            if not person.is_away:
                if len(person.dates) > 0:
                    closest_date = abs(date-max(person.dates))
                else:
                    start_date = datetime.date(2015,2,4)
                    closest_date = abs(date-start_date)
                if len(person.future) > 0:
                    closest_date = min(closest_date, min(abs(date-i) for i in person.future))
                weeks_since.append(closest_date.days/7.)
            else:
                weeks_since.append(0)
        weights = [i if i>3 else 0 for i in weeks_since]
        probs = [weight*random.random() for weight in weights]
        probs = [prob/sum(probs) for prob in probs]
        # TODO: check if probs add up to 1
        person = max(zip(self._presenters, probs), key=lambda x:x[1])[0]
        self._future[date] = {'presenter':person.name, 'title':'', 'file':''}
        person.add_future(date)

    def set_future_one(self, date, person, title='', fileinp=''):
        """manually set one person to a date

        Args:
            date: instance of datetime
            person: instance of person
            title: str
            fileinp: str
        """
        self._future[date] = {'presenter':person.name, 'title':title, 'file':fileinp}  # TODO: use setter?
        person.add_future(date)

    def set_future_random(self, n, refdate):
        """randomly assigns people to n-1 one week intervals from refdate, including refdate

        Args:
            n: int (positive)
            refdate: instance of dattime
        """
        for i in range(n):
            date = refdate + datetime.timedelta(days=7*i)
            self.set_future_random_one(date)

    def update_future(self):
        today = datetime.date.today()
        dates_past = []
        for i in self._future:
            if i < today:
                name = self._future[i]['presenter']
                self.add_past(i, name)
                self.find_person(name).update_future_to_past(i)
                dates_past.append(i)
        for i in dates_past:
            del self._future[i]

    def remove_future(self, date):
        del self._future[date]

