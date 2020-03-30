mylist=[]
n=int(input("Enter size of the list:\n"))
 
for i in range(0,n):
    temp=int(input("Enter number to append:\n"))
    mylist.append(temp)
 
print(mylist)


for x in mylist:
  for y in range(1,x+1):
    if (y % 3 == 0):
      if (y % 5 == 0) and (y % 3 == 0):
        print("fizzbuzz")
      else:  
        print("fizz")
    elif (y % 5 == 0):
      if (y % 5 == 0) and (y % 3 == 0):
        print("fizzbuzz")
      else:  
        print("buzz")
    else:
      print(y)
    y += 1      
      
