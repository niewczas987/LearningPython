#funkcja range
print(list(range(5)))       #[0, 1, 2, 3, 4]
print(list(range(2,5)))     #[2, 3, 4]
print(list(range(0,10,2)))  #[0, 2, 4, 6, 8]

for x in range(3):
    print(x, 'Python')

X = 'mielonka'
for item in X: print(item, end = ' ')

i=0
while i<len(X):
    print(X[i],end=' ')
    i +=1

for i in range(len(X)): print(X[i],end = ' ')
print('\n')
#przechodzenie niewyczerpujace - range i wycinki
S='abcdefghijklmn'
for i in range(0, len(S),2): print(S[i],end =' ')
print('\n')
for c in S[::2]: print(c,end = ' ')
print('\n')

#modyfikacje list - range
L=[1,2,3,4,5]
for i in range(len(L)):
    L[i] += 1
print(L)