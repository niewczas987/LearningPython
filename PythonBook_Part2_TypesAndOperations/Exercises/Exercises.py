#Exercise1
print('EX1')
print(2**16)    #potegowanie
print(2/5,2/5.0)    #zwrócona krotka - format float = 0.4 0.4
print('mielonka' +'jajka')  #konkatenacja = mielonkajajka
S='szynka'
print('jajka' + S)  #konkatenacja = jajkaszynka
print(S*5)  #powtorzenie = szynkaszynkaszynkaszynkaszynka
print(S[:-1])    #wycinek - w tym przypadku zwraca string bez ostatniego znaku
print('zielone %s i %s'%('jajka',S)) #wstawianie tekstu do stringa = zielone jajka i szynka
print('zielone {0} i {1}'.format('jajka',S)) #to samo z użyciem funkcji 'format'
print(('x',)[0])      #zwrócenie znaku z 0 indeksem z krotki =x
print(('x','y')[1])   #zwrócenie znaku z 1 indeksem krotki =y
L= [1,2,3] + [4,5,6] #konkatenacja listy
print(L)    #wyswietl liste
print(L[:]) #skopiuj liste
print(L[:0])    #pusta lista
print(L[-2]) #wyswietl element z indeksem -2
print(L[-2:])   #wyswietla 2 ostatnie elementy
print(([1,2,3]+[4,5,6])[2:4]) #wyswietlenie wycinka znakow z 2 i 3 indeksem z utworzonej listy = [3, 4]
print([L[2],L[3]])  #utworzenie listy zawierającej elementy z indeksem 2 i 3 z listy l
L.reverse()         #odwrocenie listy L
print(L)
L.sort()            #posortowanie rosnaco listy L
print(L)
print(L.index(4))   #wyswietlenie indeksu rekordu '4'
print({'a':1,'b':2}['b'])   #wyswietlenie ze słownika rekordu o kluczu 'b'
D={'x':1,'y':2,'z':3}   #utworzenie słownika D
D['w'] = 0  #dodanie do slownika rekordku o kluczu 'w'
print(D['x']+D['w'])    #suma wartości z kluczy 'x' i 'w'
D[(1,2,3)] = 4      #dodanei do slownika D, kluicza (1,2,3) z wartością '4'
print(D)
print(list(D.keys()), list(D.values()),(1,2,3) in D) #wypisanie krotki z: kluczami słownika D, wartosciami słownika D, spwardzeniem, czy klucz(1,2,3) znajduje sie w D
print(([[]],[""],[],(),{}))
#utworzenie krotki zawierajacej:
# liste, zawierajaca w sobie liste na indeksie [0],
# liste 1 elementowa ze stringiem,pusta liste,
# pustą krotkę, pusty słownik

print('='*20)
print('EX2')
#Exercise2
#zdefiniowanie listy
L = [0,1,2,3]
#a) jeżeli indeks będzie poza granicą listy kompilator zwrci błąd
#print(L[4]) -> IndexError: list index out of range

#b)wycinek poza dlugosc listy
print(L[-1000:100]) #zwraca wszystko co jest w podanym zakresie, czyli całą listę

#c)wycinek w odwrotnej kolejnosci
print(L[3:1]) #zwracapustą listę
L[3:1] = '?'    #wstawia na indeks 3, wartrosc '?'
print(L)


print('='*20)
print('EX3')
#Exercise3
#zdefiniowanie listy
L = [0,1,2,3]
L[2] = []   #zastapienie wartosci indeksu 2 wartoscia pustej listy []
print(L)
L[2:3] = [] #usuniecie elementu popzez wstawienie pustej listy na wycinek
print(L)
del L[0] #usuniecie elementu o indeksie 0
print(L)
del L[1:]   #usuniecie wszystkiego poza elmenetem z indeksem 0
print(L)
L=[0,1,2,3]
# L[1:2] = 1
# print(L)
#zwrocony jest blad - TypeError: can only assign an iterable


print('='*20)
print('EX4')
#Exercise4
X = 'mielonka'
Y = 'jajka'
#print((X,Y) = (Y,X)) - SyntaxError: expression cannot contain assignment


print('='*20)
print('EX5')
#Exercise5
D={}
D[1]='a'
D[2]='b'
print(D)
D[(1,2,3)] = 'c'
print(D)
#słowniki należą do typów zmiennych, więc nie ma dla nic znaczenia jaka jest wartosć klucza o ile jest
#on unikatowy


print('='*20)
print('EX6')
#Exercise6
D = dict(a=1,b=2,c=3)   #utworzenie słownika
print(D)
#print(D['d'])   #indeksowanie dla nieistniejacego klucza -> KeyError: 'd'
D['d'] = 'mielonka'
print(D)    #{'a': 1, 'b': 2, 'c': 3, 'd': 'mielonka'}


print('='*20)
print('EX7')
#Exercise7
# a)wykorzystasnie '+' na róznych typach
#print('1,2,3'+[4,5,6])  -> TypeError: can only concatenate str (not "list") to str
#print([1,2,3]+(4,5,6))   -> TypeError: can only concatenate list (not "tuple") to list

# b) czy plus zadziała jeśli jeden z argumentow jest slownikiem ->NIE
# print({'a':1}+(1,2,3))
# print({'a':1}+[1,2,3])

# c) metoda 'append' działa jedynie dla list
# print('123'.append('10'))
print([1,2,3].append('qwe'))
# d) dokonujac konkatenacji dwoch lancuhcow znakow otrzymamy lancuch znakow, to samo z lista lista+lista=lista

print('='*20)
print('EX8')
#Exercise8
S = 'jajo'*4
print(S)
print(S[0][0][0][0][0])
S1=list['j','a','j','o']
print(S1)
#print(S1[0][0][0][0][0]) - TypeError: There are no type variables left in list['j', 'a', 'j', 'o']

print('='*20)
print('EX9')
#Exercise9
S='jajo'
print(S)
print(S[:3]+'a')
