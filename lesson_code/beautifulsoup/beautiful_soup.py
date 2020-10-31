import codecademylib3_seaborn
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')

soup = bs(webpage.content, 'html.parser')

rating_raw = soup.find_all(attrs={'class':'Rating'})

ratings = []

for rating in rating_raw[1:]:
  ratings.append(float(rating.string))

plt.hist(ratings)
plt.show()

companies_raw = soup.select('.Company')

companies = []

for company in companies_raw[1:]:
  companies.append(company.get_text())

data = {'company' : companies, 'rating' : ratings}

df = pd.DataFrame.from_dict(data)

company = df.groupby('company').rating.mean()
ten_best = company.nlargest(10)
#print(ten_best)

#print(soup)
percent_raw = soup.select('.CocoaPercent')

percentage = []

for p in percent_raw[1:]:
  percent = int(float(p.get_text().strip('%')))
  percentage.append(percent)

data['cocoapercentage'] = percentage
df = pd.DataFrame.from_dict(data)

plt.clf()
plt.scatter(df.cocoapercentage, df.rating)
z = np.polyfit(df.cocoapercentage, df.rating, 1)
line_function = np.poly1d(z)
plt.plot(df.cocoapercentage, line_function(df.cocoapercentage), "r--")
plt.show()