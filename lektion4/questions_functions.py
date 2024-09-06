#Googla på "don't repeat yourself programming", ofta förkortat "DRY" - hur hjälper funktioner dig att följa denna princip?

""" print("Happy birthday to you")

print("Happy birthday to you")

print("Happy birthday to you")

print("Happy birthday to you")

print("Happy birthday to you")

## instead we can use a function to call all theese ortn functions 

def birthday_woshes():
    print("Happy birthday to you")

    print("Happy birthday to you")

    print("Happy birthday to you")

    print("Happy birthday to you")

    print("Happy birthday to you")


birthday_woshes()

birthday_woshes() """


##### **Uppgift 2.**
#När vi pratar om funktioner, vad är
#1. En parameter?
#2. Ett argument?


""" def sum(n1,n2): ## two parameters
    total= n1 + n2
    return total

print(sum(3,7))  ## calling the function and passing 3 and 7 as arguments



 """




##Om en funktion inte haft parametrar, hade de fortfarande varit användbara?

## function without input is still usefull but it wont be dynamic instead of us oassing an argument and then we return some value based on the argument. we simply do somthing hardcoded without the use of an argument once we call it 

""" def say_hello():
    print("hello user")

say_hello() """


##2. Hur kan jag definiera en funktion på ett sätt som gör det valbart att tillhandlahålla ett argument?

""" def acess_or_not(status="public"):   ## will take this defaut value if no argument is given
    if status == "private":
        print("you are an private user you have acess")
    elif status == "public":
        print("you are an public user you dont have acess")


acess_or_not("private")

acess_or_not()   ## no argument needed 
 """


#1. Vad gör nyckelordet pass? Tex:


""" def func_with_parameter(my_parameter):
   if my_parameter < 5:
      print("you dont have enoug point")
      
     
     
   elif my_parameter> 5:
      print("you have aenough points")


print(func_with_parameter(9))

 """

##### **Uppgift 5**  Förklara vad "in" gör i denna kod gör. Keywordet används två gånger,vad är skillnaden på dessa två användningsområden?:

""" names = ["tobias", "andreas", "tove"]
new_names = []   ## create empty list 
for name in names:
   if "to" in name:     ## if to exists in name tobias,tove 
      new_names.append(name)   ## append that name to empty new names list

print(new_names) """

#2. Förklara vad "in" gör i denna kod gör:

""" names = ["doctor", "teacher", "programmer"]
exists = True   ## set exist variable to true 
if "programmer" not in names:     ## if programmer is not in names list 
   exists = False   ## then set the exist variable t false

## output will be true 
print(exists)
 """




##### **Uppgift 6**
#Kan jag anropa en funktion från en annan funktion?
""" 
def func_1():
   print("in func 1")

def func_2():
   func_1()  ## function 2 is calling function 1 
   print("in func 12")   


## but no one is calling function 2 
func_2()   #tis  is solution 
 """


##### **Uppgift 7** Kan en funktion returnera mer än ett värde? Testa!

#. Vad är typen som returneras?
#. Visa hur du direkt kan tilldela de returnerade värdena


""" def useless_function():
    return 1,2

result = useless_function()
print(type(result))   ## the class is tuple list
 """

""" 
def useless_function():
    return 1,2

first_return_value, second_return_value = useless_function()    ## we unpackar the retrun values into the variables in order 

print(first_return_value,second_return_value)
 """


#### **Uppgift 8 - Avancerad fråga**
#Vilka problem kan uppstå när du skickar in en lista som argument till en funktion?
""" 
Svar: En lista är en mutable datatyp, vilket innebär att om du skickar in en lista som argument till en funktion och ändrar innehållet i listan inuti funktionen, så kommer ändringarna att reflekteras på listan 
utanför funktionen. Detta kan leda till oavsiktliga ändringar om funktionen modifierar listan utan att du är medveten om det.
Ett relaterat problem kan vara om funktionen förväntar sig en viss typ av data men får en lista med ett oväntat format eller datatyper, vilket kan orsaka fel.


 """


#- Vilka datatyper är mutable, och vad innebär det?

##svar : det är datatyper som är ändringsbara
""" Svar: Mutable datatyper är de som kan ändras efter att de skapats. Detta innebär att vi kan modifiera deras innehåll, till exempel lägga till, ta bort eller
ändra element utan att skapa ett helt nytt objekt. Exempel på mutable datatyper i Python är listor, set och dictionary.
 """
#- Vilka datatyper är immutable, och vad innebär det?


""" Svar: Immutable datatyper är de som inte kan ändras efter att de 
skapats. Om man försöker ändra deras innehåll, skapas ett nytt 
objekt istället för att det ursprungliga objektet modifieras.
Exempel på immutable datatyper i Python är strängar (strings), 
tuples och tal (int, float).

 """


#- Fundera på om listor är mutable eller immutable
""" 
Svar: Listor är mutable. Det innebär att vi kan ändra värdena i en lista direkt genom att använda indexering, samt lägga till, ta bort eller ändra element utan att skapa
en ny lista. """
 

""" Svar: Listor är mutable. Det innebär att vi kan ändra värdena i en
lista direkt genom att använda indexering, samt lägga till, ta bort 
eller ändra element utan att skapa en ny lista. """


#- Fundera på vad primitiva värden är, och hur de påverkas av funktioner

""" Primitiva värden är immutable (oföränderliga), vilket innebär att när de skickas som argument 
till en funktion så skickas en kopia av värdet. Detta innebär att om en funktion ändrar värdet
på en primitiv variabel, så ändras inte originalvärdet utanför funktionen. Förändringarna sker endast lokalt inom funktionen.
 """
 ## exempel på primtal Primitiva värden är enkla datatyper som representerar enkla värden. De är ofta de grundläggande byggstenarna 
 # i ett programmeringsspråk. Exempel på primitiva datatyper är:
""" 
Heltal (int) – till exempel 1, 42, -7
Flyttal (float) – till exempel 3.14, -0.001
Boolean (bool) – sant (True) eller falskt (False)
Strängar (string) – en sekvens av tecken, till exempel "hej" """