
# coding: utf-8

# In[16]:

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
print calendar.TextCalendar(calendar.SUNDAY).formatyear(2015, 2, 1, 6, 4)


# In[ ]:



