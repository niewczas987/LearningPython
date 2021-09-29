#podstawowe zastosowanie - iteracja po sekwencjach
for x in ['mielonka','jajka','szynka']:
    print(x,end=' ')

sum =0
for x in [1,2,3,4]:
    sum += x
print(sum)

prod =1
for item in [1,2,3,4]: prod*= item
print(prod)

S='drwal'
T = ('i','jest','git')

for x in S:print(x, end=' ')
for x in T: print(x, end= ' ')
print('\n')

#przypisanie krotek w pętli for
T=[(1,2),(3,4),(5,6)]
for (a,b) in T:
    print(a,b)

D={'a':1,'b':2,'c':3}
for key in D:
    print(key,'=>',D[key])

for both in T:
    a,b = both  #odpowiednik z przypisaniem ręcznym
    print(a,b)

#przykład z sekwencjami zagneiżdzonymi
for ((a,b),c) in [([1,2],3),('XY',6)]: print(a,b,c)

#rozszerzone przypisania
a,*b,c = (1,2,3,4)
print(a,b,c)
for (a,*b,c) in ['test','kupa']: print(a,b,c)

#zagnieżdżone pętle for
items = ['aaa', 111, (4,5), 2.01]
tests = [(4,5), 3.14]

for key in tests:
    for item in items:
        if item == key:
            print(key, 'znaleziono')
            break
    else:
        print(key, 'nie znaleziono')

seq1 = 'mielonka'
seq2 = 'biedronka'
res = []
for x in seq1:
    if x in seq2:
        res.append(x)
print(res)
