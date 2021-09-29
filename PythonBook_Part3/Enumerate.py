#przykładowe użycie
S='mielonka'
for (offset,item) in enumerate(S):
    print(item, 'wystepuje na pozycji',offset)

E = enumerate(S)
print(next(E))  #(0, 'm')
print(next(E))  #(1, 'i')
print(next(E))  #(2, 'e')

print([c*i for (c,i) in enumerate(S)])
