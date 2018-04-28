#Description: Media Room Expiration Dates project designed to speed up the work process by displaying expiration dates
#relative to the present julian date

#By: Deborah Perez

#Import calendar module, once.
import calendar

#Formatted as Sunday to Saturday
c = calendar.TextCalendar(calendar.SUNDAY)

#set the current month to be november 2015
c.prmonth(2015, 11)

#print calendar year formatted as Sunday to Saturday
#formatyear parameters(year, width, legnth, spacing in between months, months per row)
print (calendar.TextCalendar(calendar.SUNDAY).formatyear(2015, 2, 1, 6, 4))

#import time module
import time
#print current day in mm/dd/yyyy format
print (time.strftime("%m/%d/%Y"))

#Import Datetime module
import datetime
#today's date
today = datetime.date.today()
print ('Today              :', today)

#5 days calculation for expiration date in calendar days
fivedays = datetime.timedelta(days=5)
expfivedays = today + fivedays
print ('5 Days Expiration  :', expfivedays)

#1 week calculation for expiration date in calendar days
oneweek = datetime.timedelta(days=7)
exponeweek = today + oneweek
print ('1 Week Expiration  :', exponeweek)

#2 weeks calculation for expiration date in calendar days
twoweeks = datetime.timedelta(days=14)
exptwoweeks = today + twoweeks
print ('2 Weeks Expiration :', exptwoweeks)

#3 weeks calculation for expiration date in calendar days
threeweeks = datetime.timedelta(days=21)
expthreeweeks = today + threeweeks
print ('3 Weeks Expiration :', expthreeweeks)

#6 weeks calculation for expiration date in calendar days
sixweeks = datetime.timedelta(days=42)
expsixweeks = today + sixweeks
print ('6 Weeks Expiration :', expsixweeks)
