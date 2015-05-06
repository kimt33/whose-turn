import person
import datetime

#check person
john = person.Person('john','masters',[datetime.date(2000,1,1)])
assert john._name == 'john' and john.name == 'john' and john == 'john'
john.add_date_presented(datetime.date(2000,1,2))
assert len(john.dates_presented)==2
john.remove_date_presented(datetime.date(2000,1,1))
assert len(john.dates_presented)==1
john.add_date_to_present(datetime.date(2000,1,3))
john.add_date_to_present(datetime.date(2000,1,4))
assert len(john.dates_to_present)==2
john.remove_date_to_present(datetime.date(2000,1,3))
assert len(john.dates_to_present)==1
john.update_date_to_present_to_presented(datetime.date(2000,1,4))
assert len(john.dates_to_present)==0
assert len(john.dates_presented)==2

john.add_date_chaired(datetime.date(2000,1,2))
assert len(john.dates_chaired)==1
john.remove_date_chaired(datetime.date(2000,1,2))
assert len(john.dates_chaired)==0
john.add_date_to_chair(datetime.date(2000,1,3))
john.add_date_to_chair(datetime.date(2000,1,4))
assert len(john.dates_to_chair)==2
john.remove_date_to_chair(datetime.date(2000,1,3))
assert len(john.dates_to_chair)==1
john.update_date_to_chair_to_chaired(datetime.date(2000,1,4))
assert len(john.dates_to_chair)==0
assert len(john.dates_chaired)==1

john.add_email('dsfsdf')
assert john.email=='dsfsdf'

import group_meeting
john.add_date_to_chair(datetime.date(2000,1,5))
john.add_date_to_present(datetime.date(2000,1,6))
group=group_meeting.GroupMeetings([john])
assert group.presenters==['john']
assert len(group.past_presentations)==2
assert len(group.future_presentations)==2
assert group.find_person('john')==john
mary = person.Person('mary','phd')
mary.add_date_presented(datetime.date(2000,1,7))
mary.add_date_to_chair(datetime.date(2000,1,8))
mary.add_date_chaired(datetime.date(2000,1,2))
group.add_person(mary)
group.add_future_random_one(datetime.date(2010,1,1))
group.add_future_one(datetime.date(2022,2,3),'john')
group.update_future()
group.print_nice()
