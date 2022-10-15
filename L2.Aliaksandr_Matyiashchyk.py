import psycopg2 as pg
import pandas as pd
from sqlalchemy import create_engine
db_string = "postgresql://wbauer_adb:adb2020@pgsql-196447.vipserv.org:5432/wbauer_adb"

db = create_engine(db_string)

connection_sqlalchemy = db.connect() #łączymy się przez sqlalchemy
#łączymy się przez psycopg2 i pandas
connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020')

#ZADANIE 1
df = pd.read_sql('select name from category',con=connection)
print(df.size)


#ZADANIE 2

df = pd.read_sql('select name from category order by name ASC',con=connection)
print(df)

#ZADANIE 3 
#Najmłodszy film do wypożyczenia
df = pd.read_sql('select min(release_year), film_id from film group by film_id order by  min(release_year) ',con=connection)
print(df)
# Najstarszy film do wypożyczenia
df = pd.read_sql('select max(release_year), film_id from film group by film_id order by  max(release_year) ',con=connection)
print(df)


#ZADANIE 4 robimy na sqlalchemy bo na pandas nie działa, ze względu na zera po znaku -

result_set = db.execute("select rental_date from rental where rental_date between '2005-07-01' and '2005-08-01'")
for r in result_set:  
    print(r)
# ZADANIE 5
result_set = db.execute("select rental_date from rental where rental_date between '2010-01-01' and '2011-02-01'")
for r in result_set:  
    print(r)
#ZADANIE 6

df = pd.read_sql('select  amount, payment_id from payment order by amount desc  limit 1',con=connection)
print(df)

#ZADANIE 8
df = pd.read_sql('SELECT  manager_staff_id, address_id, store_id  from store  union select staff_id, address_id, store_id from staff ',con=connection)
print(df ) 
#Widzimy, że id adresów pracowników to 1, 2 3 i 4, więc możemy ich odszukać w bazie danych address 
df = pd.read_sql('select address, city_id, district from address where address_id between 1 and 4 ',con=connection)
print(df)
#znając id city(300,576) możemy wyjśc na kraj 
df = pd.read_sql('select country_id, city_id from city where city_id in (300,576)',con=connection)
print(df)
#widzimy, że country id to 20 i 8, więc wyszukujemy. 
df = pd.read_sql('select country_id, country from country where country_id in (8,20)',con=connection)
print(df)
# #W wyniku widzimy, że pracowniki mieszkają w Australii i Canadzie. 

# ZADANIE 7

result_set = db.execute("SELECT country, country_id  from country where country = 'Poland' or  country = 'Nigeria'  ")  
for r in result_set:  
    print(r)
# Widzimy, że interesujące nas kraje znajdują się pod pozycją 69, 76

df = pd.read_sql('SELECT city_id, city, country_id  from city where country_id in (69,76)',con=connection)
print(df) 
#Mamy listę klientów, gdzie możemy odczytać wartosć 21
##########
#ZADANIE 9
result_set = db.execute("SELECT country, country_id  from country where country = 'Argentina' or  country = 'Spain'  ")  
for r in result_set:  
    print(r) 
#Znamy id tych krajów
df = pd.read_sql('SELECT city_id, city, country_id  from city where country_id in (6,87)',con=connection)
print(df) 
df = pd.read_sql('SELECT city.city, address, address_id from address INNER JOIN city ON city.city_id = address.city_id where country_id in (6,87) ', con=connection )  
print(df ) #widzimy, że mamy 18 adresów w tych krajach, lecz pasują te adresy co do adresów pracowników
df = pd.read_sql('SELECT address_id from staff union select address_id from store ', con=connection )  
print(df )
#ZADANIE 10
df = pd.read_sql('SELECT name  from category ', con=connection )  
print(df)
df = pd.read_sql('SELECT rental_id, rental_date, return_date from rental ', con=connection )  
print(df)




 