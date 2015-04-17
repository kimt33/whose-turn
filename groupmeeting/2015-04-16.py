from group_meeting import *
import pickle

marco = Person('Marco Franco', 'postdoc', [datetime.date(2015,2,4)])
stijn = Person('Stijn Fias', 'postdoc', [datetime.date(2015,2,11)], isaway=True)
ramon = Person('Ramon Miranda', 'phd', [datetime.date(2015,2,18)])
kasia = Person('Kasia Boguslawski', 'postdoc', [datetime.date(2015,2,25)])
yilin = Person('Yi Lin', 'masters', [datetime.date(2015,3,4)])
sung = Person('Sung Hong', 'undergrad', [datetime.date(2015,3,11)])
diego = Person('Diego Berrocal', 'undergrad', [datetime.date(2015,4,1)], isaway=True)
cris = Person('Cristina Gonzalez', 'phd', [datetime.date(2015,4,8)], isaway=True)
derrick = Person('Derrick Yang', 'masters', [datetime.date(2015,4,15)])
pawel = Person('Pawel Tecmer', 'postdoc', [])
paul = Person('Paul Ayers', 'professor', [], isaway=True)
farnaz = Person('Farnaz Heidar Zadeh', 'phd', [])
matt = Person('Matt Chan', 'phd', [])
david = Person('David Kim', 'masters', [])
chunying = Person('Chun Ying', 'phd', [])
ahmed = Person('Ahmed Kamel', 'phd', [])
corinne = Person('Corinne Duperrouzel', 'undergrad', [], isaway=True)
anand = Person('Anand Patel', 'undergrad', [], isaway=True)
nicole = Person('Nicole Dumont', 'undergrad', [], isaway=True)
pj = Person('Paul Johnson', 'postdoc', [], isaway=True)
people = [paul, kasia, pawel, ahmed, farnaz, matt, cris, david, derrick, yilin, marco, chunying, ramon, stijn, sung, corinne, anand, nicole, pj]
groupmeetings = GroupMeetings(people)
groupmeetings.add_title(datetime.date(2015,2,4), 'Chemical reactivity at finite temperatures')
groupmeetings.add_title(datetime.date(2015,2,11), 'Linear reasponse function and its applications in chemistry and physics')
groupmeetings.add_title(datetime.date(2015,2,18), 'Fractional particle number and chemical reactivity')
groupmeetings.add_title(datetime.date(2015,2,25), 'Not so short introduction to geminals')
groupmeetings.add_title(datetime.date(2015,3,4), 'Dissecting bond formation of Palladium-ethene complexes')
groupmeetings.add_title(datetime.date(2015,3,11), 'Elucidating cation-cation interaction between uranyl cations')
groupmeetings.add_title(datetime.date(2015,4,1), 'Python workshop')
groupmeetings.add_title(datetime.date(2015,4,8), 'Electronic spectra of ThO and ThS')
groupmeetings.add_title(datetime.date(2015,4,15), 'Flat plane condition and spin reactivity indicator for atoms and ions')
groupmeetings.set_future_one(datetime.date(2015,4,22), pawel)
groupmeetings.set_future_one(datetime.date(2015,4,29), david)
groupmeetings.set_future_one(datetime.date(2015,5,6), matt)
groupmeetings.set_future_one(datetime.date(2015,5,13), chunying)
groupmeetings.set_future_one(datetime.date(2015,5,20), farnaz)
groupmeetings.set_future_one(datetime.date(2015,5,27), ramon)
groupmeetings.update_future()
for i in groupmeetings.past_presentations:
    print i
for i in groupmeetings.future_presentations:
    print i
pickle.dump(groupmeetings, open('2015-04-16.p','w'))

