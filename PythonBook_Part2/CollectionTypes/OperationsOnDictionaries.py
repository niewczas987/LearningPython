#podstawowe operacje na słownikach
D = {'mielonka':2,'szynka':1,'jajka':3}
print(D['mielonka'])    #pobranie wartosci klucza
print(len(D))           #ilosc elemenow w slowniku -> ilosc kluczy
print('szynka' in D)    #sprawdzenie istnienia klucza
print(list(D.keys()))   #utworzenie klisty kluczy

#modyfikacja slownikow w miejscu
D['szynka'] = ['grill','piecz','smaz']
print(D)    #{'mielonka': 2, 'szynka': ['grill', 'piecz', 'smaz'], 'jajka': 3}
del(D['jajka'])
print(D)    #{'mielonka': 2, 'szynka': ['grill', 'piecz', 'smaz']}
D['lunch'] = 'Bekon'
print(D)    #{'mielonka': 2, 'szynka': ['grill', 'piecz', 'smaz'], 'lunch': 'Bekon'}

#inne metody słowników
print(D.get('mielonka')) #zwraca wartosc klucza - 2
D.pop('mielonka')
print(D)    #{'szynka': ['grill', 'piecz', 'smaz'], 'lunch': 'Bekon'}

#przyklad z tabela jezykow programowania
table = {'Python':'Guido van Rossum',
         'Perl':'Larry Wall',
         'Tcl':'John Ousterhout'}
language = 'Python'
creator = table[language]
print(creator)
for lang in table:
    print(lang,'\t',table[lang])
# Python 	 Guido van Rossum
# Perl 	 Larry Wall
# Tcl 	 John Ousterhout

print(dict.fromkeys(['a','b'],0))   #utworzenie slownika z wart. domyslymi = {'a': 0, 'b': 0}

#słowniki składane
print(list(zip(['a','b','c'],[1,2,3]))) #[('a', 1), ('b', 2), ('c', 3)]
D = dict(zip(['a','b','c'],[1,2,3]))
print(D)    #{'a': 1, 'b': 2, 'c': 3} - słownik z funkcji zip
D = {k:v for (k,v) in zip(['a','b','c'],[1,2,3])}
print(D)    #{'a': 1, 'b': 2, 'c': 3} - użycie słownika składanego


#widoki słowników
D = dict(a=1,b=2,c=3)
print(D)    #{'a': 1, 'b': 2, 'c': 3}
print(D.keys())     #dict_keys(['a', 'b', 'c'])
print(D.values())   #dict_values([1, 2, 3])
print(D.items())    #dict_items([('a', 1), ('b', 2), ('c', 3)])


