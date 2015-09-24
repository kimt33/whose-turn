from group_meeting import *
from datetime import date
import pickle

groupmeetings = pickle.load(open('group_meeting.p','r'))
groupmeetings.remove_chair(date(2015,5,27))
for person in ['Kasia Boguslawski', 'Pawel Tecmer', 'Farnaz Heidar Zadeh', 'Cristina Gonzalez', 'Chunying Rong', 'Stijn Fias', 'Corinne Duperrouzel', 'Paul Johnson', 'Diego Berrocal']:
    groupmeetings.find_person(person)._is_away = True
groupmeetings.add_future_random_one(datetime.date(2015,5,27), date_type='chair')
groupmeetings.add_title(date(2015,5,6), 'Cholesky Decomposition and Density Fitting in HORTON')
groupmeetings.add_title(date(2015,5,13), 'Developing Density Functional Reactivity Theory with Information Theory')
groupmeetings.add_title(date(2015,5,20), 'Something Something Geminals')
groupmeetings.add_title(date(2015,5,27), 'Comparisons and Models')
groupmeetings.update_future()
groupmeetings.print_nice()
groupmeetings.compose_emails()
pickle.dump(groupmeetings, open('group_meeting.p','w'))
groupmeetings.store_people()
