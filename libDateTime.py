"""
    libDateTime.py
"""
from datetime import datetime
import os, sys
#----------------------------------------------------------------

#----------------------------------------------------------------
class DateTimeUtility:

    @staticmethod
    def getDateString(now:datetime, separeter:str=None):
        #print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 例: 2025-06-17 15:30:45
        if separeter is None:
            separeter = '/'
        return now.strftime("%Y"+ separeter +"%m"+ separeter +"%d")
    
    @staticmethod
    def getTimeString(now:datetime, separeter:str=None):
        #print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 例: 2025-06-17 15:30:45
        if separeter is None:
            separeter = ':'
        return now.strftime("%H"+ separeter +"%M"+ separeter +"%S")
        
    
    @staticmethod
    def getNowDateTimeString():
        #例: [2025/06/17 15:30:45]
        now = datetime.now()
        s0 = DateTimeUtility.getDateString(now)
        s1 = DateTimeUtility.getTimeString(now)
        return "["+ s0 +" "+ s1 +"]"

    @staticmethod
    def getNowTimeString():
        #例: [15:30:45]
        now = datetime.now()
        s1 = DateTimeUtility.getTimeString(now)
        return "["+ s1 +"]"

    @staticmethod
    def getNowDateString():
        #例: [2025/06/17]
        now = datetime.now()
        s0 = DateTimeUtility.getDateString(now)
        return "["+ s0 +"]"
   

#================================================================
# End of file.
#================================================================
