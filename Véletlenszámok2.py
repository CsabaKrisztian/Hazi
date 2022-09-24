import random
szam = random.randint(1,2)
kerdes = input('fej vagy iras?: ')
fej = ('fej')
iras = ('iras')
iras = 1
fej = 2
if szam == fej:
    print('Eltalaltad')
elif szam != fej:
    print('Nem talatad el')
elif szam ==  iras:
    print('Eltalatad')
elif szam != iras:
    print('Nem talatad el')