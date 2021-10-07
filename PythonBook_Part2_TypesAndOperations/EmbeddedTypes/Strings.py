#LANCUCHY ZNAKOW
S = 'Test'
print('Operacje na łańcuchu znaków: '+S)
print(len(S))   #dlugosc ciagu znakow S
print(S[0])     #pierwszy znak ciagu znakow S
print(S[-1])    #ostatni znak ciagu znakow S
print(S[-2])    #drugi od końca znak ciagu znakow S
print(S[1:3])   #wycinek S z indeksami 1 do 2, bez 3
print(S[1:])    #wszystko poza 1 znakiem
print(S+ 'xyz') #konkatenacja
print(S * 3)    #3-krotne powtorzenie

#niezmiennosc - wyrazenie pozostaje bez zmian, dopoki go nie nadpiszemy
print('Przed zmianą: '+S)
S = 'z' + S[1:]
print('Po zamianie pierwszej litery : '+S)
S='Test'

#metody specyficzne dla łańcucha znaków
#find - odnalezienie przesuniecia podlancucha (jezeli nie ma to zwraca -1)
print(S.find('es'))

#replace - zastąpienie podłańcucha inym
print(S.replace('es','XYZ'))

#podzielenie na ograniczniku - metoda split
line = 'aaa,bbbbb,cc,ddddd'
print(line)
print('Po metodize split: ')
print(line.split(','))

#isaplpha, isdigit, isalnum
print('IsAlpha: ' + str(line.isalpha()))
print('IsDigit: '+str(line.isdigit()))
print('IsAlNum: '+ str(line.isalnum()))

#rstrip - usuniecie bialych znakow
line = line+'\n'
print(line)
print('===============')
print(line.rstrip())
print('===============')

#formatowanie ciągu znaków
line = '%s %s kurwa świnia' % ('Arka','Gdynie')             #wyrażenie formatujące
print(line)
line = '{0} {1} gówno w wiadrze'.format('Górnik','Zabrze')  #metoda formatujaca
print(line)

#dopasowywanie wzorcow
import re
match = re.match('/(.*)/(.*)/(.*)','/usr/home/drwal')
print(match.groups())

print('========================================================================')