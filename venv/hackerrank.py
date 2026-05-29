# problem 1
if __name__ == '__main__':
    print("Hello, World!")


# problem 2
if __name__ == '__main__':
    a = int(input())
    b = int(input())
 
sum = a + b
sub = a - b
mul = a * b

print(sum)
print(sub)
print(mul)


# problem 3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
intdiv = a // b
floatdiv = a / b

print(intdiv)
print(floatdiv)



#problem 4
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if(n % 2 == 1):
    print("Weird")
elif(n % 2 == 0 and 2 <= n <= 5):
    print("Not Weird")
elif(n % 2 == 0 and 6 <= n <= 20):
    print("Weird")
elif(n % 2 == 0 and n > 20):
    print("Not Weird")    
else:
    print("Weird")




#problem 5
if __name__ == '__main__':
   n = int(input())
   
i = 0
    
while   i < n:
    print(i**2)
    i += 1
