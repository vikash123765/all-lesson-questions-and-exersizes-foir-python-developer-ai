#1. Vad är en boolean?
#2. Vilka värden är sanna och falska? Ge minst 5 exempel. Tips: 

""" print(bool("hello"))

print(bool(""))

print(bool(0))

print(bool([0]))

print(bool(33))
 """


""" age = 20
if age > 18:
    print("Du får rösta.")
else:
    print("Du får inte rösta.")
 """

""" 
x = 15
if x < 10:
    print("x är mindre än 10.")
elif x > 10 and x < 20:
    print("x är större än 10 men mindre än 20.")
else:
    print("x är större än 20.") """

""" 
age = 17
driving_license = False

if age >= 18 and driving_license:
    print("Du får köra bil.")
else:
    print("Du får inte köra bil.") """


### Uppgift 8.
#Skriv en if-sats som skriver ut "Du får köra bil." om variablerna age är större än eller lika med 18 och driving_license är True. I alla andra fall ska det skrivas ut "Du får inte köra bil.".

""" age= 15

driving_license= True

if age >= 18 and driving_license:
    print("du får köra bil")
else:
    print("du får inte köra bil")    
 """


#Skriv en kodsnutt som frågar användaren om deras ålder och skriver ut om de är tillräckligt gamla för att ta körkort (åldersgränsen är 18 år).

""" 
age = int(input("how old are you? "))

if age >= 18:
    print("you have the right to  drive a car")
else:
    print("you can not drive the car")      """



#Skriv en kodsnutt som frågar användaren om de gillar choklad eller glass
#(användaren svarar med "choklad", "glass" eller "båda") och skriver ut 
#"Du gillar choklad!", "Du gillar glass!" eller "Du gillar både choklad och glass!"
#beroende på svaret.


""" 
answer= input("gillar du choklad eller glass")

if answer == "choklad":
    print("Du gillar choklad!")

elif answer == "glass":
    print("Du gillar glass!")

elif answer == "båda":
    print("Du gillar både choklad och glass!")
 """



""" 

if 50 == 40 and 50 == 50:
   print("Does 50 == 50 ever get evaluated?")

if 50 == 40 or 50 == 50:
   print("Does 50 == 50 ever get evaluated?(50 == 40 or 50 == 50)")   ### yes it gets evaluated in or statement because one of the conditions is true

 """



""" x = 20
if not x == 10 or x == 20:
    print("Villkoret är uppfyllt.")   ## vilkoret är uppfylt eftersom not x == 10 is true or x == 20 is true i dettta fall är båda conditions true en de hade bara behövts en för att trigga print sataemnt
else:
    print("Villkoret är inte uppfyllt.")  
 """

##  Vad är skillnaden på en comparison-operator och en conditional? Beskriv hur de används tillsammans, både med ord och kod.

## compariosn operator coprased 2 values returns a true or false value , conditional operators like if elif and else will be triggered based on the boolan return value based on the comparsion operatos


""" age= 25 

test_passed = True 

if age > 25 and test_passed:  ## comparison operator 
    print("you can now apply for masters")
else:   ## conditional operator 
    print("you are not eligabe to apply for masters course")     """



import random
#1. Vad gör import-ordet?

##import word acesses random module  which is a library not stored locally ,via imporintg random module we can acess claases  and methods for .ex and randint() will generates random value withan i numeric range .



""" 
first_value = 2 

second_value = -2




print(abs(first_value - second_value)) """