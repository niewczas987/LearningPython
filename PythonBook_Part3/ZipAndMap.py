#przechodzenie równoległe
L1 = [1,2,3,4]
L2 = [5,6,7,8]
print(list(zip(L1,L2)))

for(x,y) in zip(L1,L2):
    print(x,'+',y,'=',x+y)

T1,T2,T3 = (1,2,3),(4,5,6),(7,8,9)
print(list(zip(T1,T2,T3)))  #[(1, 4, 7), (2, 5, 8), (3, 6, 9)]

#w przypadku nierownych sekwencji
S1 = 'abc'
S2 = 'xyz123'
print(list(zip(S1,S2))) #[('a', 'x'), ('b', 'y'), ('c', 'z')]

print(list(map(ord, 'mielonka')))

#tworzenie słowników za pomocą zip
keys = ['mielonka','jajka','toast']
vals = [1,2,3]
D2={}
for (k,v) in zip(keys,vals): D2[k]=v
print(D2)

D3= dict(zip(keys,vals))
print(D3)
