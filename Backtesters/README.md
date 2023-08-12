# Backtester V1

## Overview

The Backtester V1 is a program designed for backtesting trading strategies on historical price data. It employs various indicators and conditions to simulate trades and calculate potential profits and losses. The program focuses on CPR levels (Central Pivot Range) as well as candlestick patterns for identifying potential entry and exit points. The trading strategies are divided into a long-side and a short-side approach.

## Indicators and Strategies

The program uses the following indicators:

### Indicators

- EMA20: Exponential Moving Average with a period of 20.
- EMA50: Exponential Moving Average with a period of 50.
- CPR (Camarilla Pivot Range): Calculated using the standard CPR formula.

## Execution Flow

1. Load and Preprocess Data: The program reads historical OHLC (Open-High-Low-Close) data from a CSV file. It calculates EMA20 and EMA50 for each trading day.

2. Calculate CPR Levels: The program calculates CPR levels using the standard CPR formula based on the day's OHLC values. CPR levels are used as potential support and resistance levels.

3. Determine CPR Level Combinations: The program generates combinations of CPR levels based on trade direction (long or short). These combinations help identify which CPR level combinations are crossed in the desired trade direction.

4. Backtesting: The strategies are executed based on the identified CPR level combinations. Entry and exit conditions are applied to historical data to simulate trades. For each trade, information such as entry price, stop-loss, exit price, and risk-reward ratio are recorded.

5. Results: The program generates various statistics about the backtested trades, including net earnings, cumulative P&L, RR ratio, accuracy, and more.

Overall, the Backtester V1 is a starting point for developing and testing trading strategies. Will build upon this foundation to create more sophisticated and profitable trading algorithms.

## Acknowledgments

This program was developed as a practice project to understand Algorithmic Backtesting and Trading. It is not intended to be used for professional purposes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.