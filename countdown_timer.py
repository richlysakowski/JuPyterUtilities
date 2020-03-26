# -*- coding: utf-8 -*-
""" Created on Thu Feb  7 23:00:00 2019 by @author: lysak """

#%%
'''
Here is a Countdown Timer script that counts from 01:05 to 00:00 in MM:SS format.
Originally "Countdown Timer" By Adam Gay

# The original code came from https://stackoverflow.com/questions/25189554/countdown-clock-0105
  and was updated with better comments 
This is a synchronous, i.e., blocking process.  
'''

import time
import sys

print(' ')
print('Instructions: Input time to countdown from.')
print(' ')

c=':'

hourz = input('Hours: ')
minutesz = input('Minutes: ')
secondsz=input('Seconds: ')
print(' ')

hour = int(hourz)
minutes = int(minutesz)
seconds = int(secondsz)

while hour > -1:
    while minutes > -1:
        while seconds > 0:
            seconds=seconds-1
            time.sleep(1)
            seconds1 = ('%02.f' % seconds)  # format
            minutes1 = ('%02.f' % minutes)
            hour1 = ('%02.f' % hour)
            sys.stdout.write('\r' + str(hour1) + c + str(minutes1) + c + str(seconds1)+' ')

        minutes = minutes-1
        seconds = 60
    hour = hour-1
    minutes = 59

print(f'\n\nCountdown Complete.  It for {hourz} hours, {minutesz} minutes, {secondsz} seconds.')
# time.sleep(30)

#%%
""" Here's another countdown timer function. """
# a countdown clock in Python that looks like 00:00 (min & sec) 
# from https://stackoverflow.com/questions/25189554/countdown-clock-0105
import time
import sys

def countdown_timer(t):
    mins, secs = divmod(t, 60)
    original_mins, original_secs = mins, secs
    print(f'\n\nThe Countdown() function will run for {original_mins} minutes, {original_secs} seconds.\n')
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print('\r' + 'Time Elapsed:  ', timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print(f'\nCountdown Complete.  It ran {original_mins} minutes, {original_secs} seconds.')
    print('\nGoodbye!')
    # Issue an exit function just to make sure a normal exit occurs. 
    sys.exit

countdown_timer(5)

# Issue an exit function just to make sure a normal exit occurs. 
sys.exit
