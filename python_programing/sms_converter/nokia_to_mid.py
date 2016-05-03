# -*- coding: utf-8 -*-


with open('20121003-20130714-20140228(Nokia).csv', 'r') as nokia_file, open('middle_format_nokia.csv', 'w') as mid_file:
    for line in nokia_file:
        new_line = ''
        try:
            # sms,submit,[电话号码],2014-02-28 11:46:30,[发送者],[短信内容]\r\n
            elements = line.split(',')
            sms_type = elements[1]
            phone_number = elements[2]
            # 2012-10-07 13:41:38 -> 2012.10.07 13:41:38
            time = elements[3].replace('-', '.')
            content = elements[5].rstrip()
            new_line = '{},{},{},{}'.format(
                phone_number, time, content, sms_type)
        except Exception as e:
            print(e)

        mid_file.write(new_line + '\n')
