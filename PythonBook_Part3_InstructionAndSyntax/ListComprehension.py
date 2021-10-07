L=[1,2,3,4,5]
print(L)
L=[x+10 for x in L]
print(L)

#wykorzystanie list składanych w plikach
f= open('Expressions.py')
lines = f.readlines()
print(lines)
lines = [line.rstrip() for line in lines] #usunięcie znaku końca wiersza z listy
print(lines)
lines = [line.upper() for line in lines] #przykłądy uniwersalnosci zastsowanie
print(lines)
lines = [line.rstrip().lower() for line in lines]
print(lines)
lines = [line.replace(' ','-') for line in lines]
print(lines)

#rozszerzona składnia list składanych
f= open('Expressions.py')
lines = f.readlines()
lines = [line.rstrip() for line in lines if line[0]=='#']   #wypisanie tylko linii zaczynających się od '#'
print(lines)
#iny przykłąd
print([x+y for x in 'ab' for y in 'xyz'])