# Import numpy as np
import numpy as np

np_height = np.random.normal(loc=73.68, scale=2.31, size=(1015, 1))
np_weight = np.random.normal(loc=201.35, scale=20.81, size=(1015,1))
np_baseball = np.concatenate((np_height, np_weight), axis=1)
print(np_baseball.shape)
# For loop over np_height
for np_height_item in np_height:
    print(str(np_height_item) + " inches")

# For loop over np_baseball
for np_baseball_item in np.nditer(np_baseball):
    print(np_baseball_item)

# Import cars data
import pandas as pd
cars = pd.read_csv('data/cars.csv', index_col = 0)

# Iterate over rows of cars
for label, row in cars.iterrows():
    print(label)
    print(row)

for lab, row in cars.iterrows() :
    print("{}: {}".format(lab, row['cars_per_cap']))

# Code for loop that adds COUNTRY column
for label, row in cars.iterrows():
    cars.loc[label, 'COUNTRY'] = row['country'].upper()

print(cars)

# Use .apply(str.upper)
cars['COUNTRY'] = cars['country'].apply(str.upper)
