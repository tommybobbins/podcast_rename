#!/usr/bin/python

import re,sys,os

try: 
    for root, dirs, files in os.walk("./"):
         for name in files:
             try:
                 tagnumber = name.split('-')[6] 
                 stuff_to_end = name.split('-')[6:] 
                 concat_stuff_to_end = ''.join(stuff_to_end) + ','
                 guest = concat_stuff_to_end.split('.')[0] 
                 newname='{:s}-{:s}'.format(guest,name)
                 print newname
                 os.rename(name, newname)
             except:
                 print ("Not renaming %s" % name)
except:

    print ("Something went wrong")
