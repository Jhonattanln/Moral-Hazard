import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels import regression

#### Importing data

macro = pd.read_excel(r'Macroecomics indicators.xlsx', parse_dates=True, index_col=0)
pop = pd.read_excel(r'Popularity.xlsx', parse_dates=True, index_col='DATA')

#### Manipulating time series

macroQ = macro.asfreq('Q', method='ffill')
popQ = pop.asfreq('Q', method='ffill')
macroQ

serieI = pd.concat([macroQ, popQ], axis=1).dropna()
serieI.columns

#### Linear regression

def reg (X, Y):
    X = sm.add_constant(X)
    model = regression.linear_model.OLS(Y, X).fit()
    return model.summary()

reg(serieI['POSITIVA'], serieI['Desemprego - %'])

#### Graphics 

plt.style.use('ggplot')
sns.regplot(data=serieI, 
            x='POSITIVA',
            y='Desemprego - %')
plt.ylabel('Avaliação positiva')
plt.xlabel('Desemprego - % da população')
plt.show()

#### Others graphics

macro.plot(subplots=True)
plt.show()


pop.groupby('PRESIDENTE').plot(subplots=True)
plt.show()

