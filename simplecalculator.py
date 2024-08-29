print("A simple calculator")
c=1
while c!=0:
    a=int(input("Enter your first number: "))
    b=int(input("Enter your second number: "))
    print(" '+' for addition \n '-' for subtraction \n '*' for multiplication \n '/' for division \n '**' for exponent \n '%' for modulus \n ")
    y=input("Select your operation: ")
    if y=="+":
        print("Your solution: ",a+b)
    elif y=="-":
        print("Your solution: ",a-b)
    elif y=="*":
        print("Your solution: ",a*b)
    elif y=="/":
        print("Your solution: ",a/b)
    elif y=="**":
        print("Your solution: ",a**b)
    elif y=="%":
        print("Your solution: ",a%b)                    
