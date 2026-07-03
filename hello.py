import pandas as pd
import numpy as np
#create a simple dataset
data = {
    'day' : range(1,11),
    'price' : [100, 102, 101, 105, 107, 106, 110, 108, 112, 115]

}

df = pd.DataFrame(data)
print(df)
print(f"\nAverage price: {df['price'].mean():.2f}")
print(f"Max price: {df['price'].max()}")