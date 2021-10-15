from person import Person, Manager
bob = Person('Robert Green')
anna = Person('Ann Red', 'Programmer', 5000)
tom = Manager('Tom Black', 50000)

import shelve
db = shelve.open('person_db')
for object in (bob,anna,tom):
    db[object.name] = object
db.close()