from group_meeting import *
import pickle

groupmeetings = pickle.load(open('2015-04-22.p','r'))
groupmeetings.add_chair(datetime.date(2015,4,22), 'Yi Lin')
groupmeetings.add_title(datetime.date(2015,4,22), 'Orbital Entanglement in Quantum Chemistry')
groupmeetings.update_future()
groupmeetings.add_title(datetime.date(2015,4,29), 'Breadth over Depth: Quasiatomic orbital transformation, VB, and maybe AIM')
groupmeetings.print_nice()
groupmeetings.compose_emails()
pickle.dump(groupmeetings, open('2015-04-28.p','w'))
