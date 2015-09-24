from group_meeting import GroupMeetings
from person import Person
import pickle
import os
from datetime import date

file_names = list(os.listdir('./people'))
file_names = ['./people/'+i for i in file_names]
people = []
for name in file_names:
    f=open(name,'r')
    people.append(pickle.load(f))
x= [person.name for person in people]
gm = GroupMeetings(people)
gm.add_title('Chemical reactivity at finite temperature', date=date(2015,2,4))
gm.add_title('Linear reasponse function and its applications in chemistry and physics', date=date(2015,2,11))
gm.add_title('Fractional particle number and chemical reactivity', date=date(2015,2,18))
gm.add_title('Not so short introduction to geminals', date=date(2015,2,25))
gm.add_title('Dissecting bond formation of Palladium-ethene complexes', date=date(2015,3,4))
gm.add_title('Elucidating cation-cation interaction between uranyl cations', date=date(2015,3,11))
gm.add_title('Python workshop', date=date(2015,4,1))
gm.add_title('Electronic spectra of ThO and ThS', date=date(2015,4,8))
gm.add_title('Flat plane condition and spin reactivity indicator for atoms and ions', date=date(2015,4,15))
gm.add_title('Orbital Entanglement in Quantum Chemistry', date=date(2015,4,22))
gm.add_title('Beating a Horse to Death: Quasiatomic Orbitals', date=date(2015,4,29))
gm.add_title('Cholesky Decomposition and Density Fitting in HORTON', date=date(2015,5,6))
gm.add_title('Developing Density Functional Reactivity Theory with Information Theory', date=date(2015,5,13))
gm.remove_presentation(date=date(2015,5,20), presenter='Farnaz Heidar Zadeh')
gm.add_title('Something Something Geminals', date=date(2015,5,20))
gm.add_title('Comparisons and Models', date=date(2015,5,27))

james = Person('James Anderson', 'visiting', dates_presented=[date(2015,8,20)])
gm.add_person(james)
gm.add_title('Relativistic Quantum Theory of Atoms in Molecules', date=date(2015,8,20))
gm.add_chair('Paul Ayers', date=date(2015,8,20))

gm.remove_presentation(date=date(2015,8,25), presenter='Corinne Duperrouzel')
gm.add_title('Multi-Reference Nature of Plutonium Oxides', date=date(2015,8,26), presenter='Corinne Duperrouzel')
gm.add_title('Troubleshooting SCF and Geometry convergence in supramolecular uranyl and neptunyl systems', date=date(2015,8,26), presenter='Sung Hong')
jonathan = Person('Jonathan Snow', 'undergrad', dates_presented=[date(2015,8,26)])
gm.add_person(jonathan)
gm.add_title('Procrustes Analysis', date=date(2015,8,26), presenter='Jonathan Snow')
ali = Person('Ali Snow', 'undergrad', dates_presented=[date(2015,8,26)])
gm.add_person(ali)
gm.add_title('The Fitting Project', date=date(2015,8,26), presenter='Ali Snow')
gm.remove_presentation(date=date(2015,8,27), presenter='Nicole Dumont')
gm.add_title('Multi-Reference Nature of Plutonium Oxide', date=date(2015,8,28))
gm.add_title('Outline of the Projects in Ayers Group', date=date(2015,9,9))
gm.remove_presentation(date=date(2015,9,16), chair='David Kim')
gm.add_title('Energy extrapolation: finding a systematic way to correct model energies', date=date(2015,9,16))
gm.add_title('Polarizability Fitting and Calculation', date=date(2015,9,22))
gm.add_future_one(date=date(2015,10,6), presenter='Nicole Dumont')
gm.replace_date(date(2015,10,13), from_date=date(2015,9,29), presenter='Kumru Dikmenli')
gm.remove_presentation(date=date(2015,10,13), presenter='Marco Franco')
gm.update_future()
gm.find_person('Paul Ayers').add_date_away((date(2015,9,23),date(2015,10,7)))
gm.add_future_random_one(date(2015,9,29))
gm.add_future_random(16, date(2015,10,20))
gm.print_nice()

