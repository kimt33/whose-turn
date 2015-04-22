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
        self._dateschair = []
        self._futurechair = []
        self._isaway = isaway
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
    def dates(self):
        return self._dates
    @property
    def future(self):
            return self._future
    @property
    def dateschair(self):
        return self._dateschair
    @property
    def futurechair(self):
        return self._futurechair
    @property
    def is_away(self):
        return self._isaway
    @property
    def email(self):
        return self._email

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

    def add_datechair(self, newdate):
        """add a new date that person chaired

        Args:
            newdate: datetime instance
        """
        # TODO:check if newdate is datetime instance
        # TODO:check if newdate not in self._dates
        self._dateschair.append(newdate)
    def add_futurechair(self, newdate):
        """add a new date that person will chair

        Args:
            newdate: datetime instance
        """
        # TODO:check if newdate is datetime instance
        # TODO:check if newdate not in self._dates
        self._futurechair.append(newdate)
    def remove_futurechair(self, date):
        """remove date from future

        Args:
            date: datetime instance
        """
        # TODO: check if date occurs in future only once
        if date in self.futurechair:
            self._futurechair.remove(date)
    def update_futurechair_to_past(self, date):
        """moves date from futurechair to past

        """
        # TODO: check if date is in future
        self.remove_futurechair(date)
        self.add_datechair(date)

    def add_email(self, email):
        self._email = email

class GroupMeetings:
    def __init__(self, persons):
        """ adds all the people involved in the group meetings

        Args:
            persons: list of Person instances
        """
        self._presenters = persons
        # TODO:check if no contradicting information (more than one person present on the same day)
        self._past = {date:{'presenter':person.name, 'title':'', 'file':'', 'chair':''} for person in persons for date in person.dates}
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
    def print_nice(self, flag='both'):
        """prints the presentations nicely

        Args:
            flag: str that is one of 'both','past','future' indicating which to print
        """
        assert flag in ['both','past','future'], 'given flag is not supported'
        # TODO: not sure how to set variable length for aligning
        # maxnamewidth = max(len(name) for name in self.presenters)
        print "{date:<12}{presenter:<20} {chair:<20} {title}".format(date='date',presenter='presenter',title='title', chair='chair')
        if flag in ['both','past']:
            for i in self.past_presentations:
                print "{date:<12}{presenter:<20} {chair:<20} {title}".format(date=str(i['date']),presenter=i['presenter'],title=i['title'], chair=i['chair'])
        if flag in ['both','future']:
            for i in self.future_presentations:
                print "{date:<12}{presenter:<20} {chair:<20} {title}".format(date=str(i['date']),presenter=i['presenter'],title=i['title'], chair=i['chair'])

    def find_person(self, name):
        """returns Person instance with name
        """
        for person in self._presenters:
            if person==name:
                return person
    def add_person(self, person):
        """adds person to presenters

        Args:
            person: instance of Person
        """
        if not self.find_person(person.name):
            self._presenters.append(person)
            for date in person.dates:
                self._past[date] = {'presenter':person.name, 'title':'', 'file':'', 'chair':''}

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
        elif date in self._future:
            self._future[date]['title'] = title  # TODO: use setter?
        else:
            print 'no one is presenting on the date given (' +str(date)+')'

    def add_chair(self, date, name):
        """ adds chair to the self._past or self._future

        Args:
            date: instance of datetime
            name: str
        """
        # TODO:check if name is right
        # TODO:check if date is right
        assert self.find_person(name), 'cannot find person with name ('+name+')'
        if date in self._past:
            self._past[date]['chair'] = name  # TODO: use setter?
            self.find_person(name).add_datechair(date)
        elif date in self._future:
            self._future[date]['chair'] = name  # TODO: use setter?
            self.find_person(name).add_futurechair(date)
        else:
            print 'no one is presenting on the date given (' +str(date)+')'

    def add_past(self, date, presenter, title='', fileinp='', chair='', flag='add'):
        """ adds to past presentations

        Args:
            date: instance of datetime
            presenter: str of person's name
            title: str
            fileinp: str
            chair: str for name of person chairing presentation
            flag: str of either 'add' or 'update'
        """
        assert flag in ['add','update'], 'given flag is not add or update'
        if date < datetime.date.today():
            if date not in self._past: # NOTE: not sure about this one (can there be more than one presentations per day?)
                self._past[date] = {'presenter':presenter, 'title':title, 'file':fileinp, 'chair':chair}  # TODO: use setter?
                if flag == 'add':
                    for person in self._presenters:
                        if person == presenter:
                            person.add_date(date)
                        if person == chair:
                            person.add_datechair(date)

    def get_weights(self, date, weight_type='presentation'):
        """ gives the weights for date

        Args:
            date: instance of datetime
            weight_type: 'presentation' or 'chair', to indicate the weight selection for presentation or chair, respectively
        Return:
            weights: weights for each person
            AssertionError: if given weight_type is not 'presentation' or 'chair'
        """
        assert weight_type in ['presentation','chair'],'given weight_type is unknown'
        weeks_since = []
        for person in self._presenters:
            if not person.is_away:
                if len(person.dates) > 0 and weight_type == 'presentation':
                    closest_date = abs(date-max(person.dates))
                elif len(person.dateschair) > 0 and weight_type == 'chair':
                    closest_date = abs(date-max(person.dateschair))
                else:
                    start_date = datetime.date(2015,2,4)
                    closest_date = abs(date-start_date)
                if len(person.future) > 0 and weight_type == 'presentation':
                    closest_date = min(closest_date, min(abs(date-i) for i in person.future))
                elif len(person.futurechair) > 0 and weight_type == 'chair':
                    closest_date = min(closest_date, min(abs(date-i) for i in person.futurechair))
                weeks_since.append(closest_date.days/7.)
            else:
                weeks_since.append(0)
        weights = [i if i>3 else 0 for i in weeks_since]
        return weights

    def set_future_random_one(self, date):
        """ randomly set one person to date

        Args:
            date: instance of datetime
        """
        # check if date is already assigned
        if date in self._future:
            return None
        # weights for presentation
        weights = self.get_weights(date)
        probs = [weight*random.random() for weight in weights]
        probs = [prob/sum(probs) for prob in probs]
        # weights for chair
        weights_chair = self.get_weights(date, weight_type='chair')
        probs_chair = [weight*random.random() for weight in weights_chair]
        probs_chair = [prob/sum(probs) for prob in probs_chair]
        # TODO: check if probs add up to 1
        person = max(zip(self._presenters, probs), key=lambda x:x[1])[0]
        person_chair = max(zip(self._presenters, probs_chair), key=lambda x:x[1])[0]
        if person != person_chair:
            self._future[date] = {'presenter':person.name, 'title':'', 'file':'', 'chair':person_chair.name}
            person.add_future(date)
            person_chair.add_futurechair(date)
        else:
            self.set_future_random_one(date)

    def set_future_one(self, date, person, title='', fileinp='', chair=''):
        """manually set one person to a date

        Args:
            date: instance of datetime
            person: instance of person
            title: str
            fileinp: str
            chair: str for name of person chairing presentation
        """
        self._future[date] = {'presenter':person.name, 'title':title, 'file':fileinp, 'chair':chair}  # TODO: use setter?
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
                presentation = self._future[i]
                name = presentation['presenter']
                namechair = presentation['chair']
                self.add_past(i, name, title=presentation['title'], fileinp=presentation['file'], chair=presentation['chair'], flag='update')
                self.find_person(name).update_future_to_past(i)
                self.find_person(namechair).update_futurechair_to_past(i)
                dates_past.append(i)
        for i in dates_past:
            self.remove_future(i)

    def remove_future(self, date):
        del self._future[date]

    def compose_emails(self, flag='reminder'):
        """writes emails in gmail format (for gmail delay send) to various people

        Args:
            flag: str that is one of 'reminder', 'announcement'
        """
        assert flag in ['reminder','announcement'], 'given flag is not supported'
        if flag == 'reminder':
            with open('email.txt','w') as f:
                for presentation in self.future_presentations:
                    for numdays in [7,3,1]:
                        date = presentation['date'] + datetime.timedelta(days=-numdays)
                        title = presentation['title']
                        if title == '':
                            title = 'N/A'
                        emails = [self.find_person(i).email for i in [presentation[j] for j in ['presenter','chair']]]
                        if numdays == 1:
                            emails.append('ayers-lab@googlegroups.com')
                        f.write(', '.join(emails)+'\n')
                        f.write('@GDS!:'+str(date)+'\n')
                        f.write('This is an automatic reminder that there is a group meeting on {date} where:\n    Presenter: {presenter}\n    Title: {title}\n    Chair: {chair}\n'.format(\
                                presenter=presentation['presenter'], chair=presentation['chair'], date=presentation['date'], title=title))
                        if presentation['title'] == '' or presentation['file'] == '':
                            f.write('When you can, could the presenter send David')
                            if presentation['title'] == '':
                                f.write(' and Pawel the title of the presentation')
                                if presentation['file'] == '':
                                    f.write(' and')
                                else:
                                    f.write('?\n')
                            if presentation['file'] == '':
                                f.write(' a copy of the presentation?\n')
                        f.write('\nThanks,\nDavid\n\n')


