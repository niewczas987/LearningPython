#listy składane vs map
res = [ord(x) for x in 'mielonka']
print(res)
print([x**2 for x in range(10)])        #kwadrat liczb 0-9 przy użyciu listy składanej
print(list(map((lambda x: x**2),range(10))))    #to samo przy użyciu map

#dodanie warunków i pętli zagnieżdżonych
print([x for x in range(5) if x%2==0])  #lista składana
print(list(filter((lambda x:x%2==0), range(5))))  #funkcja filter
res=[]                                  #użycie pętli for
for x in range(5):
    if x%2==0:
        res.append(x)
print(res)
#podwojne zagniezdzanie
res= [x+y for x in [0,1,2] for y in [100,200,300]]
print(res)
res = [x+y for x in 'mielonka' for y in 'MIELONKA']
print(res)
res = [(x,y) for x in range(5) if x%2==0 for y in range(5) if y%2==1]
print(res)

#listy składane i macierze
M = [[1,2,3],
     [4,5,6],
     [7,8,9]]
N = [[2,2,2],
     [3,3,3],
     [4,4,4]]
print([row[1] for row in M])    #[2, 5, 8]
print([M[row][1] for row in (0,1,2)])   #[2, 5, 8]
print([M[i][i] for i in range(len(M))]) #[1, 5, 9] - przekątna macierzy

print([M[row][col] * N[row][col] for row in range(3) for col in range(3)])  #[2, 4, 6, 12, 15, 18, 28, 32, 36] pomnożenie przez siebie komórek macierzy
print([[M[row][col] * N[row][col] for col in range(3)] for row in range(3)])    #[[2, 4, 6], [12, 15, 18], [28, 32, 36]]