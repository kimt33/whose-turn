import datetime

class Presentation(object):
    def __init__(self, date, presenter=None, chair=None, title=''):
        """ Creates a presentation

        Parameters
        ----------
        date : datetime.date
            Date of the presentation
        presenter : {None, Person}
            Person presenting the presentation
        chair : {None, Person}
            Person chairing the presentation
        title : {'', str}
            Title of the presentation

        Raises
        ------
        AssertionError
            If date is not a datetime.date instance

        """
        assert isinstance(date, datetime.date)
        self._date = date
        self._presenter = presenter
        self._chair = chair
        self._title = title

    def __str__(self):
        return '{date:<12}{presenter:<20} {chair:<20} {title}'.format(date=str(self.date),
                                                                      presenter=self.presenter,
                                                                      chair=self.chair,
                                                                      title=self.title)

    def __eq__(self, other):
        """ Checks if both presentations have the same attribute values

        Parameters
        ----------
        other : Presentation

        Returns
        -------
        equal_or_no : {True, False}

        Raises
        ------
        AssertionError
            If other is not a Presentation instance
        """
        assert isinstance(other, Presentation), 'Cannot compare Presentation\
        instance with something that is not a Presentation instance'
        for attribute, value in self.__dict__.items():
            if value != getattr(other, attribute):
                return False
        else:
            return True

    def __ne__(self, other):
        """ Checks if the presentations have the different attribute values

        Parameters
        ----------
        other : Presentation

        Returns
        -------
        notequal_or_no : {True, False}

        Raises
        ------
        AssertionError
            If other is not a Presentation instance
        """
        assert isinstance(other, Presentation), 'Cannot compare Presentation\
        instance with something that is not a Presentation instance'
        for attribute, value in self.__dict__.items():
            if value != getattr(other, attribute):
                return True
        else:
            return False

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, newdate):
        if newdate < datetime.date.today():
            self._presenter.remove_date_presented(self.date)
            self._presenter.add_date_presented(newdate)
            self._chair.remove_date_chaired(self.date)
            self._chair.add_date_chaired(newdate)
        else:
            self._presenter.remove_date_to_present(self.date)
            self._presenter.add_date_to_present(newdate)
            self._chair.remove_date_to_chair(self.date)
            self._chair.add_date_to_chair(newdate)
        self._date = newdate

    @property
    def presenter(self):
        if self._presenter is None:
            return 'N/A'
        else:
            return self._presenter.name

    @presenter.setter
    def presenter(self, newperson):
        if self.date < datetime.date.today():
            if self._presenter is not None:
                self._presenter.remove_date_presented(self.date)
            newperson.add_date_presented(self.date)
        else:
            if self._presenter is not None:
                self._presenter.remove_date_to_present(self.date)
            newperson.add_date_to_present(self.date)
        self._presenter = newperson

    @property
    def chair(self):
        if self._chair is None:
            return 'N/A'
        else:
            return self._chair.name

    @chair.setter
    def chair(self, newperson):
        if self.date < datetime.date.today():
            if self._chair is not None:
                self._chair.remove_date_chaired(self.date)
            newperson.add_date_chaired(self.date)
        else:
            if self._chair is not None:
                self._chair.remove_date_to_chair(self.date)
            newperson.add_date_to_chair(self.date)
        self._chair = newperson

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

class PresentationStorage(object):
    """ Stores and manages a list of presentations


    """
    def __init__(self, list_presentations):
        """ Stores the list of presentations

        Parameters
        ----------
        list_presentations : list of Presentation instances
        """
        self._presentations = list(list_presentations)

    def __contains__(self, other):
        """ Checks if presentation is in storage by comparing attributes

        Parameters
        ----------
        other : Presentation

        Returns
        -------
        yes_or_no : {True, False}

        Raises
        ------
        AssertionError
            If other is not a Presentation instance

        """
        assert isinstance(other, Presentation), 'Given object is not a\
        Presentation instance'
        for presentation in self.presentations:
            if presentation == other:
                return True
        else:
            return False

    @property
    def presentations(self):
        """ Copies of the stored presentations

        """
        return self._presentations[:]

    def ordered_date(self, reverse=False):
        """ Returns presentations ordered by date

        Parameters
        ----------
        reverse : {False, True}
            Orders from earliest to latest

        Returns
        -------
        sorted_presentations : list of Presentation
        """
        return sorted(self.presentations, key=lambda x: x.date)

    def find_presentations(self, date=None, presenter=None, chair=None, title='',
                           presentation=None):
        """ Finds the presentations that matches the given parameters

        Parameters
        ----------
        date : {None, datetime.date}
            Date of the desired presentation
        presenter : {None, Person}
            Presenter of the desired presentation
        chair : {None, Person}
            Chair of the desired presentation
        title : {'', str}
            Title of the desired presentation
        presentation : {None, Presentation}
            Presentation from which the above parameters are extracted

        Returns
        -------
        found_presentations : list of Presentation instances

        Raise
        -----
        AssertionError
            If both presentation and any of the other parameters (date, presenter
            chair, title) are given
            The parameters (date, presenter, chair, title) and presentation must
            be mutually exclusive
        """
        found_presentations = []
        parameters = {}
        if date is not None:
            parameters['date'] = date
        if presenter is not None:
            parameters['presenter'] = presenter
        if chair is not None:
            parameters['chair'] = chair
        if title != '':
            parameters['title'] = title
        if presentation is not None:
            assert len(parameters)==0, 'Both the parameters (date, presenter,\
            chair, title) and the presentation are given'
            date = presentation._date
            presenter = presentation._presenter
            chair = presentation._chair
            title = presentation._title
            return self.find_presentations(date=date,
                                           presenter=presenter,
                                           chair=chair,
                                           title=title)
        for presentation in self._presentations:
            # These are not copies. They are the real deal
            for parameter, value in parameters.items():
                if (getattr(presentation, parameter) != value or
                    value != getattr(presentation, parameter)):
                    break
            else:
                found_presentations.append(presentation)
        return found_presentations

    def add_presentation(self, presentation):
        """ Stores a presentation

        Parameters
        ----------
        presentation : Presentation

        Raises
        ------
        AssertionError
           If presentation does not have a date 
        """
        # if presentation already exists
        assert hasattr(presentation, 'date'), 'Given presentation does not have\
        a date'
        if len(self.find_presentations(presentation=presentation)) == 0:
            self._presentations.append(presentation)
        else:
            print('Given presentation or a similar presentation is already\
            present in the storage')

    def remove_presentation(self, presentation):
        """ Removes a presentation from storage

        Parameters
        ----------
        presentation : Presentation

        """
        assert hasattr(presentation, 'date'), 'Given presentation does not have\
        a date'
        # need to find exact object (same memory) that is the same as the presentation
        similar_presentations = self.find_presentations(presentation=presentation)
        same_presentations = [i for i in similar_presentations if i == presentation]
        for i in same_presentations:
            self._presentations.remove(i)

