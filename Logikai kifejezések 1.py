szam= int(input('Adj meg egy szamot: '))
if szam > 0 and szam % 2 == 0 :
    print('A szamod pozitiv es paros')
elif szam < 0 and szam % 2 != 0 :
    print('A szamod negativ es paratlan')
