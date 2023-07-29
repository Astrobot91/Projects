# import all libraries
import os
import pandas as pd
import yfinance as yf
import datetime as dt
import re
import input


# Get user input
print("\nEnter 'exit' in all inputs to exit the program\n")
stock_symbol = input.ask_string("Enter Stock Symbol [As per YF]: ").upper()
period = input.ask_string("Enter Period [1d/1w/1mo/1y]: ").strip()
interval = input.ask_string("Enter Interval [1m/1h]: ").strip()


# Get today's date to name the file
timestamp = dt.datetime.now()
date_today = timestamp.date()
date_today = date_today.strftime("%d-%m-%Y")


# Get NIFTY50 stock data from yahoo finance
stock_name = yf.Ticker(f"{stock_symbol}")   
data_today = stock_name.history(period = f"{period}", interval = f"{interval}") 


# Split the input of interval "5m" in to '5' and 'm' to make the program more dynamic.
# Here, regex re.sub is used. re.search could be used as well.
interval_value, interval_unit = re.sub(r"(\d)(\D)", r"\1 \2", interval).split()
interval_value = int(interval_value)


# for timedelta m = minutes and h = hours. Change values resp.
interval_unit = interval_unit.lower()
if interval_unit == "m":
    interval_unit = "minutes"
elif interval_unit == "h":
    interval_unit = "hours"

# Create a Dict Value for timedelta Arg
timedelta_args = {interval_unit: interval_value}
data_today = data_today.reset_index()   # Before, Datetime Column was taken as index


# Extract Time and Date into seperate columns
data_today["Date"] = data_today["Datetime"].dt.strftime("%Y-%m-%d")     # Covert to strings for splitting Date and Time
data_today["Time"] = data_today["Datetime"].dt.strftime("%H:%M:%S")

data_today = data_today[["Date", "Time", "Open", "High", "Low", "Close"]].round(2)


# Making a duplicate for making seperate files according to date 
data_for_seggregation = data_today[["Date", "Time", "Open", "High", "Low", "Close"]].round(2)

if not os.path.exists(f"Data/{stock_symbol}/{interval_value}-{interval_unit.title()}/LOGS"):
    try:
        os.makedirs(f"Data/{stock_symbol}/{interval_value}-{interval_unit.title()}/LOGS")   
    except FileExistsError as e:
        print(f"\nFolders already exist - {e}")
else:
    print("\nAll folders in place - Check.")

data_today.to_csv(f"Data/{stock_symbol}/{interval_value}-{interval_unit.title()}/{date_today}.csv", index = False) # SAVE DATA for merging it later

data_today["Date"] = pd.to_datetime(data_today["Date"])     # Convert back to Timestamp again
data_today["Time"] = pd.to_datetime(data_today["Time"])

data_today_group = data_today.groupby("Date")      # Create group as per date NOTE: Groups are made if 2 dates come in the data
iterator = iter(data_today_group.groups.keys())        # Create iterator to iterate over the groups, doesn't store value of group. Only iterates

group_store = data_today_group.get_group(next(iterator))       # Store the "Value" of group in variable


# Create log file to store missing time
with open(f"Data/{stock_symbol}/{interval_value}-{interval_unit.title()}/LOGS/{date_today}-logfile.txt", "w") as file:
    for group in data_today_group:
        try:
            group_df = data_today_group.get_group(next(iterator)) 
            time_counter = group_df["Time"].iloc[0]
            for i in range(len(group_df["Time"])):
                if time_counter == group_df["Time"].iloc[i]:
                    time_counter += dt.timedelta(**timedelta_args)    # This holds the Dict Value {interval_unit: interval_value}
                else:
                    file.write(f"Date: {group_df['Date'].iloc[i]}      Incorrect Value: {group_df['Time'].iloc[i]}      Correct Value: {time_counter}\n")
                    time_counter = group_df['Time'].iloc[i] + dt.timedelta(**timedelta_args)
        except StopIteration:
            pass


with open(f"Data/{stock_symbol}/{interval_value}-{interval_unit.title()}/LOGS/{date_today}-logfile.txt", "r") as file:
    line = file.read()
line = re.sub(r"Date: (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})", r"Date: \1", line)
line = re.sub(r"Incorrect Value: (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})", r"Incorrect Value: \2", line)
line = re.sub(r"Corrected Value: (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})", r"Corrected Value: \2", line)
with open(f"Data/{stock_symbol}/{interval_value}-{interval_unit.title()}/LOGS/{date_today}-logfile.txt", "w") as file:
    file.write(line)


if not os.path.exists(f"Data/{stock_symbol}/{stock_symbol}-{interval_value}-{interval_unit.title()}-DATA.csv"):
    try:
        with open(f"Data/{stock_symbol}/{stock_symbol}-{interval_value}-{interval_unit.title()}-DATA.csv", "w") as file:
            file.write("Date,Time,Open,High,Low,Close") 
    except FileExistsError as e:
        print(f"\nThe File already exists - {e}")
else:
    print("\nStock-Data file in place - Check!")

old_data = pd.read_csv(f"Data/{stock_symbol}/{stock_symbol}-{interval_value}-{interval_unit.title()}-DATA.csv")
new_data = pd.read_csv(f"Data/{stock_symbol}/{interval_value}-{interval_unit.title()}/{date_today}.csv")

data_merger = pd.concat([old_data, new_data], ignore_index = True).drop_duplicates()
data_merger.to_csv(f"Data/{stock_symbol}/{stock_symbol}-{interval_value}-{interval_unit.title()}-DATA.csv", index = False)
print("\nMerged the data successfully!")
print(f"\nSome data points are missing in the dataset. Please check the logfile at location: 'Data/{stock_symbol}/{interval_value}-{interval_unit.title()}/LOGS/{date_today}-logfile.txt'.")


# Change the date format
data_for_seggregation["Date"] = pd.to_datetime(data_for_seggregation["Date"], format = "%Y-%m-%d")
data_for_seggregation["Date"] = data_for_seggregation["Date"].dt.strftime("%d-%m-%Y") 

groups_to_save = data_for_seggregation.groupby("Date")


# Store key of groups in "date". groups in "group". Earlier Iterator was used to do the same thing.
for date, group in groups_to_save:
    day, month, year = date.split("-")
    directory_path = f"Data/{stock_symbol}/{interval_value}-{interval_unit.title()}/{year}/{month}"
    os.makedirs(directory_path, exist_ok = True)
    if not os.path.exists(f"{directory_path}/{date}"):
        group.to_csv(f"{directory_path}/{date}.csv", index = False)
    else:
        print(f"\n{date}.csv Already in place!")


# Remove the existing new_data
os.remove(f"Data/{stock_symbol}/{interval_value}-{interval_unit.title()}/{date_today}.csv")
print()