#!/usr/bin/python

import re,sys,os

try: 
    for root, dirs, files in os.walk("./"):
         for name in files:
             try:
                 tagnumber = name.split('-')[6] 
                 tagnumber = (int(tagnumber))
                 newname='{:03d}-{:s}'.format(tagnumber,name)
                 print newname
                 os.rename(name, newname)
             except:
                 print ("Not renaming %s" % name)
except:

    print ("Something went wrong")
