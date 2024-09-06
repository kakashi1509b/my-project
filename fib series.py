print("Fibonaaci series")
c=1
while c!=0:
 a=int(input("How many terms do you want? :"))
 lst1=[0]
 lst2=[0,1]
 lst3=[0,1,1]
 k=3
 if a<=0:
  print("Not defined")
 elif a==1:
  print(lst1)
 elif a==2:
  print(lst2)
 elif a==3:
  print(lst3)
 elif a>=4:
    while k<a:
        lst3.append( lst3[k-2]+ lst3[k-1])
        k= k + 1
    print(lst3)        
    

