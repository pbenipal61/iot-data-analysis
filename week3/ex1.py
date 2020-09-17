# Ex 1: From given data set print first and last five rows

import pandas as pd

df = pd.read_csv('Automobile_data.csv', index_col=0)
first_five_rows = df.head()
last_five_rows = df.tail()

print("First 5 rows are: ", first_five_rows)
print("Last 5 rows are: ", last_five_rows)