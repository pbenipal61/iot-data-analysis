# Ex 4: Count total cars per company

import pandas as pd

df = pd.read_csv('Automobile_data.csv', index_col=0)
total_cars_per_company = df['company'].value_counts()

print("Total cars per company: ", total_cars_per_company)