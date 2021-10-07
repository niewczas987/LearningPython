#PLIKI
f = open('data.txt', 'w')        #utworzenie nowego pliku w trybie do zapisu
f.write('Czesc!\n')             #zapisanie lancucha znakow do pliku
f.write('xD\n')
f.close()                       #zamkniecie pliku i wyczyszczenie bufora

f=open('data.txt')              #bez 'r', bo read jest domyslnym typem przetwarzania
text = f.read()
print(text)
print(text.split())