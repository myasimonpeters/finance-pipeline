import pandas as pd
data = { 
    'stock' : ['Apple', 'Google', 'Tesla', 'Amazon', 'Microsoft'],
    'price' : [175, 140, 250, 180, 380]
}
df = pd.DataFrame(data)
print(df)
df['price_change'] = df['price'] - df['price'].mean()
print(df)
expensive = df[df['price']> 200]
print(expensive)
prices = pd.read_csv('prices.csv')
print(prices)
sorted_df = df.sort_values('price', ascending=False)
print(sorted_df.head(3))