# 1. Stock Data Scraper

This Python script allows you to scrape historical stock data for a specified stock symbol from Yahoo Finance and then segregate the data based on the chosen interval. The script saves the scraped data in CSV format and creates separate CSV files for each date to organize the data effectively. Additionally, it generates a logfile that contains information about missing time points during data scraping.

## Getting Started


Run the `data_scraper.py` script first as this downloads, checks and logs only the new data. 

To use this script, you need to have Python and the required libraries installed on your system. The necessary libraries used in this script are:

- os
- pandas
- yfinance
- datetime
- re
- input (This library is custom-made and available in Stock-Data-Scraper folder. It takes input and also does error handling.)

Please ensure you have these libraries installed before running the script.

## User Input

The script prompts the user to input the following parameters:

1. Stock Symbol [As per Yahoo Finance]: The ticker symbol of the stock for which you want to scrape the data.

2. Period [1d/1w/1mo/1y]: The time period for which you want to fetch the historical data. Options include 1 day, 1 week, 1 month, or 1 year.

3. Interval [1m/1h]: The frequency at which the data should be fetched. Options include 1 minute or 1 hour.

4. There are limitations by Yahoo Finance to the amount of data that can be downloaded according to the time frame. The limitations will be shown in the form of an error-handling done by Yahoo Finance module functions.

## Execution

The script performs the following steps:

1. Scrapes historical stock data using Yahoo Finance API based on the user input (stock symbol, period, and interval).

2. Creates a CSV file for the scraped data and saves it in the "Data" folder with the appropriate naming convention.

3. Segregates the data based on the date and creates separate CSV files for each date under the "Data" folder.

4. Generates a logfile that contains information about missing time points during data scraping. The logfile is saved under the "LOGS" folder inside the respective date's folder.

5. Merges the newly scraped data with any existing data in the "DATA" file to maintain a comprehensive historical record.

6. Cleans up temporary files created during process of merging by removing the existing new_data CSV file.

## Output

The script saves the historical stock data in CSV format under the "Data" folder. The data is organized into separate CSV files based on each date. The "LOGS" folder under each date contains a logfile that lists missing time points during data scraping.

Please note that this script assumes that you have write permissions in the working directory to create folders and files for storing the data.

## Notes

- The `input` library is custom-made and imported from a local file. Make sure that the `input` library is available and functional before running the script.

- The script is designed to fetch historical stock data from Yahoo Finance. In case the Yahoo Finance API changes or is not accessible, the script may need modifications to work with an alternative data source.

- Always verify the accuracy and completeness of the data scraped by the script to ensure its suitability for your specific use case.


# 2. Stock Data Checker

This Python script allows you to validate the time intervals in historical stock data. It checks if the time intervals are consistent based on the specified interval unit (minutes/hours) and value (1, 5, or 15). The script reads the historical stock data from a CSV file and outputs a logfile containing information about any incorrect or missing time points. Use this program to check the complete historical record at file location `Data/stock_symbol/stock_symbol-interval_value-interval_unit-DATA.csv`

## Getting Started

Run the script `data_checker.py` to check the historical record created by `data_scraper.py`. 

To use this script, ensure that you have Python and the required libraries installed on your system. The script requires the following libraries:

- os
- input
- pandas
- datetime

## User Input

The script prompts the user to input the following parameters:

1. Stock Symbol [As per Yahoo Finance]: The ticker symbol of the stock for which you want to validate the time intervals. input eg: AAPL

2. Interval Unit [Minutes/Hours]: The unit of the time interval, either "Minutes" or "Hours." input eg: minutes, hours

3. Interval Value [1/5/15]: The numeric value representing the time interval. Options include 1, 5, 15, etc.

4. Error handling done here is not tough. Please enter the right input to access the file.

## Execution

The script performs the following steps:

1. Reads the historical stock data from the CSV file located at `Data/stock_symbol/stock_symbol-interval_value-interval_unit-DATA.csv`. eg: `Data/AAPL/AAPL-5-Minutes-DATA.csv`

2. Converts the "Date" and "Time" columns to datetime objects for better handling.

3. Validates the time intervals based on the specified interval unit and value.

4. Logs any incorrect or missing time points into a logfile named `logfile.txt`.

5. Displays the contents of the logfile, indicating any incorrect or missing time points.

6. If no missing data is found, the script displays a message "No data missing, excellent!".

## Output

The script generates a logfile (`logfile.txt`) that contains information about any incorrect or missing time points in the historical stock data. If the logfile is empty, it means that the time intervals are consistent and no data is missing.

## Notes

- The `input` library seems to be custom-made or imported from a local file. Make sure that the `input` library is available and functional before running the script.

- This script assumes that you have the historical stock data saved in a CSV file with the specified naming convention (`Data/{stock_symbol}/{stock_symbol}-{interval_value}-{interval_unit}-DATA.csv`).

- The script aims to validate the time intervals based on the specified interval unit and value. It does not modify the original data but provides information about any discrepancies found during the validation process.

## Disclaimer

This script is intended for educational and informational purposes only. The developers of this script do not guarantee the accuracy, completeness, or reliability of the historical stock data or the results of the validation process. Any actions you take based on the information provided by this script are at your own risk.

## License

This script is released under the [MIT License](LICENSE). You are free to modify and distribute the script, but the developers disclaim any liability arising from its use.

---

Please make sure to provide the missing parts, such as the `input` library, and complete the code if there are any additional functionalities you wish to implement. Remember that this readme assumes some information about the missing parts to provide a comprehensive overview of the script's purpose and usage.
