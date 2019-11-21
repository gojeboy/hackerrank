theBill =[3,10,2,9]

k =1
b=12


def bonaAppetit(bill, k, b):

    annaCorrect = (sum(bill)- bill[k])//2

    if b == annaCorrect:
        print('Bon Appetit')
    elif b > annaCorrect:
        print(b - annaCorrect)



bonaAppetit(theBill, k,b)