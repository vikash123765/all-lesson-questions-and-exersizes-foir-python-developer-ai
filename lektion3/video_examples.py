## While loop 

""" name = input ("enter your name")

while  name == "" : 
    print("you did not enter anything")
    name = input ("enter your name")

print(f"Hello {name}")
 """


""" age = int(input("enter your age"))

while age <0:
    print("age cant be nagative")
    age = int(input("enter your age"))
print(f"you are {age} years old")     """
""" 

food = (input("enter a food you like"))

while not food == "q":
    print(f"you like you {food}")
    food= input(f"enter another food you like or q to quit")
print("Bye")    
 """


""" num = int(input("enter a num between 1 and 10"))

while num < 1 or num > 10:
    print(f"{num} is not valid ")
    num = int(input("enter a valid num"))


print(f"you num is {num}")     """


## for loop == exectus a code block a fixe number of times
""" 
for  i in range(1,10+1):
    print(i)
print("happy new year")    

 """

""" for  i in reversed(range(1,10+1,2)):##start,stop,step
    print(i)
print("happy new year")    

 """


""" credit_card = "1234 4334 6784 2345"


for num in credit_card:
    print(num ,end="") """


for x in range(1,21):
    if x == 13:
        continue
    elif x == 20:
        break
    print(x)