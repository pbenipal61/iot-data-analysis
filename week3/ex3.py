# Ex 3: Print All Toyota Cars details

import pandas as pd

df = pd.read_csv('Automobile_data.csv', index_col=0)
all_toyota_cars = df[df['company'] == 'toyota']

print(all_toyota_cars)