import pickle
from group_meeting import GroupMeetings
from datetime import date

groupmeetings = pickle.load(open('group_meeting.p','r'))
groupmeetings.update_future()
groupmeetings.add_past_presentation(date(2015,8,25), 'Corinne Duperrouzel', title='Multi-Reference Nature of Plutonium Oxides')
groupmeetings.add_past_presentation(date(2015,8,26), 'Sung Hong', title="Troubleshooting SCF and Geometry convergence in supramolecular uranyl and neptunyl systems")
groupmeetings.add_past_presentation(date(2015,8,27), 'Jonathan La', title='Procrustes Analysis')
groupmeetings.add_past_presentation(date(2015,8,28), 'Ali', title='Fitting Project')
groupmeetings.add_past_presentation(date(2015,8,20), 'James Anderson', title='Relativistic Quantum Theory of Atoms in Molecules')
groupmeetings.add_title(date(2015,9,16), 'Energy extrapolation: finding a systematic way to correct model energies')

groupmeetings.remove_future(date(2015,9,23))
groupmeetings.remove_future(date(2015,9,30))
groupmeetings.remove_future(date(2015,10,7))
groupmeetings.remove_future(date(2015,10,14))
groupmeetings.find_person('Paul Ayers').add_date_away( (date(2015,9,23), date(2015,10,5)) )

groupmeetings.add_future_one(date(2015,9,22), name_presenter='Ahmed Kamel', name_chair='Michael Richer')
groupmeetings.add_future_one(date(2015,9,29), name_presenter='Kumru Dikmenli')
groupmeetings.add_future_random_one(date(2015,9,29), date_type='chair')
groupmeetings.add_future_one(date(2015,10,6), name_presenter='Anand Patel')
groupmeetings.add_future_random_one(date(2015,10,6), date_type='chair')
groupmeetings.add_future_random(2, date(2015,10,13))
groupmeetings.print_nice()
groupmeetings.store_people()
groupmeetings.compose_emails()
groupmeetings.store_people()
pickle.dump(groupmeetings, open('group_meeting.p','w'))
