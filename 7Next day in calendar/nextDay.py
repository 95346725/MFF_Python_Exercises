#Given a date (consisting of day, month and year, i.e., three integers separated by spaces) determine the next day with respect to the Gregorian Calendar. Output shall be represented by three integers (separated by spaces), too.

#Individual months consist (in this ordering) of 31, 28/29, 31, 30, 31, 30, 31, 31, 30, 31, 30 and 31 days. The leap years are divisible by 4 except of "century-completes" (i.e., years divisible by 100). These (century-completes) are leap years if they are divisible by 400.

#Example
#Input:

#30 4 2009 
#Output:

#1 5 2009


#extra days occur in each year which is an integer multiple of 4 (except for years evenly divisible by 100, which are not leap years unless evenly divisible by 400)
date = str.split(input())
day = int(date[0])
month = int(date[1])
year = int(date[2])

#year
if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False


#month
if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30

if day<month_length:
    day+=1
else:
    day=1
    if month == 12:
        month = 1
        year+=1
    else:
        month += 1
print(day,month,year,sep = " ")