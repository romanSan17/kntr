#from random import *

#kesk1=0
#kesk2=0
#for i in range(N):
#    h1=randit(1,5)
#    h2=randit(1,5)
#    kesk1+=h1
#    kesk2+=h2
#kesk1/=N
#kesk2/=N
#print(f"Keskmine hinne 1 klassis on {kesk1}")
#print(f"Keskmine hinne 2 klassis on {kesk2}")



#1
#while True:
#    try:
#        mitu=int(input("Mitu tk: "))
#        if 1<=mitu<10:
#            break   
#    except ValueError:
#        print("Vale tüüp")

#for i in range(mitu):
#    print(' /V\ '.center(10,' '))
#print()
#for i in range(mitu):
#    print(' / V \ '.center(10,' '))
#print()
#for i in range(mitu):
#    print(' / V V \ '.center(10,' '))
#print()
#for i in range(mitu):
#    print(' /VV V VV\ '.center(10,' '))
#print()


##4
#from random import *
#sum_num=0
#sum_km=0
#for i in range(12):
#    num=randint(1000,100000)
#    km=randint(1,1000)
#    sum_num+=num
#    sum_km+=km
#    print(f"{i}. maakond. \nElanikud: {num}. Pindala: {km}\n Kokku: {sum_num},{sum_km}")
#vastus=sum_num/sum_km

from random import *
while True:
    try:
        K=int(input("Mitu kotlet sul on? "))
        if K>0: break
    except ValueError:
        print ("Vale tüüp")
while True:
    try:
        M=int(input("Mitu kotleti ühel pannil? "))
        if M>0: break
    except ValueError:
        print("Vale tüüp")
lisapann=0
pann=0
while K>0:
    if K>=M:
        K-=M
        pann+=1
        print(f"Praetud: {pann} tk")
    else:
        lisapann+=1
        print(f"Praetud: {lisapann} tk")
        break
print(f"Täispannid: {pann} ja veel on vaja {lisapann}")