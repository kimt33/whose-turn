from group_meeting import *
from datetime import date, timedelta
import pickle
from person import Person

groupmeetings = pickle.load(open('group_meeting.p','r'))
groupmeetings.update_future()
for person in groupmeetings._presenters:
    person._dates_away = []
groupmeetings.find_person('Paul Ayers').add_date_away( (date(2015,9,10), date(2015,9,20)) )
groupmeetings.find_person('Farnaz Heidar Zadeh').add_date_away( (date(2015,8,29),) )
groupmeetings.find_person('Kasia Boguslawski').add_date_away( (date(2015,8,1),) )
groupmeetings.find_person('Pawel Tecmer').add_date_away( (date(2015,9,1),) )
groupmeetings.find_person('Chunying Rong').add_date_away( (date(2015,9,28),) )
groupmeetings.find_person('Ramon Miranda').add_date_away( (date(2015,6,15),) )
groupmeetings.find_person('Stijn Fias').add_date_away( (date(2015,5,4),) )
groupmeetings.find_person('Sung Hong').add_date_away( (date(2015,9,1),) )
groupmeetings.find_person('Corinne Duperrouzel').add_date_away( (date(2015,9,1),) )
groupmeetings.find_person('Paul Johnson').add_date_away( (date(2015,1,7),) )
groupmeetings.find_person('Diego Berrocal').add_date_away( (date(2015,4,19),) )
groupmeetings.add_past_presentation(date(2015,9,9), 'Paul Ayers', title='Outline of the Projects in Ayers Group')
groupmeetings.add_past_presentation(date(2015,8,26), 'Corinne Duperrouzel')
groupmeetings.add_past_presentation(date(2015,8,27), 'Nicole Dumont')
groupmeetings.add_person(Person('Kumru Dikmenli', 'masters'))
groupmeetings.add_person(Person('Michael Richer', 'masters'))
groupmeetings.add_person(Person('Caitlin Lanssens', 'visiting'))
groupmeetings.add_future_one(date(2015,9,16), name_presenter='Cristina Gonzalez')
groupmeetings.add_future_random_one(date(2015,9,16), date_type='chair')
groupmeetings.add_future_one(date(2015,9,23), name_presenter='Ahmed Kamel')
groupmeetings.add_future_random_one(date(2015,9,23), date_type='chair')
groupmeetings.add_future_random(2, date(2015,9,30))
groupmeetings.print_nice()
groupmeetings.store_people()
pickle.dump(groupmeetings, open('group_meeting.p','w'))
groupmeetings.compose_emails()
