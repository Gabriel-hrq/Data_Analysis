import pandas as pd
import matplotlib.pyplot as plt
from pandas import read_excel
import numpy as np

from statsmodels.graphics.gofplots import qqplot

from scipy import stats as st

import researchpy as rs

from sklearn.preprocessing import StandardScaler

import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
pd.set_option('display.max_columns', None)

# In Terminal -> pip install pandas matplotlib numpy statsmodels scipy researchpy scikit-learn


df = pd.read_excel(r"C:/Users/User/Downloads/PEDIDOS_INDUSTRIA_TEXTIL_V1.xlsx", sheet_name="BASE")