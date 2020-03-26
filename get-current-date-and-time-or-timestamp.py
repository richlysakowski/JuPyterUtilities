# Python : How to get Current date and time or timestamp ?
# https://thispointer.com/python-how-to-get-current-date-and-time-or-timestamp/

import time
 
from datetime import datetime
 
def main():
 
    print('*** Get Current date & timestamp using datetime.now() ***')
 
    # Returns a datetime object containing the local date and time
    dateTimeObj = datetime.now()
 
    # Access the member variables of datetime object to print date & time information
    print(dateTimeObj.year, '/', dateTimeObj.month, '/', dateTimeObj.day)
    print(dateTimeObj.hour, ':', dateTimeObj.minute, ':', dateTimeObj.second, '.', dateTimeObj.microsecond)
 
    print(dateTimeObj)
 
    # Converting datetime object to string
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    print('Current Timestamp : ', timestampStr)
 
    timestampStr = dateTimeObj.strftime("%H:%M:%S.%f - %b %d %Y ")
    print('Current Timestamp : ', timestampStr)
 
    print('*** Fetch the date only from datetime object ***')
 
    # get the date object from datetime object
    dateObj = dateTimeObj.date()
 
    # Print the date object
    print(dateObj)
 
    # Access the member variables of date object to print
    print(dateObj.year, '/', dateObj.month, '/', dateObj.day)
 
    # Converting date object to string
    dateStr = dateObj.strftime("%b %d %Y ")
    print(dateStr)
 
    print('*** Fetch the time only from datetime object ***')
 
    # get the time object from datetime object
    timeObj = dateTimeObj.time()
    # Access the member variables of time object to print time information
    print(timeObj.hour, ':', timeObj.minute, ':', timeObj.second, '.', timeObj.microsecond)
 
    # It contains the time part of the current timestamp, we can access it's member variables to get the fields or we can directly print the object too
    print(timeObj)
 
 
    # Converting date object to string
    timeStr = timeObj.strftime("%H:%M:%S.%f")
    print(timeStr)
 
    print('*** Get Current Timestamp using time.time() ***')
 
    # Get the seconds since epoch
    secondsSinceEpoch = time.time()
 
    print('Seconds since epoch : ', secondsSinceEpoch)
 
    # Convert seconds since epoch to struct_time
    timeObj = time.localtime(secondsSinceEpoch)
 
    print(timeObj)
 
    # get the current timestamp elements from struct_time object i.e.
    print('Current TimeStamp is : %d-%d-%d %d:%d:%d' % (
    timeObj.tm_mday, timeObj.tm_mon, timeObj.tm_year, timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec))
 
    # It does not have the microsecond field
 
    print('*** Get Current Timestamp using time.ctime() *** ')
 
    timeStr = time.ctime()
 
    print('Current Timestamp : ', timeStr)
 
 
if __name__ == '__main__':
    main()