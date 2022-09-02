import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
sns.set_style('darkgrid')
sns.set(rc={'figure.figsize':(14,8)})

dataset = pd.read_csv('AAPL.csv')
df = pd.DataFrame(dataset)
df['Date'] = pd.to_datetime(df['Date'])
updatedDate = df.copy()

ax = sns.lineplot(data=df, x='Date', y='Close', palette='viridis', legend='full', lw=3)
plt.ylabel('Close')
plt.xlabel('Year-Month-Day')
plt.show()
df['Date'].values.tolist()
for index in updatedDate.index:
    if index > 0:
        # print("Before: " + str(updatedDate.loc[index, 'Close']))
        updatedDate.loc[index, 'Close'] = df.loc[index, 'Close'] - df.loc[index - 1, 'Close']
        # print("After: " + str(updatedDate.loc[index, 'Close']))

ax = sns.lineplot(data=updatedDate, x='Date', y='Close', palette='viridis', legend='full', lw=3)
plt.ylabel('Difference')
plt.xlabel('Year-Month-Day')
plt.show()
