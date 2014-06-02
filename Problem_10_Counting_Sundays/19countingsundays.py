"""
this program is for project euler #19 counting sundays
it makes a calendar list each item being weekday(name), weekday(number), month, year)
from 1900-2000
starting on 1900 because jan 1st is a monday
"""


daysinmonths = {'jan': 31,
          'feb': 28,
          'mar': 31,
          'apr': 30,
          'may': 31,
          'jun': 30,
          'jul': 31,
          'aug': 31,
          'sep': 30,
          'oct': 31,
          'nov': 30,
          'dec': 31}

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
calendar=[]
countsundays=0
currentday = 0
for year in range(1900, 2001):
    for month in months:
        if month == 'feb':
            if year % 4 == 0:
                numofdays = 29
                if year % 100 == 0:
                    numofdays = 28
                    if year % 400 == 0:
                        numofdays =29
            else:
                numofdays=28
        else:
            numofdays = daysinmonths[month]
        for day in range(1,numofdays+1):
            calendar.append([days[currentday], day, month, year])
            if year > 1900:
                if days[currentday] == 'sun':
                    if day == 1:
                        countsundays +=1
            currentday +=1
            if currentday == 7:
                currentday = 0
print(countsundays)
input()
            
    
