# t2021-2-1
Used Python Programming Language.
## Problem-1
Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.

Program-1.py contain Class Calculator and it has 4 methods Addition, Subtraction, Multiplication and Division.\
Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string.\
It also contain try and except block for ZeroDivisionError.
``` python
def Division(self,a,b):
      try:
        div=a/b
        print(a,"/",b," = ",div)
      except ZeroDivisionError:
        print("You cannot divide a number by Zero")
```
It give output as follows:
```terminal
Enter the value of a: 1
Enter the value of b: 9
type of operation: -
1.0 - 9.0  =  -8.0
```
## Problem-2
With a single integer as the input, generate the following until a = x.\
Output: (examples)
1) input a = 1, then output : 1
2) input a = 2, then output : 1, 3
3) input a = 3, then output : 1, 3, 5
4) input a = 4, then output : 1, 3, 5, 7

It will take input and assign it to variable 'a'.\
It contain a ```while``` loop that will run till count is equal to 'a'.
```python
while count!=a:
  if i%2!=0:
    print(i,end=",")
    count+=1
  i+=1
```
It give output as follows:
```terminal
Enter the no: 10
1,3,5,7,9,11,13,15,17,19
```
## Problem-3
With a single integer as the input, generate the following until a = x
Output: (examples)
1) input a = 1, then output : 1
2) input a = 2, then output : 1
3) input a = 3, then output : 1, 3, 5
4) input a = 4, then output : 1, 3, 5
5) input a = 5, then output : 1, 3, 5, 7, 9
6) input a = 6, then output : 1, 3, 5, 7, 9

It contain ```if``` and ```else``` statement. If 'a' is even number then will it give series of odd numbers and the count of those numbers will be 1 less then that of the even number. For eg, a=6, then it will give series of odd numbers and count of that series will be 5.\
Else if it's a odd number then it will give series of odd numbers and the count of those numbers will be equal to that of odd numbers. For eg, a=5, then will give series of odd no and the count of series is 5.\
It contain ```while``` block for printing the series of odd numbers.
```terminal
Enter the no: 8
1,3,5,7,9,11,13
```
## Problem-4
Get the total count of number list in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]\
(examples)
input: [1,2,8,9,12,46,76,82,15,20,30]\
Output:
{1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
It contain a ```while``` block to find the count of the numbers in the list which is given by the user that are multiple of the numbers from '1' to '9' and the multiple is stored as key and count is stored as value in the dictionary.
```python
while mul<10:
  count=0
  for i in a:
    if i%mul==0:
      count+=1
  b[mul]=count
  mul+=1
```
It give output as follows:
```terminal
Enter the List: [1,2,8,9,12,46,76,82,15,20,30]
{1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
```


