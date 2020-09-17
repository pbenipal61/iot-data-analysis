# Ex 6: Find the average mileage of each car making company

import pandas as pd

df = pd.read_csv('Automobile_data.csv', index_col=0)
avg_mileage_by_company = df.groupby(['company'], as_index=False)['average-mileage'].mean()

print("Average mileage by company: ", avg_mileage_by_company)