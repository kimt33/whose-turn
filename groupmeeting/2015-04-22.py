from group_meeting import *
import pickle

groupmeetings = pickle.load(open('2015-04-21.p','r'))
groupmeetings.find_person('Paul Ayers').add_email('theoretical.chemistry@gmail.com')
groupmeetings.find_person('Kasia Boguslawski').add_email('katharina.boguslawski@gmail.com')
groupmeetings.find_person('Pawel Tecmer').add_email('ptecmer@gmail.com')
groupmeetings.find_person('Ahmed Kamel').add_email('theoahmedkamel@gmail.com')
groupmeetings.find_person('Farnaz Heidar Zadeh').add_email('farnazhz@gmail.com')
groupmeetings.find_person('Matt Chan').add_email('talcite@gmail.com')
groupmeetings.find_person('Cristina Gonzalez').add_email('crisbeth46@gmail.com')
groupmeetings.find_person('David Kim').add_email('david.kim.91@gmail.com')
groupmeetings.find_person('Derrick Yang').add_email('yxt1991@gmail.com')
groupmeetings.find_person('Yi Lin').add_email('zhao229@mcmaster.ca')
groupmeetings.find_person('Marco Franco').add_email('qimfranco@gmail.com')
groupmeetings.find_person('Chun Ying').add_email('chunyingrong@gmail.com')
groupmeetings.find_person('Ramon Miranda').add_email('ramirandaq@gmail.com')
groupmeetings.find_person('Stijn Fias').add_email('stijn.fias@gmail.com')
groupmeetings.find_person('Sung Hong').add_email('hongsw2@gmail.com')
groupmeetings.find_person('Corinne Duperrouzel').add_email('duperrc@mcmaster.ca')
groupmeetings.find_person('Anand Patel').add_email('anandpatel98@gmail.com')
groupmeetings.find_person('Nicole Dumont').add_email('dumontns@mcmaster.ca')
groupmeetings.find_person('Paul Johnson').add_email('bigpauljohnson@gmail.com')
groupmeetings.find_person('Diego Berrocal').add_email('cestdiego@gmail.com')

pickle.dump(groupmeetings, open('2015-04-22.p','w'))
