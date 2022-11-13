import psycopg2 as pg
import pandas as pd
import numpy as np 

from pandas.io.excel import ExcelWriter

import matplotlib.pyplot as plt

df=pd.read_csv("D:\\Education\\3 rok AGH\\5 Semestr\\AiBD\\pandas_project\\lab_6_Matyiashchyk\\Analysis Data\\8_PODKARPACKIE.csv")



df.dropna(subset=['Wiek kupującego'], inplace=True)
df.to_csv( "D:\\Education\\3 rok AGH\\5 Semestr\\AiBD\\pandas_project\\lab_6_Matyiashchyk\\Analysis Data\\8_PODKARPACKIE_modyfikowane.csv")
df2=pd.read_csv("D:\\Education\\3 rok AGH\\5 Semestr\\AiBD\\pandas_project\\lab_6_Matyiashchyk\\Analysis Data\\8_PODKARPACKIE_modyfikowane.csv")
print(df2.describe(include='all'))

print (df2)
###### Wykres pokazujący podział kobiet męźczyzn i ich wiek
ax = df2.plot.hist(column=["Wiek kupującego"], by="Płeć kupującego", figsize=(10,10 ), stacked=True, title = 'Pokazanie ilość kupujących ze względy na plec' , bins = 25)
ax[0].set_xlabel('Wiek kupującego')  
ax[0].set_ylabel('Częstósć Występowania w columnie')
ax[0].set_title('Woomen')
ax[1].set_xlabel('Wiek kupującego')
ax[1].set_ylabel('Częstósć Występowania w columnie')
ax[1].set_title('Man')
ax[2].set_xlabel('Wiek kupującego')
ax[2].set_ylabel('Częstósć Występowania w columnie')
ax[2].set_title('Brak danych')
plt.subplots_adjust(hspace=1)
############## Wykres ocen dla każdej Marki
ax1 = df2.plot.hist(column=["Ocena"], by="Marka", figsize=(10,10 ), stacked=True, bins = 20)
plt.subplots_adjust(hspace=1)
ax1[0].set_xlabel('Ocena')  
ax1[0].set_ylabel('Częstósć')
ax1[1].set_xlabel('Ocena')  
ax1[1].set_ylabel('Częstósć')
ax1[2].set_xlabel('Ocena')  
ax1[2].set_ylabel('Częstósć')
ax1[3].set_xlabel('Ocena')  
ax1[3].set_ylabel('Częstósć')
ax1[4].set_xlabel('Ocena')  
ax1[4].set_ylabel('Częstósć')
ax1[0].set_title('Oceny dla Beko')
ax1[1].set_title('Oceny dla Dyson')
ax1[2].set_title('Oceny dla Electrolux')
ax1[3].set_title('Oceny dla Samsung')
ax1[4].set_title('Oceny dla Tefal ')

####### Wykres Dni od zakpupu do sumy ocen 
dni_ocena = df2.groupby('Dni od zakupu').agg({'Ocena':'sum'})
dni_ocena.plot(y = 'Ocena', kind='bar', title = 'Pokazanie sumy ocen w poszczególnych dniach od momentu zakupu', xlabel = 'Dni od zakupu', ylabel = 'Ocena')
###### Wykres dla zmiennej "Wiek kupującego"
bins = np.arange(0,100,5)
ax2 = df2.plot.hist(column=["Wiek kupującego"], figsize = (8,8), bins = bins + 1, width = 4)
ax2.set_xlabel('Wiek kupującego')  
ax2.set_ylabel('Częstósć Występowania w columnie')
ax2.set_title('Pokazanie ilości ludzi w poszczegółnym wieku')
#######  Wykres dla zmiennej "Dni od zakupu"
bins = np.arange(0,19,1)
ax3 = df2.plot.hist(column=["Dni od zakupu"], figsize = (8,8), bins = bins + 1, width = 0.8)
ax3.set_xlabel('Dni od Zakupu')    
ax3.set_ylabel('Częstósć Występowania w columnie')
ax3.set_title('Wykres dla zmiennej "Dni od zakupu" ')
plt.xticks(bins)
##########   Wykres dla zmiennej "Ocena"
bins1 = np.arange(0,5.5,0.5)
ax3 = df2.plot.hist(column=["Ocena"], figsize = (8,8), bins = bins1 + 1, width = 0.4)
ax3.set_xlabel('Ocena')  
ax3.set_ylabel('Częstósć Występowania w columnie')
ax3.set_title('Wykres dla zmiennej "Ocena"')
plt.xticks(bins1)
plt.subplots_adjust(hspace=1)
########### Wykres słupkowy dla płecu od oceny 
dni_ocena = df2.groupby('Płeć kupującego').agg({'Ocena':'mean'})
dni_ocena.plot(y = 'Ocena', kind='bar', title = 'Pokazanie średniej ocen dla każdego z płeców', xlabel = 'Płęć kupującego', ylabel = 'Ocena')
plt.legend()
plt.show()



# mark_ocena = df2.groupby('Marka').agg({'Ocena':'sum'})
# mark_ocena.plot(kind='bar', cmap='Accent', title = 'Pokazanie ocen w poszczególnych marok', figsize = (10,10))