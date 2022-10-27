import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple
from sqlalchemy import create_engine
db_string = "postgresql://wbauer_adb:adb2020@pgsql-196447.vipserv.org:5432/wbauer_adb"
db = create_engine(db_string)

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020')

def film_in_category(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str, dokładnie taki jak podana wartość
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''

    if isinstance(category, int):
        request = f"""select f.title, l.name as languge, c.name as category
                    from film f
                    join language l on l.language_id = f.language_id
                    join film_category fc on fc.film_id = f.film_id
                    join category c on c.category_id = fc.category_id
                    where c.category_id = {category}
                    order by f.title, languge"""
    elif isinstance(category, str):
        request = f"""select f.title, l.name as languge, c.name as category
                        from film f
                        join language l on l.language_id = f.language_id
                        join film_category fc on fc.film_id = f.film_id
                        join category c on c.category_id = fc.category_id
                        where c.name like '{category}'
                        order by f.title, languge"""
    else:
        return None

    return pd.read_sql_query(request, con=connection)

    
def film_in_category_case_insensitive(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''

    if isinstance(category, int):
        request = f"""select f.title, l.name as languge, c.name as category
                    from film f
                    join language l on l.language_id = f.language_id
                    join film_category fc on fc.film_id = f.film_id
                    join category c on c.category_id = fc.category_id
                    where c.category_id = {category}
                    order by f.title, languge"""
    elif isinstance(category, str):
        request = f"""select f.title, l.name as languge, c.name as category
                        from film f
                        join language l on l.language_id = f.language_id
                        join film_category fc on fc.film_id = f.film_id
                        join category c on c.category_id = fc.category_id
                        where c.name ilike '{category}'
                        order by f.title, languge"""
    else:
        return None

    return pd.read_sql_query(request, con=connection)
    
def film_cast(title:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o obsadę filmu o dokładnie zadanym tytule.
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |
    |0	|Greg       |Chaplin    | 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    title (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''

    if not isinstance(title, str):
        return None

    request = f"""select a.first_name, a.last_name
                from actor a
                join film_actor fa on fa.actor_id = a.actor_id
                join film f on f.film_id = fa.film_id
                where f.title like '{title}'
                order by a.last_name, a.first_name"""

    return pd.read_sql_query(request, con=connection)
    

def film_title_case_insensitive(words:list) :
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuły filmów zawierających conajmniej jedno z podanych słów z listy words.
    Przykład wynikowej tabeli:
    |   |title              |
    |0	|Crystal Breaking 	| 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.

    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    words(list): wartość minimalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''

    if not isinstance(words, list):
        return None

    words_str = '|'.join(words)
    request = f"""select title
                from film
                where title ~* '(?:^| )({words_str})""" + """{1,}(?:$| )'
                order by title"""

    return pd.read_sql_query(request, con=connection)
    #Zadanie 1.
df = pd.read_sql("select country FROM country where country like 'P%' ",con=connection)
print(df)
    #Zadanie 2.
df = pd.read_sql("select country FROM country where country like \'P%s\' ",con=connection)
print(df)
    #Zadanie 3.
df = pd.read_sql("select title FROM film where title like \'1:9\' ",con=connection)
print(df)
    #Zadanie 4.
df = pd.read_sql('select first_name, last_name FROM staff where first_name like \'%-%\'  ',con=connection)
print(df)
    #Zadanie 5.
df = pd.read_sql('select first_name, last_name FROM actor where first_name like \'P____\' or first_name like \'C____\'   ',con=connection)
print(df)
    #Zadanie 6.
df = pd.read_sql("select title FROM film where title like \'%Trip%\' union select title FROM film where title like \'%Alone%\' ",con=connection)
print(df)
    #Zadanie 7.
df = pd.read_sql("select first_name FROM actor where first_name ~'^Al[a:z, 1:9]*'  ",con=connection)
print(df)
#Wydaje imiona aktorów, ktrórzy mają imię rozpoczynające się na "Al" zawierające znaki od a do z i cyfry od 1 do 9, wielkość liter ma znaczenie
df = pd.read_sql("select first_name FROM actor where first_name ~*'^al[a:z, 1:9]*'  ",con=connection)
print(df)
#Wydaje imiona aktorów, ktrórzy mają imię rozpoczynające się na "Al" zawierające znaki od a do z i cyfry od 1 do 9, wielkość liter nie ma znaczenie




