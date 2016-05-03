# -*- coding: utf-8 -*-


with open('middle_final.csv', 'r') as middle_file, open('wandoujia_final.csv', 'w') as wandoujia_file:
    for line in middle_file:
        new_line = ''
        try:
            elements = line.split(',')
            if elements[0] == 'submit':
                sms_type = 'submit'
                phone_number = elements[1]
                time = elements[3]
                content = elements[4].rstrip()
                new_line = 'sms,{},,\t{},,{},39,{}'.format(
                    sms_type, phone_number, time, content)
            else:
                sms_type = 'deliver'
                phone_number = elements[1]
                time = elements[3]
                content = elements[4].rstrip()
                new_line = 'sms,{},\t{},,,{},39,{}'.format(
                    sms_type, phone_number, time, content)
        except Exception as e:
            print(e)

        wandoujia_file.write(new_line + '\n')
