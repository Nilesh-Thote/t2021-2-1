"""Problem-3: With a single integer as the input,
 generate the following until a = x """
a=int(input("Enter the no: "))              #Asking user for input
i=1
if a%2==0:                                  #If  the user input number is an even number then it will print odd series that will be 1 less count than that of user input number.
  count=1
  while count<a:
    if i%2!=0:
      print(i,end=",")
      count+=1
    i+=1
else:                                       #Else it will print odd series Equal to the count of user input number.
  count=0   
  while count!=a:
    if i%2!=0:
      print(i,end=",")
      count+=1
    i+=1
print("\b")