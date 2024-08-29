print("Check your number as prime or not")
c=1
while c!=0:
    a=int(input("Enter your number: "))
    if a==1:
        print("It is not prime neither composite")
    elif a==2:
        print("It is prime")    
    else:
        i=[x for x in range(2,a)]
        b=[a % element for element in i]
        if 0 in b:
            print("This is not prime")
        else:
            print("This is prime")
