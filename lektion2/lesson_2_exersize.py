 #1. Använd input() för att fråga efter ett telefonnummer
 #2. Konvertera det till ett nummer
 #3. Skriv något med variabeln med hjälp av print(), tex. “Your number is XYZ”


""" number = int(input("please eneter you number"))
print(f"you number is{number}") """

## to check if value is true or false via bool and to check the dataype via type 

""" spam = "True"
spam = bool(spam)

print(spam)
print(type(spam))

 """

# chekcing diffrent values via bool to see which return  true or flase. 

""" # This is all True
bool("A string") # A non empty string
bool(-0.5) # A number that is not 0
bool([0]) # A list that is not empty here we are referign to index position 0 in the list

# These are False
bool("") # An empty string   
bool(0.000) # The number 0    here its simply the value 0 
bool([]) # An empty list   
bool(None) # The special None type """




# Compare some values
""" first= x = 10
print(first)
second =x > 10 # False
print(second)
x < 10 # False
x <= 10 # True

# We can do two comparisons at the same time
5 < x < 15 # True
 """



""" first_value = 50
second_value = 50 # VI ÄNDRAR DENNA TILL 40

# True or false?
if first_value == 50 and second_value == 50:
    print("true")
else:
    print("false") """


# What does this print?
""" b = False and "some text"   ## fattar intew direkt är det för att vi assignar false så blir inte texten del utav variale ? 
print(b)
 """

## or operator 

""" first_value = 50
second_value = 40
third_value = 50
fourth_value = 40

# We can add any number of expressions. This uses 4 expressions.
if first_value == 50 or second_value == 50 or fourth_value == 40 or third_value == 30:
     print("true")
else:
    print("false") 

 """


# What does this print?
""" a = True or "some text"   ## again it only printing True is it because boolean values has higher hirechry then string values therefor its only assigning the bool value to variable ? 
print(a) """

""" 
print(45+45 == 90 and not  30 + 30 == 50 and 2*20 == 2 + 38)   ## here and not is a true expression if we remove the not it will become false expression, altought this is a very wierd way of writing code. 30 +30 == 50 is false by using not befpre the expression we make it to true value
 """


## nested if statement 


""" name = 'Mary'
password = 'swordfish'
if name == 'Mary':  
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted. Welcome home!')  
 """


# Uppgift
#Du ska be en användare om en siffra mellan 1 och 3.
#Printa något ifall användaren väljer 1 eller 2. Gör inget om användaren väljer 3.

number = int(input("please choose anumber between 1 and 3 "))

if number >= 1 and number <= 2:
    print(f"you chose {number} ac3ess granted")
elif number == 3:
     pass
else:
     print(f"please choosa a valid number. you number was{number} ")
 


# Uppgift 1

#Kodan nedan kommer ge dig en slumpmässig siffra mellan 1 till 6. Skriv ett program som gör följande:

#- printar “A number between 0 and 2!” om numret är mellan 0 och 2
#- printar “The number is 3!” om det endast är en trea
#- printar "fizzbuzz" om numret är högre än 3 och mindre eller lika med 5
#- printar “Hmm, probably something else!” om ovanstående tre punkter inte gäller


""" import random


num = random.randint(1,6)
print(num)

if num >=0 and num <=2:
    print("A number between 0 and 2!")
elif num == 3:
    print("“The number is 3!” " )  
elif num > 3 or num <= 5:
    print("fissbuzz")
else:
    print("Hmm, probably something else!")

 """

 


