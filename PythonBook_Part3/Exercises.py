#Ex1
#a) napisać petle wypisujaca znak ASCII dla każdego znaku łańucha S
print('1a')
S='abcdefghijkl'
res = []
for c in S:
    res.append(ord(c))
print(res)
#b)zmodyfikować pętlę by wyświetlałą sumę kodów łańcucha
print('1b')
S='abcdefghijkl'
res = 0
for c in S:
    res += ord(c)
print(res)
#c) - zrobione w a
print('1c')
print(list(map(ord, S)))

#Ex2
#do psrawdzenia jedna instrukcja, która powinna wykonywać piszczenie-> ASCII BELL
# for i in range(50):
#     print('Witaj%d\n\a' %i)

#Ex3
#Wypisać posortowany słownik
D = dict(a=1,b=2,x=3,c=0,y=5,z=7)
print(D)
listOfKeys = [key for key in D]
print(listOfKeys)
listOfKeys.sort()
for value in listOfKeys:
    print(value, '->', D[value])
#inna metoda
print(sorted(D.items()))

#Ex4
print('Przykład')
L=[1,2,48,16,32,64]
X=5
found = False
i=0
while not found and i<len(L):
    if 2**(X) ==L[i]:
        found =True
    else:
        i=i+1
if found:
    print('pod indeksem',i)
else:
    print(5,'nie odnaleziono')
#a) przepisać kod z użyciem częsci else pętli while
print('4a')
L=[1,2,48,16,32,64]
X=5
found = False
i=0
while i<len(L):
    if 2**(X) == L[i]:
        found = True
        print('pod indeksem', i)
        break
    else:
        i=i+1
else:
    print(5,'nie odnaleziono')
#b)wyrzucić logikę indeksującą liste przy użyciu pętli for
print('4b')
L=[1,2,48,16,32,64]
X=5
for i in L:
    if 2**(X) == i:
        found = True
        print('pod indeksem', L.index(2**X))
        break
else:
    print(5,'nie odnaleziono')
#c) usunac pętlę for na rzecz wyrazenia 'in'
print('4c')
L=[1,2,48,16,32,64]
X=5
if 2**(X) in L:
    print('pod indeksem', L.index(2**X))
else:
    print(5,'nie odnaleziono')
#d)przy użyciu 'for' oraz 'apend' wygenerować listy potęg 2
print('4d')
L=[]
for x in range(6):
    L.append(2**x)
print(L)

#f)ine podejście z użyciem lambda
print(list(map(lambda x: 2**x, range(6))))