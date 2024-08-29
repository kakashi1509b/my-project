c=1
while c!=0:
    a=int(input("Enter your number: "))
    if a==0:
        print("The factorial is: ",0)
    elif a==1:
        print("The factorial is: ",1)
    else:
        n=1
        lst=[x for x in range(2,a+1)]
        for y in lst:
            n *= y
        print("The factorial is: ",n)        

