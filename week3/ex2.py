# Ex 2: Find the most expensive car company name

import pandas as pd

df = pd.read_csv('Automobile_data.csv', index_col=0)
most_expensive_car = df.nlargest(1, ['price'])

print("Most expensive car is: ", most_expensive_car)