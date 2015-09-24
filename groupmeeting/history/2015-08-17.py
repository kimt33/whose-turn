from group_meeting import *
from datetime import date
import pickle

groupmeetings = pickle.load(open('group_meeting.p','r'))
groupmeetings.update_future()
thisweek = date(2015,8,19)
for person in groupmeetings._presenters:
    print person.__dict__.keys()
groupmeetings.print_nice()
#groupmeetings.compose_emails()
