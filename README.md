# Projects Repository

Welcome to the "Projects" repository on GitHub! This repository is dedicated to storing all of my projects, showcasing the diverse range of work and coding endeavors I have undertaken.

## About

As a passionate developer, I enjoy exploring various domains of programming and creating practical solutions to real-world challenges. This repository serves as a central hub where I can organize, document, and share my projects with others.

## Repository Structure

The "Projects" repository is designed to be well-organized for easy navigation and access to individual projects. Each project will have its own directory, which contains all the relevant files, documentation, and resources associated with that project. Additionally, I will provide detailed README files within each project directory, explaining the purpose, features, and usage of the project.

## Contribution

While this repository primarily serves as a personal showcase, I am open to collaboration and feedback. If you find any of my projects interesting or have suggestions for improvement, feel free to create issues or submit pull requests. I value the community's input and am always eager to learn from others.

## Projects Overview

Here is a brief overview of some of the projects you can find in this repository:

1. **Backtester V1**: The Backtester V1 is a Python-based backtesting program designed for evaluating trading strategies using historical price data. It incorporates technical indicators like Exponential Moving Averages (EMA20 and EMA50) and Camarilla Pivot Range (CPR) levels to assess trading performance. The program implements both long and short side strategies, considering specific entry and exit conditions based on indicators and candlestick patterns like hammer candles. It calculates and records key trade metrics such as entry and exit prices, risk-reward ratios, cumulative profits and losses, and accuracy. While offering a solid foundation for testing trading strategies, the program has potential for further improvement through strategy refinement, advanced indicator integration, parameter optimization, efficiency enhancements, and better risk management techniques. Users can clone the repository, customize strategies, and iterate to develop tailored algorithms aligned with their trading objectives. With its versatile design, the Backtester V1 empowers traders to backtest, refine, and optimize strategies for enhanced trading outcomes.

2. **Stock-Data-Downloader**: The Data Downloader is a Python script that allows users to retrieve historical stock data for a specified stock symbol from Yahoo Finance. The script prompts the user to input the stock symbol, period (1d/1w/1mo/1y), and interval (1m/1h) for data retrieval. Upon execution, the script uses the `yfinance` library to fetch the stock data based on the user's input. It then processes the data and segregates it based on the date, creating separate CSV files for each date under the "Data" folder. Additionally, a log file is generated that contains information about any missing or incorrect time points during data scraping. The Data Downloader aims to be user-friendly and dynamic by allowing users to choose their desired time period and interval. It handles data validation and provides feedback to users through the logfile, where any discrepancies in the time intervals are logged. This project serves as a useful tool for collecting and organizing historical stock data for analysis, research, or building financial models. As an open-source project, it encourages collaboration and contributions from the community to enhance its functionality and adapt it for other data scraping purposes.

3. **health-tracker**: The provided Python program implements a health tracker application using object-oriented programming (OOP) principles. It calculates and provides personalized health insights to users based on their input data. Users provide information like age, gender, weight, height, and body fat percentage. The program then calculates the user's Basic Metabolic Rate (BMR) using different formulas and offers recommendations for daily caloric intake based on their activity level. Users can also set fitness goals, such as weight gain, loss, or maintenance, and the program calculates the required caloric intake to achieve those goals. It incorporates error handling for various inputs and utilizes numpy for numerical computations.
The program starts by gathering user data and creating an instance of the ErrorChecker class. It allows users to select different BMR formulas, lifestyle activity levels, and fitness goals. The modular structure and interactive approach make the program user-friendly and informative. It provides valuable insights for individuals aiming to manage their health and fitness effectively.

## License

All projects in this repository are open-source and released under the [MIT License](LICENSE). You are free to explore, use, and modify the code for your own purposes. However, please make sure to attribute the original work to me and include the appropriate license in any derivative works.

## Connect with Me

If you have any questions, ideas, or simply want to connect with me, feel free to reach out through GitHub or my other social media platforms. I am always excited to engage with fellow developers and learn from their experiences.

Thank you for visiting the "Projects" repository, and I hope you find the projects here inspiring and useful!

Happy coding! 🚀
