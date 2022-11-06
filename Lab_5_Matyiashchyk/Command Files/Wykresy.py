import psycopg2 as pg
import pandas as pd
import numpy as np 

from pandas.io.excel import ExcelWriter

import matplotlib.pyplot as plt






df=pd.read_csv("D:\\Education\\3 rok AGH\\5 Semestr\\AiBD\\pandas_project\\lab_5_Matyiashchyk\\Analysis Data\\billboard.csv",encoding='unicode_escape',na_values='nie ma danych', dtype = 'str')
# print(df.isnull().sum())
# df.fillna(0)

for x3 in range(0, len(df), 10):
    df[x3:x3+10].plot.bar(figsize=(10,10))
    plt.show()
