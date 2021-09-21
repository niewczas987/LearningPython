# cudzyslowy i apostrofy sa tym samym
print(('żywpłot,"żywopłot'))
print(('ryc"erz', "ryc'erz"))
title = "Life of" 'Brian'  # niejawna konkatenacja
print(title)
print(('ryc\'erz', "ryc\"erz"))  # sekwencje ucieczki

# bajty specjalne - escape sequences
s = 'a\nb\tc'
print(s)
print(len(s))  # 5 znaków w stringu 's'

s = 'a\0b\0c'
print(s)
print(len(s))  # 5 z dwonma zerami binarnymi

s = '\001\002\x03'
print(s)
print(len(s))

# jeżeli chcemy odwołaś się do ścieżkoi należy pamiętać o dodaniu przed stringa litery r - r'C\nowy\texkst.txt', lub zastosowaniu '\\'
print('C:\nowy\tekst.txt')  # C: \n owy	ekst.txt
print(r'C:\nowy\tekst.txt')  # C:\nowy\tekst.txt

# blokowe łańcuchy znaków
mantra = """
Zawsze patrz
na życie
z humorem"""

print(mantra)

# Operacje podstawowe
a = 'abc'
print(a)
print(len(a))  # dlugosc
print('abc' + 'def')  # konkatenacja
print('=' * 8)  # powtorzenie

myjob = 'haker'
for c in myjob: print(c, end=' ')
print('k' in myjob)  # true
print('z' in myjob)  # false
print('ker' in myjob)  # true
S = 'mielonka'
print((S[1:3], S[1:], S[:-1]))  # ('ie', 'ielonka', 'mielonk')
print(S[3:-1])  # lonk    - wycinki są pobierane <:) zamkniety z lewej i otwarty z prawej
# trzeci limit (krok) i obiekty wycinkow
S = 'abcdefghijklmnoprstuwyz'
print(S[::2])  # acegikmortwz - co 2 element
print(S[::10])  # akw - co 10 element
S = 'halo'
print(S[::-1])  # olah - odwrócona kolejnosc znakow
# skladnia wycinkow - slices
print('mielonka'[1:3])
print('mielonka'[slice(1, 3)])
print('mielonka'[::-1])
print('mielonka'[slice(None, None, -1)])

# konwersje kodu znaków
print(ord('s'))  # 115
print(chr(115))  # s
S = 'mielonka'
S = S + 'MIELONKA!'  # mielonkaMIELONKA!
print(S)
S = S[:8] + 'JAJKA' + S[-1]  # mielonkaJAJKA!
print(S)
S = 'mielonka'
S = S.replace('lon', 'lonecz')
print(S)  # mieloneczka
print('Ten %d %s jest martwy' % (1, 'ptak'))
print('Ten {0} {1} jest żywy'.format(1, 'ptak'))
# alternatywy dla replace - find
S = 'xxxJAJKAxxxxJAJKAxxxx'
where = S.find('JAJKA')
S = S[:where] + 'MIELONKA' + S[(where + 5):]
print(S)
S = 'xxxJAJKAxxxxJAJKAxxxx'
print(S.replace('JAJKA', 'MIALONKA'))  # zastepuje wszystkie wystapienia 'JAJKA'
print(S.replace('JAJKA', 'MIALONKA', 1))  # zastepuje tylko 1 wystapienie slowa 'JAJKA'

# instrukcje list i join
S = 'gate'
L = list(S)
print(S)
print(L)
S = ''.join(L)
print(S)

# analiza składniowa tekstów
line = 'aaa bbb ccc'
print(line)
cols = line.split()
print(cols)

# inne metody na lancuchach znakow
line = 'Rycerze, którzy mówią Ni!\n'
print(line.rstrip())  # usuniecie znakow niewidocznych
print(line.upper())  # znaki do uppercase'a
print(line.isalpha())  # false - nie jest wartoscia alfanumeryczna
print(line.endswith('NI!\n'))  # false - zakonczenie strinka wartoscia'NI!'

# wyrażenia formatujące
for x in range(0, 5):
    print('Przyklad wyrazenia formatujacego nr %s.' % (x))
x = 1234
print('integers:  %d , %-6d , %06d' % (x, x, x))  # integers:  1234 , 1234   , 001234
x = 1.23456789
print('%e | %f | %g' % (x, x, x))  # 1.234568e+00 | 1.234568 | 1.23457
print('%-6f | %05.2f | %+06.1f' % (x, x, x))  # 1.234568 | 01.23 | +001.2

reply = """
Witaj %(name)s,
Twoj wiek to %(age)s lat"""
values = {'name': 'Adam', 'age': 22}
print (reply%values)

#metoda format
template = '{0}, {1} and {2}'
print(template.format('raz','dwa','trzy'))
#klucze, atrybuty, przesunięcia
import sys
print('Mój 1[spam] ma zainstalowany system {0.platform}'.format(sys, {'spam':'PC'}))

#porownanie z wyrazeniami formatujacymi
template = '%s, %s, %s'
print(template % ('raz','dwa','trzy'))  #raz, dwa, trzy - podstawienie pozycyjne
template = '%(motto)s, %(pork)s , %(food)s'
print(template % dict(motto = 'mielonka', pork = 'szynka', food ='jajka'))  #podstawienie słownikowe`