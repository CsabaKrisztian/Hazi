import random
genszam = random.randint(1, 5)

szam= int(input('Adj meg egy szamot: '))
if szam == genszam :
    print('A szamod egyenlo')
elif szam > genszam :
    print('A szamod nagyobb')
else:
    print ('A szamod kisebb')
   
