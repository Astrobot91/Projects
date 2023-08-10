import os
import input
import pandas as pd
import datetime as dt
from re import sub


stock_symbol = input.ask_string("Enter the stock symbol as per YF: ").upper()
interval_unit = input.ask_string("Enter Unit [Minutes/Hours]: ").title()
interval_value = input.ask_string("Enter Value [1/5/15]: ")

stock_data = pd.read_csv(f"Data/{stock_symbol}/{stock_symbol}-{interval_value}-{interval_unit}-DATA.csv")

stock_data["Date"] = pd.to_datetime(stock_data["Date"])
stock_data["Time"] = pd.to_datetime(stock_data["Time"])

interval_value = int(interval_value)


# for timedelta m = minutes and h = hours. Change values resp.
interval_unit = interval_unit.lower()
if interval_unit == "m":
    interval_unit = "minutes"
elif interval_unit == "h":
    interval_unit = "hours"


# Create a Dict Value for timedelta Arg
timedelta_args = {interval_unit: interval_value}

date_groups = stock_data.groupby("Date")


# This iterator will iterate all the groups one at a time using "next" function.
iterator = iter(date_groups.groups.keys())

# Open a file to store the wrong or the missing data
with open("logfile.txt", "w") as file:

    # Loop till the number of groups in date_groups
    for group in date_groups:
        
        # Handling the StopIteration Error: Occurs because Python doesn't know when to stop iterations
        try:

        # Store the group in th group_store as a DATAFRAME
            group_store = pd.DataFrame(date_groups.get_group(next(iterator)))
            
            # Counter takes the first Value of the Time column in group
            counter = group_store["Time"].iloc[0]
            
            # Loop through the Time 
            for i in range(len(group_store["Time"])):

                # If counter is equal to first value of Time Column, increase counter by 5 mins.
                if counter == group_store["Time"].iloc[i]:
                    counter = counter + dt.timedelta(**timedelta_args)

                # Else Log the incorrect data and change counter to the next Time Value.    
                else:
                    file.write(f"Date: {group_store['Date'].iloc[i]}   Incorrect Value: {group_store['Time'].iloc[i]}    Corrected Value: {counter}\n")
                    counter =  group_store['Time'].iloc[i] + dt.timedelta(**timedelta_args)
            
        except StopIteration:
            pass

# Read all the lines of the file
with open("logfile.txt", "r") as file:
    content = file.read()


# Substitute Date: 2015-03-13 00:00:00 by Date: 2015-03-13 using re.sub
# \1 refers to 1st group of regex
content = sub(r"Date: (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})", r"Date: \1", content)


# Same substitutions done, but chose group 2 as group 2 holds time value.
content = sub(r"Incorrect Value: (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})", r"Incorrect Value: \2", content)
content = sub(r"Corrected Value: (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})", r"Corrected Value: \2", content)


# Stored new values in logfile
with open("logfile.txt", "w") as outfile:
    outfile.write(content)
 
       
# Read the logfile
print()
with open("logfile.txt", "r") as file:
    for line in file:
        print(line)

if os.stat("logfile.txt").st_size == 0:
    print("No data missing, excellent!\n")
else:
    print("Listed are missing data points.\n")