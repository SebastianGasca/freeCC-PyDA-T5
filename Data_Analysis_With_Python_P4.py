import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dateparse = lambda dates: pd.to_datetime(dates, format='%Y-%m-%d')
df = pd.read_csv('Data_Analysis_With_Python_P4_fcc-forum-pageviews.csv', 
                 index_col='date',
                 parse_dates=['date'],
                 date_parser= dateparse)

df.head() #resumen 
df.describe() #estadistcas
df.dtypes #tipos de variables

df.quantile([.025, 0.975])
p25 = df.quantile([.025, 0.975]).iloc[0,0]
p975 = df.quantile([.025, 0.975]).iloc[1,0]

df_sin_out = df[(df['value'] > p25) & (df['value'] < p975)]
df_sin_out.head() 

#df_sin_out['date'] = pd.to_datetime(df_sin_out['date'])
#df_sin_out.dtypes

#G1
#df_sin_out = df_sin_out.reset_index()

fig, ax = plt.subplots(figsize=(12, 6))

#ax.plot(df_sin_out['date'] , df_sin_out['value']); 
ax.plot(df_sin_out.index , df_sin_out['value']); 

ax.set_title('Daily freeCodeCamp Forum Page Views')
ax.set_ylabel('Pages Views')   
ax.set_xlabel('Date')

#G2
df_sin_out = df_sin_out.reset_index()

df_sin_out['Years'] = df_sin_out['date'].dt.year
df_sin_out['Months'] = df_sin_out['date'].dt.strftime('%B')

df_anio_mes_mean = df_sin_out.groupby(["Years","Months"]).mean()
df_anio_mes_mean = df_anio_mes_mean['value'].round()
df_anio_mes_mean = df_anio_mes_mean.reset_index()

df_anio_mes_mean['Months'].unique()
categorias = pd.Series(['January', 'February', 'March', 'April', 'May', 'June', 'July',
                        'August', 'September', 'October', 'November', 'December'])
df_anio_mes_mean['Months'] = pd.Categorical(df_anio_mes_mean['Months'], categories=(categorias))

sns.set(rc={'figure.figsize':(8,8)})
fig, ax = plt.subplots(1)
sns.barplot(x = 'Years', y = 'value', hue = 'Months', data = df_anio_mes_mean, ax = ax)
ax.legend(loc = 'upper left', title = 'Months')
ax.set(ylabel = 'Average Page Views')

#G3
categorias = pd.Series(['January', 'February', 'March', 'April', 'May', 'June', 'July',
                        'August', 'September', 'October', 'November', 'December'])
df_sin_out['Months'] = pd.Categorical(df_sin_out['Months'], categories=(categorias))

fig, (ax1, ax2) = plt.subplots(1,2)

g1 = sns.boxplot(x = 'Years', y = 'value', data = df_sin_out, ax = ax1)
g1.set(xlabel = 'Year', ylabel = 'Pages Views', title = 'Years-wise Box Plot (Trend)')

sns.set(rc={'figure.figsize':(12,8)})
g2 = sns.boxplot(x = 'Months', y = 'value', data = df_sin_out, ax = ax2)
g2.set(xlabel = 'Month', ylabel = 'Pages Views', title = 'Months-wise Box Plot (Seasonality)')

#--