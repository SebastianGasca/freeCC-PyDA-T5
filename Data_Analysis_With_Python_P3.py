import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data_Analysis_With_Python_P3_medical_examination.csv');df

#colum
df['height_m'] = df['height'] / 100
df['BMI'] = df['weight'] / df['height_m']**(2)

condicion = [df['BMI'] > 25, df['BMI'] <= 25]
valores = [1,0]
df['overweight'] = np.select(condicion, valores)
df = df.drop(['height_m', 'BMI'], axis = 1)

#standardize
condicion_col = [df['cholesterol'] > 1, df['cholesterol'] == 1]
valores_col = [1,0] 
condicion_glu = [df['gluc'] > 1, df['gluc'] == 1]
valores_glu = [1,0]
df['cholesterol'] = np.select(condicion_col, valores_col)
df['gluc'] = np.select(condicion_glu, valores_glu)

#---
#creando tabla para el grafico
df_pivot = df.loc[:,['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio','overweight']]; df_pivot

## probando 
df_pivot_refinado = (df_pivot.stack()); df_pivot_refinado
df_pivot_refinado = (df_pivot
                     .stack()
                     .reset_index()
                     .rename(columns={'level_1':'atributos', 0:'values'})
                     .drop(columns='level_0') )

df_pivot_refinado.value_counts().sort_index() 

## probando otra cosa 
df_pivot = df.loc[:,['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio','overweight']]

df_pivot_refinado = df_pivot.melt(id_vars = 'cardio'); df_pivot_refinado                    
df_pivot_refinado_v1 = df_pivot_refinado.groupby(['cardio', 'variable', 'value']).agg('size'); df_pivot_refinado_v1
df_pivot_refinado_v2 = df_pivot_refinado.value_counts().sort_index().reset_index().rename(columns = {0:'total'}); df_pivot_refinado_v2

#grafico 1
import matplotlib.pyplot as plt
import seaborn as sns

df_grafico = df_pivot_refinado_v1.reset_index().rename(columns={0:'total'}) ; df_grafico
catplot = sns.catplot(data = df_grafico, x = 'variable', y = 'total', kind = 'bar', hue = 'value', col = 'cardio')

#---
#limpiando datos
df.info()

## probando 
df_clean_p1 = df[df['ap_lo'] <= df['ap_hi']]
df_clean_p1.shape

## probando otra cosa 
df_clean_p2 = df[df['ap_lo'] <= df['ap_hi']]
df_clean_p2 = df_clean_p2[df_clean_p2['height'] >= df_clean_p2['height'].quantile(0.025)]
df_clean_p2 = df_clean_p2[df_clean_p2['height'] <= df_clean_p2['height'].quantile(0.975)]
df_clean_p2 = df_clean_p2[df_clean_p2['weight'] >= df_clean_p2['weight'].quantile(0.025)]
df_clean_p2 = df_clean_p2[df_clean_p2['weight'] <= df_clean_p2['weight'].quantile(0.975)]


# probando una forma sacada de internet (este me da los valores correctos, no se por que?)
df_clean_p2 = \
    df[(df['ap_lo'] <= df['ap_hi']) & 
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))]


#grafico de correlacion
matriz_cor = df_clean_p2.corr() ; matriz_cor
sns.heatmap(matriz_cor)

np.ones_like(matriz_cor, dtype=bool)
triangulo_mask = np.triu(np.ones_like(matriz_cor, dtype=bool)); triangulo_mask

sns.heatmap(matriz_cor, annot = True, mask = triangulo_mask)

fig , ax = plt.subplots(figsize = (7,7))
sns.heatmap(matriz_cor, annot = True, fmt = '.1f', mask = triangulo_mask, square= True)