import sqlite3
import pandas as pd

conn = sqlite3.connect('stocks.db')

query = """
SELECT Date, "('Close', 'AAPL')", "('MA20', '')", "('MA50', '')", "('Signal', '')"
FROM aapl_prices
WHERE "('Signal', '')" = 1
ORDER BY Date
"""

results = pd.read_sql_query(query, conn)
conn.close()

print(f"Total buy signals: {len(results)}")
print(results.head(10))