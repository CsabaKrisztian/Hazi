import random
szam = int(input('Adj meg egy szamot: '))
randomszam = random.randint(1,3)
if randomszam > szam :
    print('A szamod kisebb mint a generalt szam')
elif randomszam < szam :
    print('A szamod nagyobb mint a generalt szam')
else:
    print('A szam amit megadtal egyenlo a generalt szammal')
    