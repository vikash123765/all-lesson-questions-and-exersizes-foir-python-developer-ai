
# if else statemnts 

""" age =int(input("Whats childs age"))
age_at_kindergatden= 5

thomas_age=5

age_at_kindergatden= 5



if(thomas_age > age_at_kindergatden):
    print("thhomas is in preschool")
elif(thomas_age == age_at_kindergatden):
    print("thomas is at kimdergarten") 
else:
    print("thomas is on other class")     
 """

##creating function with som lines of code 
""" def printVikash():
    text="vikash has a great website"
    print(text)
    print(text)
    print(text)

printVikash() # calling the fuinction   """  

##creating function with som lines of code 
""" def printVikash(text): ## eciving argument in the paramater
    print(text)
    print(text)
    print(text)


text= "vikash is the best"  ## creating argument

printVikash(text)    ## passing argument into the functions parameter
 """


## if statement inside a function 

""" def adultOrNot(age):
    if(age < 18 ):
        print("you are a minor")
    else:
        print("you are an adult")


age=13

adultOrNot(age)
 """


## if statement inside a function with two arguments 

""" def school_age_calcultaor(age,name):
    if age < 5:
        print(f"enjoy your time, {name} is only {age}")
    elif age == 5:
        print(f"enjoy kindergarten, {name}")    
    else:
        print("they grow upp so fast")    


school_age_calcultaor(9,"jhonny") """

## how to get value back from function

""" def age_In_10_Years(age):
    age_after_10_years=age +10
    return age_after_10_years

how_old_will_i_be = age_In_10_Years(9)

print(f"you will be {how_old_will_i_be} in 10 years") """

## creating loop in pyhton 

# while loop 

""" x = 0

while(x < 5):
    print(x)
    x +=1 
 """
# for looop

""" for i in range(5,10):
    print(i)
 """

# loop trough array
"""  
days=["Mon","Tis","ons","Tors","Fre","lör","sön",] 

for day in days:
    if(day == "Tors"):
        #break   will stop on element before tors
        continue #will skip tors 
    print(day)
 """


""" 
import math 

print("pi is",math.pi)

 """

""" age = 25
print(f"Han är {age} år gammal.") """


### **Uppgift 6.**
#Vad gör input()-funktionen? Varför är den användbar? Svara med meningar.

# Skriv ett program som ber användaren skriva in sitt namn, printa sedan ut det i terminalen


# input ör till för att ta emot/lagra  ett värde från användaren 

""" name= input("vad är ditt namn")
print(name) """


# Korrigera koden
""" number = float(input("Ange ett nummer: "))
half = number / 2 
print("Hälften av ditt nummer är " + str(half)) """


""" gpa = 22.2

print(type(gpa)) """

##upprepa text ett antal gånger
""" 
text="ingen ör sig pyhton med hjälp av enbart memory"

for i in range(1000):
    print(text) """



