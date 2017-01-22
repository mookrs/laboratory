# -*- coding: utf-8 -*-

import _winreg as winreg

hkcr = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, '')

for i in range(999999):
    try:
        key = winreg.EnumKey(hkcr, i)
        if '\0' in key:
            print "Found null character in key: HKEY_CLASSES_ROOT/%s" % str(key).replace('\0', '*')
    except WindowsError:
        print "Finished!"
        break
