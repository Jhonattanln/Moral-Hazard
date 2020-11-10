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

serieI = pd.concat([macroQ, popQ['POSITIVA']], axis=1).dropna()
serieI

#### Linear regression

def reg (X, Y):
    X = sm.add_constant(X)
    model = regression.linear_model.OLS(Y, X).fit()
    return model.summary()

reg(serieI['Dívida/PIB - %'], serieI['POSITIVA'])


plt.style.use('ggplot')
sns.regplot(data=serieI, 
            x='Dívida/PIB - %',
            y='POSITIVA')
plt.ylabel('Avaliação positiva')
plt.show()