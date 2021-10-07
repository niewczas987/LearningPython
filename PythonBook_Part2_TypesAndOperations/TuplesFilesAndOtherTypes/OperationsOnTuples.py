#podstawowe operacje
a=(1,2)
b=(3,4)
print(a+b)  #konkatenacja
print(a*4)  #powtorzenie
T=(1,2,3,4,5,6)
print(T[0]) #indeksowanie
print(T[1:3])   #wycinek

#sortowanie
T=('cc','aa','bb','dd')
tmp = list(T)
tmp.sort()
print(tmp)  #['aa', 'bb', 'cc', 'dd']
T=tuple(tmp)
print(T)
print(sorted(T))    #['aa', 'bb', 'cc', 'dd']
T=(1,2,3,2,3,4,5,2)
print(T.index(2))   #indeks pierwszego wystapienia wartosci '2'
print(T.count(2))   #zwraca ilosc wystapien wyrazenia '2'