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