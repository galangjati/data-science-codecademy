import codecademylib3_seaborn
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')

df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']

f, ax = plt.subplots(figsize=(12, 7))
sns.set_style('whitegrid')
sns.set_context('poster', font_scale=2)
ax = sns.barplot(data=df, x='Year', y='Total Goals')
ax.set_title('Total Goals for Each World Cup')
plt.show()
plt.clf()

df_goals = pd.read_csv('goals.csv')

f, ax2 = plt.subplots(figsize=(12, 7))
sns.set_context('notebook', font_scale = 1.25)
ax2 = sns.boxplot(data=df_goals, x='year', y='goals', palette = "Spectral")
ax2.set_title('Persebaran jumlah gol pada World Cup')
plt.show()