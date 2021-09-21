#podstawowe poperacje na plikach
myfile = open('myfile.txt','w')     #utworzenie i otwarcie pustego pliku
myfile.write('witaj, pliku tekstowy.\n')    #zapis wiersza do pliku
myfile.write('Żegnaj pliku tekstowy\n')
myfile.close()  #zrzucenie bufora wyjsciowego na dyusk

#odczyt pliku
myfile = open('myfile.txt')
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())    #pusta linia, czyli EOF

print(open('myfile.txt').read())    #odczyt całego pliku

for line in open('myfile.txt'): #odczyt z uzyciem pętli for
    print(line, end='')

#pprzechowywanie obiektów w plikach
X,Y,Z = 43,44,45
S= 'Mielonka'
D = {'a':1,'b':2}
L=[1,2,3]

F = open('datafile.txt','w')
F.write(S+'\n')
F.write('%s,%s,%s\n'%(X,Y,Z))
F.write(str(L)+'$'+str(D)+'\n')
F.close()

chars = open('datafile.txt').read()
print(chars)

F=open('datafile.txt')
line = F.readline()
print(line)
line.rstrip()
print(line)
line = F.readline()
print(line)
parts = line.split(',')
print(parts)
numbers = [int(P) for P in parts]   #konwersja na liczby
print(numbers)
line = F.readline()
print(line)
parts = line.split('$')
print(parts)
eval(parts[0])
objects = [eval(P) for P in parts]
print(objects)

#moduł 'pickle'
print('='*20)
print('Moduł pickle')
D={'a':1,'b':2}
F = open('datafile.pkl','wb')
import pickle
pickle.dump(D,F)
F.close()

F=open('datafile.pkl','rb')
E = pickle.load(F)
print(E)