# -*- coding: utf-8 -*-


with open('20130616(Labi).csv', 'r') as labi_file, open('middle_format_labi.csv', 'w') as mid_file:
    for line in labi_file:
        new_line = ''
        try:
            elements = line.split(',')
            if elements[1] == 'submit':
                # sms,submit,,\t[电话号码],,2012.10.07 13:44:57,[短信内容]\r\n
                sms_type = 'submit'
                phone_number = elements[3].lstrip()
                time = elements[5]
                content = elements[6].rstrip()
                new_line = '{},{},{},{}'.format(
                    phone_number, time, content, sms_type)
            else:
                sms_type = 'deliver'
                phone_number = elements[2].lstrip()
                if not elements[3]:
                    # sms,deliver,\t[电话号码],,,2012.10.07 13:41:38,[短信内容]\r\n
                    time = elements[5]
                    content = elements[6].rstrip()
                else:
                    # sms,deliver,\t[电话号码],[发送者],2012.10.07 13:41:38,[短信内容]\r\n
                    time = elements[4]
                    content = elements[5].rstrip()
                new_line = '{},{},{},{}'.format(
                    phone_number, time, content, sms_type)
        except Exception as e:
            print(e)

        mid_file.write(new_line + '\n')
