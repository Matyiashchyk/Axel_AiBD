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


# print(df.iloc[:, x1:x])

 
# Przywitanie 
print("WELCOME TO A SIMPLE MENSURATION PROGRAM") 
 
# Menuy 
while True: 
    print("\nMAIN MENU") 
    print("1. Wyszukaj według nazwy tworu ") 
    print("2. Wyszukaj według numeru tygodnia") 
    print("3. Wyszukaj według nazwy artystu") 
    print("4. Exit") 
    choice1 = int(input("Enter the Choice:")) 
 
    if choice1 == 1: 

     txt = input("Wprowadz nazwę albo co pamiętasz z nazwy tworu")
     df1 = df[df['track'].str.contains(txt)] #Odpowiada za wyszukiwanie według nazwy tworu
     print('\n'.join(df1)) #wyświetlanie
     df1.to_csv( "D:\\Education\\3 rok AGH\\5 Semestr\\AiBD\\pandas_project\\lab_5_Matyiashchyk\\Analysis Data\\nowu.csv", sep='|')

    if choice1 == 2: 
        x1 = input("wprowadż tydzień, który chciałbyś odczytać ")
        x1 = int(x1)
        y = x1 +6
        df2 = df.iloc[:, [1,2,3,4,5,6,y]] #Odpowiada za wyszukiwanie według numeru tygodnia
        print(df2)
        df2.to_csv( "D:\\Education\\3 rok AGH\\5 Semestr\\AiBD\\pandas_project\\lab_5_Matyiashchyk\\Analysis Data\\nowu.csv", sep='|')

    if choice1 == 3: 

     txt = input("Wprowadz nazwę albo co pamiętasz z nazwy grupy bądz śpiewacza")
     df3 = df[df['artist.inverted'].str.contains(txt)] #Odpowiada za wyszukiwanie według nazwy artystu
     print('n'.join(df3))
     df3.to_csv( "D:\\Education\\3 rok AGH\\5 Semestr\\AiBD\\pandas_project\\lab_5_Matyiashchyk\\Analysis Data\\nowu.csv", sep='|')

    if choice1 == 4:
        break
    











































































# x1 = input("Введите свое счастливое число: ")

# try:
#     x1 = int(x1)
#     print("Это правильный ввод! Ваше счастливое число: ", x1)
# except ValueError:
#     print("Это не правильный ввод. Это не число вообще! Это строка, попробуйте еще раз.")
# x = input("Введите свое счастливое число: ")

# try:
#     x = int(x)
#     print("Это правильный ввод! Ваше счастливое число: ", x)
# except ValueError:
#     print("Это не правильный ввод. Это не число вообще! Это строка, попробуйте еще раз.")

# print(df.iloc[:, x1:x])




