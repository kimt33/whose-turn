from group_meeting import *
import pickle

groupmeetings = pickle.load(open('2015-04-16.p','r'))
diego = Person('Diego Berrocal', 'undergrad', [datetime.date(2015,4,1)], isaway=True)
groupmeetings.add_person(diego)
groupmeetings.add_title(datetime.date(2015,4,1), 'Python workshop')
for presenter in groupmeetings._presenters:
    presenter._dateschair = []
    presenter._futurechair = []
groupmeetings.add_chair(datetime.date(2015,2,4), 'Cristina Gonzalez')
groupmeetings.add_chair(datetime.date(2015,2,11), 'Diego Berrocal')
groupmeetings.add_chair(datetime.date(2015,2,18), 'Chun Ying')
groupmeetings.add_chair(datetime.date(2015,2,25), 'Yi Lin')
groupmeetings.add_chair(datetime.date(2015,3,4), 'Marco Franco')
groupmeetings.add_chair(datetime.date(2015,3,11), 'Kasia Boguslawski')
groupmeetings.add_chair(datetime.date(2015,4,1), 'Cristina Gonzalez')
groupmeetings.add_chair(datetime.date(2015,4,8), 'David Kim')
groupmeetings.add_chair(datetime.date(2015,4,15), 'Ramon Miranda')
groupmeetings.add_chair(datetime.date(2015,4,22), 'Derrick Yang')
groupmeetings.add_chair(datetime.date(2015,4,29), 'Matt Chan')
groupmeetings.add_chair(datetime.date(2015,5,6), 'Farnaz Heidar Zadeh')
groupmeetings.add_chair(datetime.date(2015,5,13), 'Pawel Tecmer')
groupmeetings.add_chair(datetime.date(2015,5,20), 'Sung Hong')
groupmeetings.add_chair(datetime.date(2015,5,27), 'Chun Ying')

groupmeetings.print_nice(flag='both')
groupmeetings.print_nice(flag='future')
pickle.dump(groupmeetings, open('2015-04-21.p','w'))
