# Ex 7: Sort all cars by Price column

import pandas as pd

df = pd.read_csv('Automobile_data.csv', index_col=0)
sorted_by_price = df.sort_values('price', ascending=False)

print("Cars sorted by price: ", sorted_by_price)