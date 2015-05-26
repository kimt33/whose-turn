from person import *
import copy
import random

class GroupMeetings:
    """
    Attributes:
        _presenters: list of Person instances
        _past_presentations: dictionary of date to {presenter, title, file, chair}
        _future_presentations: dictionary of date to {presenter, title, file, chair}
    """
    def __init__(self, persons):
        """ adds all the people involved in the group meetings

        Args:
            persons: list of Person instances
        """
        self._presenters = persons
        # TODO:check if no contradicting information (more than one person present on the same day)
        self._past_presentations = {date:{'presenter':person.name, 'title':'', 'file':'', 'chair':''} for person in persons for date in person.dates_presented}
        self._future_presentations = {date:{'presenter':person.name, 'title':'', 'file':'', 'chair':''} for person in persons for date in person.dates_to_present}
        for person in persons:
            for date in person.dates_chaired:
                if date in self._past_presentations:
                    self._past_presentations[date]['chair'] = person.name
                else:
                    raise AssertionError, 'presentation in past does not exist without presenter'
            for date in person.dates_to_chair:
                if date in self._future_presentations:
                    self._future_presentations[date]['chair'] = person.name
                else:
                    self._future_presentations[date] = {'presenter':'', 'title':'', 'file':'', 'chair':person.name}

    @property
    def presenters(self):
        return [presenter.name for presenter in self._presenters]
    @property
    def past_presentations(self):
        """returns alternative dictionary of name to {presenter, title, file, chair, date}

        """
        dates = sorted(date for date in self._past_presentations)
        pretty = [copy.deepcopy(self._past_presentations[date]) for date in dates]
        for i,date in zip(pretty,dates): # CHECK: is i a reference to self._past?
            i['date'] = date
        return pretty
    @property
    def future_presentations(self):
        """returns alternative dictionary of name to {presenter, title, file, chair, date}

        """
        dates = sorted(i for i in self._future_presentations)
        pretty = [copy.deepcopy(self._future_presentations[i]) for i in dates]
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
            for date in person.dates_presented:
                if date not in self._past_presentations:
                    self._past_presentations[date] = {'presenter':person.name, 'title':'', 'file':'', 'chair':''}
                elif self._past_presentations[date]['presenter'] != person.name:
                    raise AssertionError,'presentation already exists on that date'
            for date in person.dates_chaired:
                if date in self._past_presentations:
                    self._past_presentations[date]['chair'] = person.name
                else:
                    raise AssertionError,'presentation does not exist without preseneter'
            for date in person.dates_to_present:
                if date not in self._future_presentations:
                    self._future_presentations[date] = {'presenter':person.name, 'title':'', 'file':'', 'chair':''}
                elif self._future_presentations[date]['presenter'] != person.name:
                    raise AssertionError,'presentation already exists on that date'
            for date in person.dates_to_chair:
                if date in self._future_presentations:
                    self._future_presentations[date]['chair'] = person.name
                else:
                    self._future_presentations[date] = {'presenter':'', 'title':'', 'file':'', 'chair':person.name}

    def add_title(self, date, title):
        """ adds title to a presentation

        Args:
            date: instance of datetime
            title: str
        """
        # TODO:check if name is right
        # TODO:check if date is right
        if date in self._past_presentations:
            self._past_presentations[date]['title'] = title
        elif date in self._future_presentations:
            self._future_presentations[date]['title'] = title
        else:
            print 'no one is presenting on the date given (' +str(date)+')'

    def add_chair(self, date, name):
        """ adds chair to a presentation of date

        Args:
            date: instance of datetime
            name: str
        """
        # TODO:check if name is right
        # TODO:check if date is right
        assert self.find_person(name), 'cannot find person with name ('+name+')'
        if date in self._past_presentations:
            self._past_presentations[date]['chair'] = name
            self.find_person(name).add_date_chaired(date)
        elif date in self._future_presentations:
            self._future_presentations[date]['chair'] = name
            self.find_person(name).add_date_to_chair(date)
        else:
            print 'no one is presenting on the date given (' +str(date)+')'
    def remove_chair(self, date):
        """ removes chair for the given date

        """
        # TODO:check if name is right
        # TODO:check if date is right
        if date in self._past_presentations:
            name = self._past_presentations[date]['chair']
            self.find_person(name).remove_date_chaired(date)
            self._past_presentations[date]['chair'] = ''
        elif date in self._future_presentations:
            name = self._future_presentations[date]['chair']
            self.find_person(name).remove_date_to_chair(date)
            self._future_presentations[date]['chair'] = ''
        else:
            print 'no one is presenting on the date given (' +str(date)+')'

    def add_past_presentation(self, date, name, title='', fileinp='', chair=''):
        """ adds to past presentations

        Args:
            date: instance of datetime
            name: str of person's name
            title: str
            fileinp: str describing file
            chair: str for name of person chairing presentation
        """
        # NOTE: not sure about this one (can there be more than one presentations per day?)
        if date < datetime.date.today() and date not in self._past_presentations:
            self._past_presentations[date] = {'presenter':name, 'title':title, 'file':fileinp, 'chair':chair}
            for person in self._presenters:
                if person == name:
                    person.add_date_presented(date)
                if person == chair:
                    person.add_date_chaired(date)

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
                # find closest date from past
                if len(person.dates_presented) > 0 and weight_type == 'presentation':
                    closest_date = abs(date-max(person.dates_presented))
                elif len(person.dates_chaired) > 0 and weight_type == 'chair':
                    closest_date = abs(date-max(person.dates_chaired))
                else:
                    start_date = datetime.date(2015,2,4)
                    closest_date = abs(date-start_date)
                # find closest date from future and past
                if len(person.dates_to_present) > 0 and weight_type == 'presentation':
                    closest_date = min(closest_date, min(abs(date-i) for i in person.dates_to_present))
                elif len(person.dates_to_chair) > 0 and weight_type == 'chair':
                    closest_date = min(closest_date, min(abs(date-i) for i in person.dates_to_chair))
                weeks_since.append(closest_date.days/7.)
            else:
                weeks_since.append(0)
        weights = [i if i>3 else 0 for i in weeks_since]
        return weights

    def add_future_random_one(self, date, date_type='both'):
        """ randomly set one person to date

        Args:
            date: instance of datetime
            date_type: one of ['both', 'presentation', 'chair']
        """
        # weights for presentation
        if date_type == 'both':
            self.add_future_random_one(date, date_type='presentation')
            self.add_future_random_one(date, date_type='chair')
            return None
        elif date_type == 'presentation':
            weights = self.get_weights(date, weight_type='presentation')
        elif date_type == 'chair':
            weights = self.get_weights(date, weight_type='chair')
        probs = [weight*random.random() for weight in weights]
        probs = [prob/sum(probs) for prob in probs]
        # TODO: check if probs add up to 1
        person = max(zip(self._presenters, probs), key=lambda x:x[1])[0]
        if date_type=='presentation':
            if date in self._future_presentations:
                # if person is already chairing on this date
                if person.name == self._future_presentations[date]['chair']:
                    # try again
                    self.add_future_random_one(date, date_type=date_type)
                    return None  # kill recursion here
                self._future_presentations[date]['presenter'] = person.name
            else:
                self._future_presentations[date] = {'presenter':person.name, 'title':'', 'file':'', 'chair':''}
        elif date_type=='chair':
            if date in self._future_presentations:
                # if person is already chairing on this date
                if person.name == self._future_presentations[date]['presenter']:
                    # try again
                    self.add_future_random_one(date, date_type=date_type)
                    return None  # kill recursion here
                self._future_presentations[date]['chair'] = person.name
            else:
                self._future_presentations[date] = {'presenter':'', 'title':'', 'file':'', 'chair':person.name}
        if date_type == 'presentation':
            person.add_date_to_present(date)
        elif date_type == 'chair':
            person.add_date_to_chair(date)

    def add_future_one(self, date, name_presenter='', title='', fileinp='', name_chair=''):
        """manually set one person to a date

        Args:
            date: instance of datetime
            name_presenter: str of presenter's name
            title: str
            fileinp: str
            name_chair: str for chair's name
        """
        assert name_presenter == '' or name_presenter in self.presenters
        assert name_chair == '' or name_chair in self.presenters

        if date not in self._future_presentations:
            self._future_presentations[date] = {'presenter':name_presenter, 'title':title, 'file':fileinp, 'chair':name_chair}
        else:
            if name_presenter!='':
                self._future_presentations[date]['presenter'] = name_presenter
            if title!='':
                self._future_presentations[date]['title'] = title
            if fileinp!='':
                self._future_presentations[date]['file'] = fileinp
            if name_chair!='':
                self._future_presentations[date]['chair'] = name_chair
        if name_presenter != '':
            self.find_person(name_presenter).add_date_to_present(date)
        if name_chair != '':
            self.find_person(name_chair).add_date_to_chair(date)

    def add_future_random(self, n, refdate):
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
        for date in self._future_presentations:
            if date < today:
                presentation = self._future_presentations[date]
                name_presenter = presentation['presenter']
                name_chair = presentation['chair']
                self.add_past_presentation(date, name_presenter, title=presentation['title'], fileinp=presentation['file'], chair=presentation['chair'])
                if name_presenter != '':
                    self.find_person(name_presenter).update_date_to_present_to_presented(date)
                if name_chair != '':
                    self.find_person(name_chair).update_date_to_chair_to_chaired(date)
                dates_past.append(date)
        for date in dates_past:
            self.remove_future(date)

    def remove_future(self, date):
        if date in self._future_presentations:
            presenter_name = self._future_presentations[date]['presenter']
            self.find_person(presenter_name).remove_date_to_present(date)
            chair_name = self._future_presentations[date]['chair']
            self.find_person(chair_name).remove_date_to_chair(date)
            del self._future_presentations[date]

    def compose_emails(self):
        """writes emails in gmail format (for gmail delay send) to various people

        """
        with open('email.txt','w') as f:
            for presentation in self.future_presentations:
                for numdays in [7,3,1]:
                    date = presentation['date'] + datetime.timedelta(days=-numdays)
                    title = presentation['title']
                    if title == '':
                        title = 'N/A'
                    emails = [self.find_person(i).email for i in ['David Kim', 'Cristina Gonzalez', 'Ramon Miranda']]
                    emails += [self.find_person(i).email for i in [presentation[j] for j in ['presenter','chair']]]
                    if numdays in [3,1]:
                        emails.append('ayers-lab@googlegroups.com')
                    f.write('Group Presentation: '+presentation['presenter'].split()[0]+'\n')
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

    def store_people(self):
        import pickle
        for person in self._presenters:
            name = person.name
            filename = '_'.join(name.lower().split())+'.p'
            pickle.dump(person,open('./people/'+filename,'w'))

