# Financial Data Pipeline

A Python pipeline that pulls live stock market data, generates 
trading signals using moving average crossovers, stores the 
results in a SQL database, and visualises price trends.

## What it does

- Downloads real OHLCV stock data from Yahoo Finance using yfinance
- Calculates 20-day and 50-day moving averages
- Generates buy/sell signals when the moving averages cross
- Stores all data in a SQLite database
- Queries the database using SQL to filter buy signals
- Visualises price and signal data using matplotlib

## Why I built it

I built this to understand how financial data pipelines work 
at a fundamental level — from raw price data through to 
actionable trading signals. The moving average crossover is 
one of the simplest systematic trading strategies, making it 
a good foundation for understanding more complex approaches 
used at firms like Marshall Wace.

## Tech stack

- Python 3.12
- pandas — data manipulation and analysis
- yfinance — live market data
- SQLite — local database storage
- matplotlib — visualisation

## How to run it

Clone the repo and install dependencies:

git clone git@github.com:myasimonpeters/finance-pipeline.git
cd finance-pipeline
python -m venv venv
source venv/bin/activate
pip install pandas yfinance matplotlib

Run the pipeline:

python pipeline.py

Query buy signals from the database:

python query.py

## What the signal means

- Signal = 1 (Buy): the 20-day MA is above the 50-day MA, 
  indicating upward momentum
- Signal = -1 (Sell): the 20-day MA is below the 50-day MA, 
  indicating downward momentum
- Signal = 0: insufficient data to calculate both averages

## Results

Running the pipeline on AAPL (2024) shows the stock spent 
the majority of the year in a buy signal, consistent with 
Apple's strong performance throughout 2024.

## Next steps

- Add backtesting to calculate returns if signals were followed
- Expand to multiple tickers simultaneously
- Add anomaly detection for unusual price movements
- Calculate Sharpe ratio and maximum drawdown