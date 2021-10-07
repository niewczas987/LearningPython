#przypisanie sekwencji
nudge =1
wink = 2
A,B = nudge,wink    #przypisanie krotki
print(A,B)
[C,D] = [nudge,wink]    #przypisanie listy
print(C,D)

[a,b,c] = (1,2,3)   #przypisanie krotki wartosci do liaty nazw
print(a,c) #1 3
(a,b,c) = "ABC"     #przypisanie łańcucha znaków do krotki
print(a,c)  #A C

#zaawansowane wzorce przypisania sekwencji
string = 'JAJO'
a,b,c,d = string
print(a,d)  #J O

a,b,c = string[0],string[1],string[2:]  #indeksowanie i wycinek
print(a,b,c)
(a,b),c = string[:2],string[2:]     #zagnieżdżone sekwencje
print(a,b,c)
((a,b),c) = ('JA','JO')     #połaczone w pary zgodnie z ksztaltem i pozycja
print(a,b,c)
red, green, blue = range(3) #przypisanie serii liczb całkowitych do zbioru zmiennych
print(red, blue)
#dzielenie sekwencji
L=[1,2,3,4]
while L:
    front, L = L[0],L[1:]
    print(front,L)

#rozszerzona składnia rozpakowania
seq = [1,2,3,4]
a,*b = seq
print(a,b)  #1 [2, 3, 4]
*a,b = seq
print(a,b)  #[1, 2, 3] 4
a,*b,c = seq
print(a,b,c) #1 [2, 3] 4
L=[1,2,3,4]
while L:
    front, *L = L
    print(front,L)  #ten sam ekfekt co wyżej