#wyłąpywanie ograniczeń - instrukcja assert
def f(x):
    assert x<0 #x musi być ujemne
    return x**2

print(f(-1))
# f(1) #assertionError

