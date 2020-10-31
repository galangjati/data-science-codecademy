import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

states = glob.glob('states*.csv')

census = []
for state in states:
  data = pd.read_csv(state)
  census.append(data)

us_census = pd.concat(census)

us_census['Income'] = us_census['Income'].replace('[\$,]', '', regex=True)

gender_split = us_census['GenderPop'].str.split('_')

us_census['Men'] = gender_split.str.get(0)
us_census['Women'] = gender_split.str.get(1)

us_census['Men'] = us_census['Men'].replace('[M,]', '', regex=True)
us_census['Women'] = us_census['Women'].replace('[F,]', '', regex=True)

us_census['Men'] = pd.to_numeric(us_census['Men'])
us_census['Women'] = pd.to_numeric(us_census['Women'])

us_census = us_census.fillna(value={'Women':(us_census['TotalPop'] - us_census['Men'])})

us_census = us_census.drop_duplicates()

print(us_census.columns)

plt.scatter(us_census['Women'], us_census['Men'])
plt.show()