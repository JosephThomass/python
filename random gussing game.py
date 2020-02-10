import random
a=random.randint(0,100)
print(a)
while True:
    x=int(input("enter your guss:"))
    if a==x:
        print("you get it right")
        break
    elif (a-x)>10:
        print("getting away")
    elif abs(a-x)<5:
        print("Your are very close") 
    elif a-x<2:
        print("you are about to it ")
