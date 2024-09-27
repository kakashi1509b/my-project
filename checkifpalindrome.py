print("Check if your keyword is palindrome")
a=str(input("Enter your keyword: "))
lst1=[i for i in a]   
lst2=lst1.copy()
lst2.reverse()
if lst1==lst2:
    print("It is palindrome")
else:
    print("It is not palindrome")    