#operacje podstawowe
L= [1,2,3]
print(len(L))   #dlugosc
L= L + [4,5,6]     #konkatenacja
print(L)
L=['He']*10 #powtorzenie
print(L)

#iteracje i składanie
L=[1,2,3]
print(3 in L)   #true
for x in L:     #iteracja
    print(x,end=' ')

res = [c*4 for c in 'QWE']  #lista składana
print(res)
print(list(map(abs, [-1,-2,0,1,2])))    #wywolanie funkcji map na sekwencji

#indeksowanie, wycinki i macierze
L=['qwe','QWE','Q-W-E']
print(L[1]) #QWE
print(L[-1])    #Q-W-E
print(L[1:])    #['QWE', 'Q-W-E']
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1])    #[4, 5, 6]
print(matrix[1][1]) #5

#modyfikowanie list w miejscu
L=['qwe','QWE','Q-W-E']
L[1]= 'xxx'
print(L)    #['qwe', 'xxx', 'Q-W-E']
L[0:2] = ['XXX','DDD']
print(L)    #['XXX', 'DDD', 'Q-W-E']

#metody na listach
L=['bbb','ccc','aaa']
L.append('xD')
print(L)    #['bbb', 'ccc', 'aaa', 'xD']
L.sort()
print(L)    #['aaa', 'bbb', 'ccc', 'xD']

L=[1,2]
L.extend([3,4,5])
print(L)    #[1, 2, 3, 4, 5]
L.pop()
print(L)    #[1, 2, 3, 4]
L.reverse()
print(L)    #[4, 3, 2, 1]
print(list(reversed(L)))    #[1, 2, 3, 4]

L = ['mielonka','jajka','szynka']
print(L.index('jajka')) #1
L.insert(1,'tost')
print(L)    #['mielonka', 'tost', 'jajka', 'szynka']
L.remove('jajka')
print(L)    #['mielonka', 'tost', 'szynka']
L.pop(1)
print(L)    #['mielonka', 'szynka']
del(L[0])
print(L)    #['szynka']
L= L*5
print(L)    #['szynka', 'szynka', 'szynka', 'szynka', 'szynka']
del(L[2:])
print(L)    #['szynka', 'szynka']