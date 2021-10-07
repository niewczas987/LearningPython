#LICZBY
#dodawanie
a= 123+234
print(a)

#mnożenie
a=1.5*4
print(a)

#potegowanie
a=2**100
print(len(str(a))) #wypisz dlugosc ciagu znakow 2^100

#moduł math
import math
print(math.pi) #liczba pi
print(math.sqrt(9)) #pierwiastkowanie

#moduł random
import random
print(random.random()) #wypisanie losowej liczby
print(random.choice([1,2,3,4])) #wybierz losowa liczbe z tabeli choice

print('========================================================================')

#LANCUCHY ZNAKOW
S = 'Test'
print('Operacje na łańcuchu znaków: '+S)
print(len(S))   #dlugosc ciagu znakow S
print(S[0])     #pierwszy znak ciagu znakow S
print(S[-1])    #ostatni znak ciagu znakow S
print(S[-2])    #drugi od końca znak ciagu znakow S
print(S[1:3])   #wycinek S z indeksami 1 do 2, bez 3
print(S[1:])    #wszystko poza 1 znakiem
print(S+ 'xyz') #konkatenacja
print(S * 3)    #3-krotne powtorzenie

#niezmiennosc - wyrazenie pozostaje bez zmian, dopoki go nie nadpiszemy
print('Przed zmianą: '+S)
S = 'z' + S[1:]
print('Po zamianie pierwszej litery : '+S)
S='Test'

#metody specyficzne dla łańcucha znaków
#find - odnalezienie przesuniecia podlancucha (jezeli nie ma to zwraca -1)
print(S.find('es'))

#replace - zastąpienie podłańcucha inym
print(S.replace('es','XYZ'))

#podzielenie na ograniczniku - metoda split
line = 'aaa,bbbbb,cc,ddddd'
print(line)
print('Po metodize split: ')
print(line.split(','))

#isaplpha, isdigit, isalnum
print('IsAlpha: ' + str(line.isalpha()))
print('IsDigit: '+str(line.isdigit()))
print('IsAlNum: '+ str(line.isalnum()))

#rstrip - usuniecie bialych znakow
line = line+'\n'
print(line)
print('===============')
print(line.rstrip())
print('===============')

#formatowanie ciągu znaków
line = '%s %s kurwa świnia' % ('Arka','Gdynie')             #wyrażenie formatujące
print(line)
line = '{0} {1} gówno w wiadrze'.format('Górnik','Zabrze')  #metoda formatujaca
print(line)

#dopasowywanie wzorcow
import re
match = re.match('/(.*)/(.*)/(.*)','/usr/home/drwal')
print(match.groups())

print('========================================================================')

#LISTY
L= [ 123, ' Mielonka', 1.35]
#operacje na sekwencjach
print(len(L))
print(L[0])         #indeksowanie po pozycji
print(L+ [4,5,6])   #konkatenacja

#operacje specyficzne
L.append('QWE')     #dodanie obiektu na końcu listy
print(L)
L.pop(2)            #kurczenie się - usunięcie elementu ze środka listy **może być też del
M= ['bb','aa','cc']
M.sort()            #sortowanie rosnaco
print(M)
M.reverse()         #sortowanie malejaco
print(M)

#zagnieżdżanie - socketing
M = [[1,2,3],                   #macierz 3x3
     [4,5,6],
     [7,8,9]]
print(M[1])                     #zwraca 1 wiersz
print(M[1][2])                  #zwraca liczbę na miejscu 1,2 - pierwszy wiersz, druga kolumna
#listy składane
col2 = [row[1] for row in M]    #zwraca 1 kolumnę
print(col2)
print([row[1]+1 for row in M])  #dodanie +1 do każdego elementu w kolumnie 1
print([row[1] for row in M if row[1] %2 == 0])  #wypisanie elementów parzystych z kolumny 1
diag = [M[i][i] for i in [0,1,2]]               #wypisanie elementów z przekatnej macierzy M
print(diag)
doubles = [c*2 for c in 'test']                 #powtórzenie znaku w łańcuchu 'test'
print(doubles)
#generatory
G = (sum(row) for row in M)                     #generator sum wierszy
print(next(G))                                  #suma 0 wiersz
print(next(G))                                  #suma 1 wiersza
#map
print(list(map(sum,M)))                         #mapowanie sumy dla każdego z wierszy M
print({sum(row) for row in M})                  #utworzenie zbioru sum wierszy
print({i:sum(M[i]) for i in range(3)})          #utworzenie tabeli,klucz-wartosc sum wierszy

print([ord(x) for x in 'mielonka'])             #lista numerow porzadkowych znakow
print({ord(x) for x in 'mielonka'})             #zbiory usuwają duplikaty
print({x: ord(x) for x in 'mielonka'})          #klucze słownika sa unikalne

print('========================================================================')

#SLOWNIKI
#operacje na odwzorowaniach
D = {'jedzenie': 'Mielonka','ilość':4,'kolor':'czerwony'}       #utworzony słownik
print(D)
print(D['jedzenie'])                                            #pobranie wartości kluczea 'jedzenie'
D['ilość'] +=1                                                  #dodanie 1 do wartosci klucza 'ilosć'
print(D)

D1={}                                                           #utworzenie pustego słoenika
D1['imie'] = 'Robert'                                           #tworzenie kluczy przez przypisanie
D1['zawód'] = 'Programista'
D1['wiek'] = 45
print(D1)

#zagnieżdżanie - socketing
rec = { 'dane osobowe': {'imie':'Robert','nazwisko':'Kowalski'},
        'zawod': ['programista', 'inzynier'],
        'wiek': 34.5}
print(rec['dane osobowe'])              #zagniezdzony slownik
print(rec['dane osobowe']['nazwisko'])  #indeksowanie zagniezdzonego slownika
print(rec['zawod'])                     #zagniezdzona lista
print(rec['zawod'][-1])                 #indeksowanie zagniezdzonej listy
rec['zawod'].append('lesniczy')         #rozszerzenie listy zawodow
print(rec['zawod'])

rec=0                                   #czyszczenie pamieci ze sownika
print(rec)


#sortowanie kluczy - petla FOR
D = {'a':1,'c':3,'b':2}
Ks = list(D.keys())
print(Ks)
Ks.sort()
print(Ks)

for key in Ks:                          #iteracja przez posortowane klucze
    print(key, '=>', D[key])

#instrukcja sorted
for key in sorted(D):                   #to samo z instrukcj sorted
    print(key, '=>', D[key])

for c in 'mielonka':
    print(c.upper())
#petla while
x=4
while x>0:
    print('ok'*x)
    x -=1

#obliczanie kwadratu z listy liczb
squares = [x**2 for x in [1,2,3,4,5]]
print(squares)
#to samo w petli for
squares =[]
for x in [1,2,3,4,5]:
    squares.append(x**2)

print(squares)

#testoawanie za pomoc if
D= {'a':1,'b':2,'c':3}
D['e'] = 99
print('f' in D)                         #sprawdzenie, czy jest klucz o nazwie 'f' w slowniku 'D'

if not 'f' in D:                        #insstrukcja warunkowa if
    print('Nie ma')

value = D.get('x',0)                    #indeks z wartoscia domyslna
print(value)
value = D['x'] if 'x' in D else 0       # forma wyrazenia if/else
print(value)


#KROTKI (eng. TUPLES)
T = (1,2,3,4)               #krotka z 4 elementami
print(len(T))
T= T + (5,6)                   #konkatenacja
print(T)
print(T[0])                    #indeksowanie
print(T.index(4))
print(T.count(4))              #ilosc pojawien sie liczby 4

#PLIKI
f = open('data.txt', 'w')        #utworzenie nowego pliku w trybie do zapisu
f.write('Czesc!\n')             #zapisanie lancucha znakow do pliku
f.write('xD\n')
f.close()                       #zamkniecie pliku i wyczyszczenie bufora

f=open('data.txt')              #bez 'r', bo read jest domyslnym typem przetwarzania
text = f.read()
print(text)
print(text.split())

#ZBIORY (eng. CLUSTERS)
X = set('mielonka')
Y = {'s','z','y','n','k','a'}

print(X,Y)
print(X & Y)    #czesc wspolna zbiorow
print(X | Y)    #suma zbiorow
print(X - Y)    #roznica zbiorow

# LICZBY ZMIENNOPRZECINKOWE - FLOATS
print(1 / 3)
print((2 / 3) + (1 / 2))
import decimal

d = decimal.Decimal('3.141')
print(d + 1)
decimal.getcontext().prec = 2
print(decimal.Decimal(1.00)/decimal.Decimal(3.00))
#ulamki
from fractions import Fraction
f = Fraction(2,3)
print(f+1)

#BOOL
x = 1>2
print(x)


#TYPES - sprawdzanie elastycznosci kodu
L= [ 123, ' Mielonka', 1.35]
print(type(L))
if type(L) == type([]):
    print('yes')

if type(L) ==list:  #uzycie nazwy typu
    print('yes')

if isinstance(L, list): #sprawdzanie zorientowania obiektow
    print('yes')