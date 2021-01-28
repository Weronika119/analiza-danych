# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 22:16:56 2021

@author: HP
"""

#1.Importowanie paczek pythonowych  

  

import pandas as pd  

import numpy as np  

import matplotlib.pyplot as plt  

import seaborn as sns  

import scipy.stats as st  

import os  

  

  

#Styl wykresów  

sns.set_style('whitegrid')  

  

   

#2.Wczytanie pliku danych  

os.getcwd()  

os.listdir()  

os.chdir("C:/Users/HP/Desktop/AWD") 

   

  

plik = 'bestsellers.csv' 

dane = pd.read_csv(plik)  

  

   

#3.Czyszczenie danych  

dane.isnull().sum() #brak brakujących wartosci  

  

   

#3.1.Nieprawidłowosci w danych  

#3.1.1.W 2 miejscach zle napisano inicjaly autora - jest przerwa pomiedzy literami w J.K.Rowling  

dane.loc[dane.Author == 'J. K. Rowling', 'Author'] = 'J.K. Rowling'  

  

#3.1.2 Zmiana nazw kolumn na polskie  

dane.columns = ['Tytuł','Autor','Ocena', 'Liczba opinii', 'Cena', 'Rok', 'Gatunek']  

   

#5.Opisy zmiennych  

#5.1.Tytuł  

tytul = 'Tytuł'  

dane[tytul].describe() #informacje o tytułach  

  

  

ranking_tyt = dane.groupby(['Tytuł', 'Autor', 'Gatunek'], as_index=False)[['Ocena', 'Liczba opinii']].mean()  

ranking_tyt = ranking_tyt[ranking_tyt['Liczba opinii']>3000]  

ranking_tyt = ranking_tyt.sort_values('Ocena', ascending=False).head(20)  

print(ranking_tyt) 

  

#Wykres do najczesciej wystepujacych tytułów  

tytuly = dane['Tytuł']  

pos_nazwy = tytuly.value_counts()  

najcz_nazwy = pos_nazwy.iloc[:18]  

y = najcz_nazwy  

dane2 = y.reset_index()  

dane2.plot(rot=90)  

plt.bar(dane2.index, y)  

plt.xticks(range(len(y)), pos_nazwy.index)  

plt.yticks(range(0,13))  

plt.ylabel('Liczba wystąpień')  

plt.xlabel('Tytuły')  

plt.legend('')  

  

  

#5.2.Autor  

autor = 'Autor'  

dane[autor].describe() #informacje o autorach  

  

#Wykres do najczesciej występujących autorów  

autorzy = dane['Autor']  

pos_autorzy = autorzy.value_counts()  

najcz_autorzy = pos_autorzy.iloc[:13]  

x = najcz_autorzy  

dane1 = x.reset_index()  

dane1.plot(rot=90)  

plt.bar(dane1.index, x)  

plt.xticks(range(len(x)), pos_autorzy.index)  

plt.yticks(range(0,15))  

plt.ylabel('Liczba wystąpień')  

plt.xlabel('Autorzy')  

plt.legend('')  

plt.show()  

  

   

#5.3.Ocena  

ocena = 'Ocena'  

print(dane[ocena].describe())  

print(dane[ocena].median())  

print(dane[ocena].mode())  

  

#Histogram zmiennej ocena 

plt.hist(dane[ocena])  

plt.xlabel('Ocena')  

plt.ylabel('Częstosć')  

plt.show()  

  

   

#5.4.Liczba opinii  

opinie = 'Liczba opinii'  

print(dane[opinie].describe())  

print(dane[opinie].median())  

print(dane[opinie].mode())  

  

#Histogram zmiennej liczba opinii 

plt.hist(dane[opinie])  

plt.xlabel('Liczba opinii')  

plt.ylabel('Częstosć')  

plt.show()  

   

  

#5.5.Cena  

#opis zmiennej cena  

dane['Cena'].mean()  

dane['Cena'].median()  

dane['Cena'].mode()  

dane['Cena'].std()  

dane['Cena'].max()  

dane['Cena'].min()  

dane['Cena'].quantile(0.25)  

dane['Cena'].quantile(0.75)  

  

#wykres pudełkowy dla zmiennej 'Cena'  

plt.boxplot(dane['Cena']) 

plt.ylabel('Cena [$]') 

plt.savefig('wykres pudełkowy dla ceny') 

plt.show() 

  

#5.6.Rok  

dane = dane.sort_values(by = 'Rok', ascending = True)  

print(dane.Rok)  

   

  

#5.7.Gatunek  

gatunek = 'Gatunek'  

dane[gatunek].describe()  

  

#wykres 

labels= ['literatura faktu', 'beletrystyka'] 

plt.figure(figsize =(6, 6))  

plt.pie(dane[gatunek].value_counts(), labels=labels,  autopct='%1.1f%%') 

plt.show() 

  

   

  

#6.Badanie związków między zmiennymi;   

#6.1.Czy występuje różnica między średnią ceną książek beletrystki i książek literatury faktu w latach 2009-2019?   

  

beletrystyka = dane[dane.Gatunek == 'Fiction']  

literatura_faktu = dane[dane.Gatunek == 'Non Fiction']  

  

#korelacja 

st.ttest_ind(beletrystyka['Cena'], literatura_faktu['Cena'])  

srednia_1 = beletrystyka['Cena'].mean()  

srednia_2 = literatura_faktu['Cena'].mean()  

  

#wykres 

x = ['srednia_1', 'srednia_2']  

y = [beletrystyka['Cena'].mean(), literatura_faktu['Cena'].mean()]  

podpisy =['Beletrystyka', 'Literatura faktu']  

plt.bar(x,y, color = 'g')  

plt.xticks(x, podpisy)  

plt.xlabel('Gatunek')  

plt.ylabel('Średnia cena[$]')  

plt.show()  

  

  

#6.2.Czy jest różnica w ocenach książek literatury faktu i beletrystyki?   

#wykres  

plt.figure()  

sns.countplot(x='Gatunek', data=dane, hue='Ocena')  

plt.legend (title="Ocena", bbox_to_anchor=(1.2, 1.0))   

plt.xlabel('Gatunek')  

plt.ylabel('Liczba wystąpień')  

plt.show()  

  

#tabelka  

print(dane.groupby('Gatunek')[['Ocena']].mean())  

  

#korelacja  

print(st.ttest_ind(beletrystyka['Ocena'],literatura_faktu['Ocena']))  

  

   

#6.3.Czy istnieje zależność między ceną książki a liczbą opinii?   

#korelacja 

st.spearmanr(dane['Cena'], dane['Liczba opinii'])  

  

#wykres 

plt.scatter(dane['Cena'], dane['Liczba opinii'], c='black', alpha=0.3, s=30)  

plt.xlabel('Cena[$]')  

plt.ylabel('Liczba opinii')   

plt.show()  

  

   

#6.4.Czy istnieje zależność między ceną książki, a oceną czytelników?   

#wykres 

plt.scatter(dane['Cena'],dane['Ocena'], c='black', alpha=0.3, s=30)  

plt.xlabel('Cena[$]')  

plt.ylabel('Oceny czytelników')  

plt.show()  

  

#korelacja  

print(st.pearsonr(dane['Cena'],dane['Ocena']))  

   

  

#6.5.Czy średnia liczba opinii zmieniała się na przestrzeni lat?   

#korelacja 

st.spearmanr(dane['Rok'], dane['Liczba opinii'])  

  

#dane do tabeli  

dane.groupby('Rok')['Liczba opinii'].mean()  

  

  

#6.6.Czy średnia ocena czytelników zmieniała się na przestrzeni lat?  

#korelacja 

st.spearmanr(dane.Rok, dane.Ocena)  

  

#dane do tabeli  

dane.groupby('Rok')['Ocena'].mean() 

 

#6.7.Czy istnieje związek między całkowitą liczbą recenzji autora a średnią oceną tego autora przez użytkowników? 

x=dane.groupby('Autor')['Liczba opinii'].sum() 

x.max() #największa ilosc recenzji 

y=dane.groupby('Autor')['Ocena'].mean() 

plt.scatter(x,y) 

plt.xticks(range(0,280001,40000)) 

plt.xlabel('Ilość recenzji') 

plt.ylabel('Ocena') 

plt.show() 

 

#korelacja 

st.spearmanr(dane['Liczba opinii'], dane['Ocena']) 


 