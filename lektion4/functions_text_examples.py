""" def is_prime(n):
    if n <= 1: ## if n is lesss then  or equal to 1 its not a prime
        return False 
    elif n == 2: ##  if n is exactly 2 as it is the only even prime number
        return True 
    
    for i in range(2,n):## start loop from 2 up to n(not including the stop value)
        if n % i == 0: ## check if n is divisible by i(n % i fives us the remainder of n devided  by i)
            return False ## if n is divisble by any i its false, because then n is not a prime number
    return True  ## if loop completes without any devisors its a prime number

print(is_prime(13))

 """
## function with 2 arguments
""" 

def sum(n1,n2):
    sum = n1+n2
    return sum


print(sum(2,3)) """

## few math import inbuilt functions 

""" import math


sqr_root= math.sqrt(4)
print(sqr_root)

power = pow(2,3)

print(power) """


##Assignment 

""" 
## function to find avarage marks  
def avg_marks(m):
    avg=sum(m) / len(m)
    return avg


##calcaulte the grade and then return it  
def compute_grade(avg_marks):
    if avg_marks >=80:
        grade="A"
    elif avg_marks >=60:
        grade="B"  
    elif avg_marks >=50:
        grade="C"
    else:
        grade="F"
    return grade              




marks = [55,64,75,80,65]


avaarge_marks= avg_marks(marks)
print(avaarge_marks)

grade=compute_grade(avaarge_marks)

print(grade) """


## to add an multiply with functions

""" 
def add_nums(n1,n2):
    sum =n1 +n2
    return sum



def multiply_nums(n1,n2):
    result =n1* n2
    return result


add=add_nums(2,3)
print(add)
multiply = multiply_nums(2,3)
print(multiply)

 """
