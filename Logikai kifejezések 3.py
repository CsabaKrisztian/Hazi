szam= int(input('Adj meg egy szamot: '))
if szam % 3 == 0 :
    print('A szamod oszthato 3-mal')
if szam % 4 == 0 :
    print('A szamod oszthato 4-gyel')
elif szam % 3 == 0 and 4 == 0 :
    print('A szamod 3-mal es 4-gyel is oszthato')
else:
    print('A szamod 3-mal se 4-gyel nem oszthato')