from group_meeting import *
from datetime import date
import pickle

groupmeetings = pickle.load(open('group_meeting.p','r'))
for person in groupmeetings._presenters:
    person._dates_away = []
    del person._is_away
for person in ['Kasia Boguslawski', 'Pawel Tecmer', 'Cristina Gonzalez', 'Chunying Rong', 'Stijn Fias', 'Corinne Duperrouzel', 'Paul Johnson', 'Diego Berrocal']:
    groupmeetings.find_person(person)._dates_away.append([date.today()])
for person in ['Farnaz Heidar Zadeh', 'Matt Chan', 'David Kim', 'Derrick Yang', 'Yilin Zhao', 'Marco Franco',]:
    groupmeetings.find_person(person)._dates_away.append([date(2015,6,4)])
groupmeetings.find_person('Paul Ayers')._dates_away.append([date(2015,05,29)])
groupmeetings.print_nice()
groupmeetings.store_people()
