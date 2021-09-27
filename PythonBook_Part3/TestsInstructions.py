#pętle interaktywne
while True:
    reply = input('Wpisz tekst:')
    if reply == 'stop':break
    try:
        num = int(reply)
    except:
        print('Złe dane! '*5)
    else:
        print(int(reply)**2)
print('Koniec')
