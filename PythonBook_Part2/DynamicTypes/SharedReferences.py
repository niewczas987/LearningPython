a=3
b=a
a = a+2
print(a)    #5
print(b)    #3

L1 = [2,3,4]
L2=L1
L1[0]=24
print(L1)   #[24,3,4]
print(L2)   #[24,3,4]

#kopiowanie listy
L1 = [2,3,4]
L2=L1[:]
L1[0]=24
print(L1)   #[24,3,4]
print(L2)   #[2,3,4]

#obiekty kopiuje się funkcją 'copy'

#referencje współdzielone, a równość
L = [1,2,3]
M=L
print(L==M)    #true
print(L is M)  #true

L = [1,2,3]
M = [1,2,3]
print(L==M)    #true
print(L is M)  #false   - pokazuje to, że M jest referencją do innego obiektu, o tej samej wartosci

X=42
Y=42
print(X==Y) #true
print(X is Y)   #true - obie zmienne odnosza sie do tego samego obiektu o wartosci '42'
