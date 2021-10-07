#rozgałęzienia kodu
choice = 'szynka'

if choice == 'mielonka':
    print(1.99)
elif choice == 'szynka':
    print(2.65)
elif choice == 'boczek':
    print(21.37)
else:
    print('zły wybór')

branch = {'mielonka':1.25,'boczek':1.99,'jajka':0.65}
print(branch.get('boczek','Zły wybór'))
print(branch.get('szynka','Zły wybór'))
choice = 'boczek'
if choice in branch:    #test przynaleznosci
    print('1.54')
else:
    print('Zły wybór')

#wyrazenia trójargumentowe
A = 't' if 'mielonka' else 'f'
print(A)    #t
A = 't' if '' else 'f'
print(A)    #f