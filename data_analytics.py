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

uf = df.groupby(by="REGIAO")["VLRFATURADO"].sum().reset_index()
#Output sobre as variáveis
def variables_description(df):
    print('Variáveis da base de dados e seus tipos: \n')
    print(df.info(),"\n")
    

def analise_faturamento(uf):
    uf = uf.rename(columns={"VLRFATURADO": "VLRFATURADO_REGIAO"})
    print(uf,"\n")



def bar_graph_plot(x,y,title,uf):
    plt.rcParams["figure.figsize"] = (20,5)
    ax = uf.plot(kind='bar')
    ax.set_xticklabels(uf[x], minor=False)
    plt.title(title)
    plt.ylabel(y)
    plt.xlabel(x)
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x(), p.get_height() * 1.10))
    plt.tight_layout()
    plt.show()


def main():
    variables_description(df)
    analise_faturamento(uf)
    bar_graph_plot("REGIAO","VLRFATURADO","Valor faturado por região", uf)  #Grafico faturamento x regiao

main()