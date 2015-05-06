from group_meeting import *
import pickle

groupmeetings = pickle.load(open('group_meeting.p','r'))
groupmeetings.add_title(datetime.date(2015,4,29), 'Beating a Horse to Death: Quasiatomic Orbitals')
groupmeetings.update_future()
groupmeetings.find_person('Paul Johnson')
groupmeetings.add_future_one(datetime.date(2015,5,20),'Paul Johnson')
groupmeetings.find_person('Chun Ying')._name = 'Chunying Rong'
past = groupmeetings._past_presentations
for date in past:
    if past[date]['presenter'] == 'Chun Ying':
        past[date]['presenter'] = 'Chunying Rong'
    if past[date]['chair'] == 'Chun Ying':
        past[date]['chair'] = 'Chunying Rong'
future = groupmeetings._future_presentations
for date in future:
    if future[date]['presenter'] == 'Chun Ying':
        future[date]['presenter'] = 'Chunying Rong'
    if future[date]['chair'] == 'Chun Ying':
        future[date]['chair'] = 'Chunying Rong'
groupmeetings.find_person('Yi Lin')._name = 'Yilin Zhao'
past = groupmeetings._past_presentations
for date in past:
    if past[date]['presenter'] == 'Yi Lin':
        past[date]['presenter'] = 'Yilin Zhao'
    if past[date]['chair'] == 'Yi Lin':
        past[date]['chair'] = 'Yilin Zhao'
future = groupmeetings._future_presentations
for date in future:
    if future[date]['presenter'] == 'Yi Lin':
        future[date]['presenter'] = 'Yilin Zhao'
    if future[date]['chair'] == 'Yi Lin':
        future[date]['chair'] = 'Yilin Zhao'
groupmeetings.print_nice()
groupmeetings.compose_emails()
pickle.dump(groupmeetings, open('group_meeting.p','w'))
groupmeetings.store_people()
