# -*- coding: utf-8 -*-

# 2013. 7.15  8:12 -> 2013.07.15 08:12
def convert_time(old_time):
    tmp = old_time.replace(' ', '0')
    return tmp[0:10] + ' ' + tmp[11:16] + ':00'

with open('20130714-20150425(Wandoujia).csv', 'r') as wandoujia_file, open('middle_format_wandoujia.csv', 'w') as mid_file:
    for line in wandoujia_file:
        new_line = ''
        try:
            elements = line.split(',')
            if elements[1] == 'submit':
                # sms,submit,[发送者],\t[电话号码],,2013. 7.15  8:12,9,[短信内容]\r\n
                sms_type = 'submit'
                phone_number = elements[3].lstrip()
                time = convert_time(elements[5])
                content = elements[7].rstrip()
                new_line = '{},{},{},{}'.format(
                    phone_number, time, content, sms_type)
            else:
                # sms,deliver,\t[电话号码],[发送者],,2013. 7.15  9:32,9,[短信内容]\r\n
                sms_type = 'deliver'
                phone_number = elements[2].lstrip()
                time = convert_time(elements[5])
                content = elements[7].rstrip()
                new_line = '{},{},{},{}'.format(
                    phone_number, time, content, sms_type)
        except Exception as e:
            print(e)

        mid_file.write(new_line + '\n')
