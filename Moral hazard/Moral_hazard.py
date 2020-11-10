import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels import regression

#### Importing data

macro = pd.read_excel(r'Macroecomics indicators.xlsx', parse_dates=True, index_col=0)
pop = pd.read_excel(r'Popularity.xlsx', parse_dates=True, index_col='DATA')

