#automatyczne przekierowanie strumienia
# import sys
# temp = sys.stdout
# sys.stdout = open('log.txt','a')    #przekierowanie zapisu do pliku
# print('mielonka'*3)
# print('1,2,3')
# sys.stdout.close()
# sys.stdout = temp

print('znow jestem w konsoli')
print(open('log.txt').read())

#zapisywanie komunikatow o bledach
# sys.stderr.write(('xD'*8+'\n'))