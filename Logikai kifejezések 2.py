kerdes1 = input('Jon Henrik ma kosarazni?: ')
kerdes2 = input('Jon Hanna ma kosarazni?: ')
igen = ('igen')
nem = ('nem')
if kerdes1 == igen and kerdes2 ==igen :
    print('Mindketten jonnek')
elif kerdes1 == igen and kerdes2 == nem :
    print('Egyikuk nem jon')
elif kerdes1 == nem and kerdes2 == igen :
    print('Egyikuk nem jon')
else:
    print('Egyikuk se jon')
