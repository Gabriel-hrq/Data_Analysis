import pandas as pd
import matplotlib.pyplot as plt
from pandas import read_excel
import numpy as np

from statsmodels.graphics.gofplots import qqplot

from scipy import stats as st

import researchpy as rs

from sklearn.preprocessing import StandardScaler

import locale

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    print("Locale 'pt_BR.UTF-8' is not available on your system.")

pd.set_option('display.max_columns', None)

print("All libraries are imported successfully!")
