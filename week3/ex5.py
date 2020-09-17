# Ex 5: Find each company’s highest priced car

import pandas as pd

df = pd.read_csv('Automobile_data.csv', index_col=0)
highest_prices_car_by_company = df.sort_values('price', ascending=False).drop_duplicates(['company'])

print("Highest prices by company: ", highest_prices_car_by_company)