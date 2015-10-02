from datetime import datetime

def str_to_date(date_str):
    return datetime.strptime(date_str, '%Y%m%d')

dt = str_to_date('20150803')
dt2 = str_to_date('20150729')
if (dt - dt2).days > 5.0:
    print 'yes'