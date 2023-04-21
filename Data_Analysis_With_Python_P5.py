import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('Data_Analysis_With_Python_P5_epa-sea-level.csv')

#%%
fig , ax = plt.subplots(1)
ax.plot(df['Year'], df['CSIRO Adjusted Sea Level'])

#%%
plt.plot(df['Year'], df['CSIRO Adjusted Sea Level'], 'o')
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


#%%
reg = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
s = reg.slope
i = reg.intercept

#%%
df_2000 = df.loc[df['Year'] > 1999]

reg_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
s_2000 = reg_2000.slope
i_2000 = reg_2000.intercept

#%%
anios1 = pd.date_range('1880', '2050', freq='Y').year
anios2 = pd.date_range('2000', '2050', freq='Y').year


#%%
plt.plot(df['Year'], df['CSIRO Adjusted Sea Level'], 'o')
plt.plot(df['Year'], i + s * df['Year'])
plt.plot(df_2000['Year'], i_2000 + s_2000 * df_2000['Year'], color = 'green')

#%%
plt.plot(df['Year'], df['CSIRO Adjusted Sea Level'], 'o')
plt.plot(anios1, i + s * anios1)
plt.plot(anios2, i_2000 + s_2000 * anios2, color = 'green')

plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt
