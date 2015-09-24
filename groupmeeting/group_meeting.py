from person import Person
from presentation import Presentation, PresentationStorage
import datetime
import copy
import random

class GroupMeetings(object):
    """
    Attributes
    ----------
    _presenters: list of Person instances
        All the people that presents will be represented by a Person instance
    _past_presentations : list of Presentation instances
        Each past presentation is represented by a Presentation instance
    _future_presentations : list of Presentation instances
        Each future presentation is represented by a Presentation instance
    """
    def __init__(self, persons):
        """ adds all the people involved in the group meetings

        Parameters
        ----------
        persons : list of Person instances
        """
        self._presenters = list(persons)
        self._past_presentations = PresentationStorage([Presentation(date, presenter=person)
                                                        for person in persons
                                                        for date in person.dates_presented])
        self._future_presentations = PresentationStorage([Presentation(date, presenter=person)
                                                          for person in persons
                                                          for date in person.dates_to_present])
        for person in persons:
            for date in person.dates_chaired:
                matches = self._past_presentations.find_presentations(date=date)
                assert len(matches)==1, '''Unsupported number of presentations,{0},
                                        on this date, {1}'''.format(len(matches), date)
                matches[0].chair = person
            for date in person.dates_to_chair:
                matches = self._future_presentations.find_presentations(date=date)
                assert len(matches) in [0,1], 'Unsupported number of\
                presentations,{0}, on this date, {1}'.format(len(matches), date)
                if len(matches) == 0:
                    new_presentation = Presentation(date, chair=person)
                    self._future_presentations.add_presentation(new_presentation)
                elif len(matches) == 1:
                    matches[0].chair = person

    @property
    def presenters(self):
        return [presenter.name for presenter in self._presenters]

    @property
    def past_presentations(self):
        """ Returns information on the past presentations, ordered by date

        Returns
        -------
        past_presentations : list of dictionary
            __dict__ of each presentation
        """
        ordered_past = self._past_presentations.ordered_date()
        return [i.__dict__ for i in ordered_past]

    @property
    def future_presentations(self):
        """ Returns information on the future presentations, ordered by date

        Returns
        -------
        future_presentations : list of dictionary
            __dict__ of each presentation
        """
        ordered_future = self._future_presentations.ordered_date()
        return [i.__dict__ for i in ordered_future]

    def print_nice(self, flag='both'):
        """prints the presentations nicely

        Parameters
        ----------
        flag : {'both', 'past', 'future'}
            controls which presentations to print
        """
        assert flag in ['both','past','future'], 'given flag is not supported'
        # TODO: not sure how to set variable length for aligning
        # maxnamewidth = max(len(name) for name in self.presenters)
        print "{date:<12}{presenter:<20} {chair:<20} {title}".format(date='date',
                                                                     presenter='presenter',
                                                                     chair='chair',
                                                                     title='title')
        if flag in ['both','past']:
            for presentation in self._past_presentations.ordered_date():
                print presentation
        if flag in ['both','future']:
            for presentation in self._future_presentations.ordered_date():
                print presentation

    def find_person(self, name):
        """ Returns Person instance that corresponds to the name

        Parameters
        ----------
        name : str
            Name of the person you are trying to find
        """
        for person in self._presenters:
            if person == name:
                return person

    def add_person(self, person):
        """ Adds person to presenters

        Parameters
        ----------
        person : Person

        Raises
        ------
        AssertionError
            If person already is added
        """
        assert not self.find_person(person.name)
        self._presenters.append(person)
        for date in person.dates_presented:
            self.add_past_presentation(date=date, presenter=person)
        for date in person.dates_to_present:
            self.add_future_one(date, presenter=person)
        for date in person.dates_chaired:
            self.add_chair(date, person)
        for date in person.dates_to_chair:
            self.add_chair(date, person)

    def _change_presentation_attribute(self, attribute, value,
                                       date=None, presenter=None, chair=None, title=''):
        """ Adds/replaces or removes the attribute from the presentation that
        matches the given date, presenter, chair, or title

        Parameters
        ----------
        attribute : str
            Name of the attribute that is going to be changed
        value : {datetime.date, Person, str}
            New value of the attribute
            Setting the value to the default value (date=None, presenter=None,
            chair=None, and title='') would remove the attribute from the
            presentation
        date : {None, datetime.date}
        presenter : {None, Person, str}
        chair : {None, Person, str}
        title : {'', str}

        Raises
        ------
        AssertionError
            If more than one presentations are found
        """
        if isinstance(presenter, str):
            presenter = self.find_person(presenter)
        if isinstance(chair, str):
            chair = self.find_person(chair)
        matches_past = self._past_presentations.find_presentations(date=date,
                                                                   presenter=presenter,
                                                                   chair=chair,
                                                                   title=title)
        matches_future = self._future_presentations.find_presentations(date=date,
                                                                       presenter=presenter,
                                                                       chair=chair,
                                                                       title=title)
        assert len(matches_past)+len(matches_future)<=1, 'Too many\
        presentations to assign'
        for presentation in matches_past:
            setattr(presentation, attribute, value)
        for presentation in matches_future:
            setattr(presentation, attribute, value)

    def replace_date(self, to_date, from_date=None, presenter=None, chair=None, title=''):
        """ Replaces date of a presentation with attributes presenter,
        chair or title

        Parameters
        ----------
        to_date : datetime.date
        from_date : {None, datetime.date}
        presenter : {None, Person, str}
        chair : {None, Person, str}
        title : {'', str}
        """
        self._change_presentation_attribute('date', to_date, date=from_date,
                                            presenter=presenter,
                                            chair=chair, title=title)

    def add_presenter(self, person, date=None, chair=None, title=''):
        """ Adds/Replaces presenter of a presentation with attributes date,
        chair or title

        Parameters
        ----------
        person : {str, Person}
        date : {None, datetime.date}
        chair : {None, Person, str}
        title : {'', str}

        Raises
        ------
        AssertionError
            If person cannot be found by the name given
        """
        if isinstance(person, str):
            assert self.find_person(person), 'Cannot find person with name, {0}'.format(name)
            person = self.find_person(person)
        self._change_presentation_attribute('presenter', person, date=date,
                                            chair=chair, title=title)

    def remove_presenter(self, date=None, presenter=None, chair=None, title=''):
        """ Removes presenter of a presentation with attributes date,
        chair or title

        Parameters
        ----------
        date : {None, datetime.date}
        presenter : {None, Person}
        chair : {None, Person}
        title : {'', str}
        """
        self._change_presentation_attribute('presenter', None, date=date,
                                            presenter=presenter, chair=chair,
                                            title=title)

    def add_chair(self, person, date=None, presenter=None, title=''):
        """ Adds/Replaces chair of a presentation with attributes date,
        chair or title

        Parameters
        ----------
        person : {str, Person}
        date : {None, datetime.date}
        presenter : {None, Person}
        title : {'', str}

        Raises
        ------
        AssertionError
            If person cannot be found by the name given
        """
        if isinstance(person, str):
            assert self.find_person(person), 'Cannot find person with name, {0}'.format(name)
            person = self.find_person(person)
        self._change_presentation_attribute('chair', person, date=date,
                                            presenter=presenter, title=title)

    def remove_chair(self, date=None, chair=None, presenter=None, title=''):
        """ Removes chair of a presentation with attributes date,
        chair or title

        Parameters
        ----------
        date : {None, datetime.date}
        chair : {None, Person}
        presenter : {None, Person}
        title : {'', str}
        """
        self._change_presentation_attribute('chair', None, date=date,
                                            presenter=presenter, chair=chair,
                                            title=title)

    def add_title(self, title, date=None, presenter=None, chair=None):
        """ Adds/Replaces title to a presentation with attributes date,
        chair or title

        Parameters
        ----------
        title : str
        date : {None, datetime.date}
        presenter : {None, Person}
        chair : {None, Person}
        """
        self._change_presentation_attribute('title', title, date=date,
                                            presenter=presenter, chair=chair)

    def remove_title(self, date=None, title='', presenter=None, chair=None):
        """ Removes title from a presentation with attributes date,
        chair or title

        Parameters
        ----------
        date : {None, datetime.date}
        title : {'', str}
        presenter : {None, Person, str}
        chair : {None, Person, str}
        """
        self._change_presentation_attribute('title', '', date=date,
                                            presenter=presenter, chair=chair)

    def add_past_presentation(self, date=None, presenter=None, chair=None, title='',
                              presentation=None):
        """ Adds presentation to past presentation

        Parameters
        ----------
        date : {None, datetime.date}
        presenter : {None, Person, str}
        chair : {None, Person, str}
        title : {'', str}
        presentation : {None, Presentation}

        Raises
        ------
        AssertionError
            If both presentation and the parameters (date, presenter, chair or
            title) are given
            If date of presentation is in the future
        """
        assert ((date is not None or presenter is not None or chair is not None or
                title != '') != (presentation is not None)), 'Both the presentation and the\
                parameters (date, presenter, chair, or title) are given'
        if isinstance(presenter, str):
            presenter = self.find_person(presenter)
        if isinstance(chair, str):
            chair = self.find_person(chair)
        if date is not None:
            presentation = Presentation(date, presenter, chair, title)
        assert presentation.date < datetime.date.today(), 'The presentation\
        takes place in the future'
        if presentation._presenter is not None:
            presentation._presenter.add_date_presented(presentation.date)
        if presentation._chair is not None:
            presentation._chair.add_date_chaired(presentation.date)
        self._past_presentations.add_presentation(presentation)

    def get_weights(self, date, weight_type='presenter'):
        """ Assigns weights for the weighed probability distribution

        Parameters
        ----------
        date : datetime.date
        weight_type : {'presenter', 'chair'}
            'presentation' gives weights for the presenter
            'chair' gives weights for the chair

        Returns
        -------
        weights
            weights for each person

        Raises
        ------
        AssertionError
            If weight_type is not 'presenter' or 'chair'
        """
        assert weight_type in ['presenter', 'chair'], 'Given weight_type is not\
        supported'
        weeks_since = []
        for person in self._presenters:
            if (not person.is_away(date) and 
                person.position not in ['undergrad', 'visiting', 'professor']):
                if weight_type == 'presenter':
                    dates_past = person.dates_presented +\
                                 [i for i in person.dates_to_present if i<date]
                elif weight_type == 'chair':
                    dates_past = person.dates_chaired +\
                                 [i for i in person.dates_to_chair if i<date]
                num_weeks = datetime.timedelta(days=15)
                if len(dates_past) != 0:
                    num_weeks = min((date-dates_past[-1])/7, num_weeks)
                weeks_since.append(num_weeks.days)
            else:
                weeks_since.append(0.)
        weights = [i if i>3 else 0. for i in weeks_since]
        return weights

    def add_future_random_one(self, date, job_type='both'):
        """ Randomly select a person on date to present and/or chair

        Parameters
        ----------
        date : datetime.date
        job_type : {'both', 'presenter', 'chair'}
        """
        # weights for presentation
        if job_type == 'both':
            self.add_future_random_one(date, job_type='presenter')
            self.add_future_random_one(date, job_type='chair')
            return None
        elif job_type == 'presenter':
            weights = self.get_weights(date, weight_type='presenter')
        elif job_type == 'chair':
            weights = self.get_weights(date, weight_type='chair')
        probs = [weight*random.random() for weight in weights]
        probs = [prob/sum(probs) for prob in probs]
        person = max(zip(self._presenters, probs), key=lambda x:x[1])[0]
        if job_type=='presenter':
            matches = self._future_presentations.find_presentations(date=date)
            if len(matches) != 0:
                # if person is already chairing on this date
                if len([i for i in matches if i.chair==person]) != 0:
                    # try again
                    self.add_future_random_one(date, job_type=job_type)
                    return None  # kill recursion here
                self.add_presenter(person, date=date)
            else:
                self.add_future_one(date, presenter=person)
        elif job_type=='chair':
            matches = self._future_presentations.find_presentations(date=date)
            if len(matches) != 0:
                # if person is already presenting on this date
                if len([i for i in matches if i.presenter==person]) != 0:
                    # try again
                    self.add_future_random_one(date, job_type=job_type)
                    return None  # kill recursion here
                self.add_chair(person, date=date)
            else:
                self.add_future_one(date, chair=person)

    def add_future_one(self, date, presenter=None, chair=None, title=''):
        """ Manually select a person to persent/chair

        Parameters
        ----------
        date : datetime.date
        presenter : {None, Person, str}
        chair: {None, Person, str}
        title: {'', str}

        Raise
        -----
        AssertionError
            If presenter is not in the list of presenters
            If chair is not in the list of presenters
        """
        if isinstance(presenter, str):
            presenter = self.find_person(presenter)
        if isinstance(chair, str):
            chair = self.find_person(chair)
        assert presenter is None or presenter.name in self.presenters
        assert chair is None or chair.name in self.presenters
        matches = self._future_presentations.find_presentations(date=date)
        if len(matches) == 0:
            new_presentation = Presentation(date=date, presenter=presenter,\
                                            chair=chair, title=title)
            if presenter is not None:
                presenter.add_date_to_present(date)
            if chair is not None:
                chair.add_date_to_chair(date)
            self._future_presentations.add_presentation(new_presentation)
        else:
            if isinstance(presenter, Person):
                self.add_presenter(presenter, date=date)
            if isinstance(chair, Person):
                self.add_chair(chair, date=date)
            if title != '':
                self.add_title(title, date=date)

    def add_future_random(self, n, from_date):
        """ Randomly select people to present and chair for some number of weeks
        from some date

        Parameters
        ----------
        n : int
        from_date : datetime.date
        """
        for i in range(n):
            date = from_date + datetime.timedelta(days=7*i)
            self.add_future_random_one(date)

    def remove_presentation(self, date=None, presenter=None, chair=None, title=''):
        """ Removes a presentation that has the given properties

        Parameters
        ----------
        date : {None, datetime.date}
        presenter : {None, Person, str}
        chair : {None, Person, str}
        title : {'', str}

        Raises
        ------
        AssertionError
            If there are more than one presentation that matches the given
            parameters
        """
        if isinstance(presenter, str):
            presenter = self.find_person(presenter)
        if isinstance(chair, str):
            chair = self.find_person(chair)
        matches_past = self._past_presentations.find_presentations(date=date,
                                                                   presenter=presenter,
                                                                   chair=chair,
                                                                   title=title)
        matches_future = self._future_presentations.find_presentations(date=date,
                                                                       presenter=presenter,
                                                                       chair=chair,
                                                                       title=title)
        assert len(matches_past)+len(matches_future)<=1, 'Too many\
        presentations to assign'
        for presentation in matches_past:
            self._past_presentations.remove_presentation(presentation)
        for presentation in matches_future:
            self._future_presentations.remove_presentation(presentation)

    def update_future(self):
        """ Moves the presentations from future presentations to past
        presentations if the current date is past the dates of the future
        presentations
        """
        today = datetime.date.today()
        for presentation in self._future_presentations.presentations:
            date = presentation.date
            if date < today:
                self._future_presentations.remove_presentation(presentation)
                self._past_presentations.add_presentation(presentation)

    def compose_emails(self):
        """ Writes emails in gmail format (for gmail delay send) to people involved
        in the presentation

        1 week and 3 days before the presentation, the presenter, the chair, David,
        Marco, Ahmed, Yilin, and Pawel are notified
        1 day before the presentation, Ayers lab is notified

        """
        with open('email.txt','w') as f:
            for presentation in self.future_presentations:
                for numdays in [7,3,1]:
                    date = presentation['date'] + datetime.timedelta(days=-numdays)
                    title = presentation['title']
                    if title == '':
                        title = 'N/A'
                    emails = [self.find_person(name).email for name in
                              ['David Kim', 'Marco Franco', 'Ahmed Kamel']]
                    emails += [self.find_person(name).email for name in
                               [presentation[j] for j in ['presenter','chair']]]
                    if numdays in [3,1]:
                        emails.append('ayers-lab@googlegroups.com')
                    f.write(', '.join(emails)+'\n')
                    f.write('Group Presentations: {0}\n'.\
                            format(presentation['presenter'].split()[0]))
                    f.write('@GDS!:{0}\n'.format(date))
                    f.write('This is an automatic reminder that there is a group\
                    meeting on {date} where:\n    Presenter: {presenter}\n    \
                    Title: {title}\n    Chair: {chair}\n'.\
                            format(date=presentation['date'],
                                   presenter=presentation['presenter'],
                                   chair=presentation['chair'],
                                   title=title))
                    if presentation['title'] == '':
                        f.write('When you can, could the presenter send David')
                        if presentation['title'] == '':
                            f.write(' and Pawel the title of the presentation and')
                        f.write(' a copy of the presentation?\n')
                    f.write('\nThanks,\nDavid\n')

    def store_people(self):
        """ Backs up the presenters

        """
        import pickle
        for person in self._presenters:
            name = person.name
            filename = '_'.join(name.lower().split())+'.p'
            pickle.dump(person,open('./backup/'+filename,'w'))

