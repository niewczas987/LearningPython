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