def fetcher(obj, index):
    return obj[index]

x='mielonka'

#obsługa wyjątkow
try:
    fetcher(x,8)
except IndexError:
    print('mam wyjątek')
print('kontynuuje')

#zglaszanie wyjatkow
try:
    raise IndexError    #przy debugowaniu częściej używa się assert niż raise
except IndexError:
    print('test')

#assert przykład
#assert False,'Nobody expect spanish inquisition'

#wyjątki zdefiniowane przez użytkownika
class Bad(Exception):
    pass

def doomed():   #zgłoszenie instancji
    raise Bad()

try:
    doomed()
except Bad:
    print('przechwycenie Bad')

#działania końcowe - try/finally
try:
    fetcher(x,3)
finally:
    print('po pobraniu')

try:
    fetcher(x,8)
finally:
    print('po pobraniu')
print('po TRY')