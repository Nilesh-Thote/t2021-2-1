"""Problem-2: With a single integer as the input, 
generate the following until a = x"""
a=int(input("Enter the no: "))    #Asking user for input
count=0
i=1
while count!=a:                   #Loop will run till count is equal to input number
  if i%2!=0:                      #To print odd series
    print(i,end=",")
    count+=1
  i+=1
print("\b")                       #To remove the last comma from series.