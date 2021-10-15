import shelve
db = shelve.open('person_db')
for key in sorted(db):
    print(key,'=>',db[key])

anna = db['Ann Red']
anna.giveRaise(.10)
db['Ann Red'] = anna
db.close()