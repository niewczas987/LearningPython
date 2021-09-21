#TYPES - sprawdzanie elastycznosci kodu
L= [ 123, ' Mielonka', 1.35]
print(type(L))
if type(L) == type([]):
    print('yes')

if type(L) ==list:  #uzycie nazwy typu
    print('yes')

if isinstance(L, list): #sprawdzanie zorientowania obiektow
    print('yes')