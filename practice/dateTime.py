import datetime as dt

#DATE:A date in Python is not a data type of its own, but we can import a module named datetime to work with
#dates as date objects
#Display date using this method
date = dt.datetime.now()
print(date)
print(date.year)

#Creating date object using the datetime() class constructor
me = dt.datetime(2025, 2, 26)
print(me)

#The strftime() method is used for formatting date object into readable string and display the format of the
#returned string
print(date.strftime("%a")) #Short version of today
print(date.strftime("%A")) #Full version of today
print(date.strftime("%b")) #Stort version of month
print(date.strftime("%B")) #Full version of month
print(date.strftime("%c")) #Shows local version of date and time
print(date.strftime("%C")) #Shows the century (20 from 2025)
print(date.strftime("%y")) #Short version of year (18)
print(date.strftime("%Y")) #Full version of year (2018)
print(date.strftime("%m")) #Numeric version of month
print(date.strftime("%M")) #Numeric version of Minutes
print(date.strftime("%S")) #Numeric version of Seconds
print(date.strftime("%f")) #Numeric version of microsecond
print(date.strftime("%x")) #Shows the local version of date
print(date.strftime("%X")) #Shows the local version of time
print(date.strftime("%u")) #International standard of weekday (1 - 7)
print(date.strftime("%w")) #Numeric version of today (it starts from 0 which Sunday)[0-6]
print(date.strftime("%W")) #Shows the week in the exact point of the year (Monday as the first day of the week)
print(date.strftime("%U")) #Shows the week in the exact point of the year (Sunday as the first day of the week)
print(date.strftime("%j")) #Shows the day in the exact point of the year
print(date.strftime("%z")) #UTC offset (+01:00)
print(date.strftime("%Z")) #Timezone (West African Time [WAT])
print(date.strftime("%d")) #Day of the month (numeric)
print(date.strftime("%V")) #International standard of weeknumber (01 - 53)
print(date.strftime("%G")) #International standard of year
print(date.strftime("%H")) #Hours in the 24 hours format
print(date.strftime("%I")) #Hours in the 12 hours format
print(date.strftime("%p")) #Shows the AM / PM for the 12 hours format
print(date.strftime("%%")) #Displays the % character