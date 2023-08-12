# Backtester V1

## Overview

The Backtester V1 is a Python-based backtesting framework designed to evaluate trading strategies using historical price data. It combines technical indicators, such as Exponential Moving Averages (EMA), and Camarilla Pivot Range (CPR) levels, with specific entry and exit conditions to simulate and assess trading performance.

## Key Features

- **EMA20 and EMA50:** The program calculates Exponential Moving Averages with periods of 20 and 50, providing insights into trend direction and momentum.
- **CPR Levels:** Camarilla Pivot Range levels are calculated using the standard formula. These levels serve as potential support and resistance levels.
- **Long and Short Side Strategies:** The program includes both long and short side trading strategies based on different entry and exit conditions.
- **Candlestick Patterns:** The strategies incorporate candlestick patterns, such as hammer candles, to identify potential entry points.
- **Backtesting:** Historical price data is used to execute simulated trades, recording key trade metrics such as entry price, exit price, risk-reward ratio, and more.
- **Results and Statistics:** The program generates statistics about the simulated trades, including net earnings, cumulative profits and losses, risk-reward ratios, accuracy, and more.

## How It Works

1. **Data Loading and Preprocessing:** The program loads historical OHLCV (Open-High-Low-Close-Volume) data from a CSV file. It calculates EMA20 and EMA50 for trend analysis.

2. **CPR Calculation:** CPR levels are computed based on the standard formula using the day's OHLC values.

3. **Strategy Execution:** The program implements trading strategies by applying specific entry and exit conditions. These conditions incorporate indicators like EMA and CPR levels, as well as candlestick patterns.

4. **Backtesting and Results:** Trades are simulated using historical data, capturing entry, exit, and other trade-related details. The program calculates key trade metrics and provides an overview of the trading strategy's performance.

## Usage

Users can clone this repository and customize the strategies, indicators, and parameters to suit their trading preferences. By iterating, optimizing, and adding new strategies, traders can develop profitable algorithms tailored to their trading goals.

## Acknowledgments

This program was developed as a practice project to understand Algorithmic Backtesting and Trading. It is not intended to be used for professional purposes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.