import yfinance as yf
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Download stock data
ticker = "AAPL"
df = yf.download(ticker, start="2024-01-01", end="2024-12-31")

print(df.head(10))
print(f"\nRows downloaded: {len(df)}")

df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()

print(df[['Close', 'MA20', 'MA50']].tail(20))

df['Signal'] = 0
df.loc[df['MA20'] > df['MA50'], 'Signal'] = 1
df.loc[df['MA20'] < df['MA50'], 'Signal'] = -1

print(df[['Close', 'MA20', 'MA50', 'Signal']].tail(20))
conn = sqlite3.connect('stocks.db')
df.to_sql('aapl_prices', conn, if_exists='replace')
conn.close()
print("\nData saved to stocks.db")
plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='AAPL Price', color='blue')
plt.plot(df['MA20'], label='20-day MA', color='orange')
plt.plot(df['MA50'], label='50-day MA', color='red')
plt.title('AAPL Price with Moving Average Signals')
plt.legend()
plt.show()