

#  Downloading Data

#  Access and visualize data in two common data formats:
#    CSV and JSON

#   Weather data recorded  in Sitka, available thru:
#   https://www.nostarch.com/pythoncrashcourse/

#  Parsing csv File Headers

#  Open the file nd store  the file object in f.
#  Call csv.reader and pass it the file object as an arg to 
#     create a reader object 
#  Store the reader object in reader
#  CSV module contains a next() function that returns the next
#     line  in the file when passed the reader object
#  Store the data returned in header_row

import csv

from datetime import datetime

from matplotlib import pyplot as plt

#filename = 'sitka_weather_07-2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #print(header_row)

#  Printing the Header and their positions

#  Use enumerate() on the list to get an index of each item and value

#for index, column_header in enumerate(header_row):
	#print(index, column_header)

#  Extracting and reading data

#  Make an empty list - highs and loop thru the remaining rows in the file
#  The reader object continues from where it left off in the CSV file
#  As we've already read the header row, the loop begins at the second line
#    where the actual data begins
#  On each pass thru the loop, we append the data from index 1, the secoond
#    column to highs
    #highs = []
    #for row in reader:
	    #highs.append(row[1])

    #print(highs)

#  Convert the strings to numbers with int() to be readable in matplotlib
    #highs = []
    #dates, highs = [],[]
    dates, highs, lows = [],[],[]
    for row in reader:
        #current_date = datetime.strptime(row[0], "%Y-%m-%d")
        #dates.append(current_date) 

        #high = int(row[1])
        #highs.append(high)
        
        #low = int(row[3]) 
        #lows.append(low)

    #print(highs)
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#  Plot data

#  Pass the list of highs to plot()
fig = plt.figure(dpi=128, figsize=(10,6))
#plt.plot(highs, c='red')
#plt.plot(dates, highs, c='red')
plt.plot(dates, highs, c='red',alpha=0.5)
#plt.plot(dates, lows, c='blue')
plt.plot(dates, lows, c='blue',alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='green',alpha=0.2)

#plt.title("Daily high temp, July 2014",fontsize=24)
#plt.title("Daily hi and low temp - 2014", fontsize = 24)
title = "Daily hi and low temp - 2014\nDeath Valley,CA"
plt.title(title, fontsize=20)
plt.xlabel('',fontsize=16)

fig.autofmt_xdate()

plt.ylabel("Temp(F)", fontsize=16)
plt.tick_params(axis='both', which='major',labelsize=16)

plt.show()

#  Plotting Dates

#  Convert the string '2014-7-1' to an object representing this date using strptime()
#    from datetime module
#  Create two empty lists to store the date and high temp i.e. dates, highs = [],[]
#  Convert the data containing the date info (row[0]) to a datetime object and append
#    it to dates
#  Pass the date and high temp values to plot()
#  Call fig.autofmt_xdate() - draws the date labels diagonally to prevent overlapping

#  See Date and Time Formatting Args from datetime Module

#  Plotting a larger timeframe

#  Generate a graph for the period's weather

#  Plotting a second date series 

#  Added the empty list lows and then extract/store the low temp for each date from the
#    fourth pistion in each row (row[3])
#  Plot for the low temp and color it blue. Update the title 

#  Shading an area in the chart

#  Use the fill_between() method, that takes a series of x_values and two series of y_values
#    and fills the space btw the two y_values
#  Alpha arg controls a color's transparency (O value = complete transparancy; 1 value = opaque)
#  Facecolor arg determines the color of the shaded region

#  Error checks

#  Generate a temp plot for Death Valley, CA. Error in the program. Traceback tells that Python
#    can;t process the hi temp for one of dates because it can't turn an empty string ('') into
#    an integer. Look at the death-valley_2014.csv shows that on Feb 16,2014, no data was 
#    recorded, therefore the string for the hi temp was empty
#  Address this issue by an error checking code; the values are read from CSV file to handle
#    exceptions that might arise when parsing the data. 

#  Code address the fwllg : 1)each time we examine a row, we try to extract the data and the
#    hi and low temp. If any data is missing, Python will raise a ValueError and we handle it
#    by printing an error msg that includes the date of the missing data 2)After printing the
#    error, the loop continue processing the next row. If all data for a date is retreived
#    without error, the else block will run and the data will be appended to the appropriate
#    lists.
#  When you run highs-lows.py after this code, we'll see that one date had missing data
#  Update the title for the new location

#  Sometimes we can use 'continue' to skip over some data or use remove() or 'del' to 
#    remove some data after extraction. Use any approach that works. Here we use 'try-except-else'
#    block

