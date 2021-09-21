"""Problem-4: Get the total count of number list in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
(examples)
input: [1,2,8,9,12,46,76,82,15,20,30]
Output:
{1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}"""

a=eval(input("Enter the list: "))     #Asking User to input list.
b={}                                   
mul=1
while mul<10:                         #running while loop for number between 1 and 9
  count=0
  for i in a:
    if i%mul==0:                      #if the numbers in the list gets divided by the multiple then it will increment the counter variable
      count+=1
  b[mul]=count                        #inserting mul as key and count as value in the dictionary.
  mul+=1
print(b)