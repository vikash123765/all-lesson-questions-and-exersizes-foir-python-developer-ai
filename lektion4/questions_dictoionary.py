### **Uppgift 1**
#Skapa en dictionary med namn student där följande information ska finnas: name är "John", age är 20 och course är "Pythonprogrammering 1". 

#1. Vad returneras om vi skriver student["name"]?
#2. Byt namn till "Erik"
#3. Ta bort keyn "name"
#4. Lägg till keyn "student" och sätt värdet till True
#5. Loopa igenom dictionaryn och printa både key och value, tex. print(f"{value} and {key}")
""" 

students={"name":"John","age":20,"course":"Pythonprogrammering 1"}

print(students["name"]) ## this  will acess the name value via the key name Jhon 

students["name"]="Erik"   ## assining new value to the key name

print(students["name"])  

students.pop("name")

print(students)

students["student"] = True

print(students)

for key,value in students.items():
    print(f"{key} : {value}") """


### **Uppgift 2.** Varför kan du skriva mer explicit och lättolkad kod genom att använda en dictionary istället för en lista?





### **Uppgift 3.** Du har följande lista med dictionaries

#Lägg till samtliga key-value-pairs in i framework-dicten
#Tips: Det finns en metod tillgänglig på dictionaries som hjälper dig


## my solution 
""" framework_collection = [{"Django": 11, "FastAPI": 7, "Flask": 17, "DRF": 23},{"Angular": 22, "Vue": 9, "React": 13}]

frameworks = {} 


for framework_dicts in framework_collection:
    for key,value in framework_dicts.items():
        frameworks[key] = value
    
print(frameworks) """

## gpt solution 
""" framework_collection = [{"Django": 11, "FastAPI": 7, "Flask": 17, "DRF": 23},
                        {"Angular": 22, "Vue": 9, "React": 13}]

frameworks = {}

for framework_dict in framework_collection:
    frameworks.update(framework_dict)  # Använder update() för att lägga till alla key-value-pairs

print(frameworks)

"""




#### **Uppgift 4.** Du jobbar som lärare och undersöker dina students betyg. Du inser att det vore värdefullt att ta fram lite statistik om betygen.
#Tips: Det finns en pythonmodul som passar bra för detta! 
#1. Vad är summan av betygen?
#2. Vad är medelvärdet?
#3.   
""" 
import statistics 
test_grades = {'linda' : 24, 'andreas' : 55, 'karin' : 33, 'aisha': 45, 'simon': 25}

print(sum(test_grades.values()))  ## sum of values

print(sum(test_grades.values())/len(test_grades.values()))  ## median of values

values= list(test_grades.values())  ## make vaues into a list so we can use the median function 

print((statistics.median(values))) ## we pass the list of values into the median fucntion 



 """






### **Uppgift 5.**
#Du har följande dictionary, du behöver rensa bort alla studenter som
#har blivit godkända. 
#1. Hur gör du?
#2. Funkar det att **ändra** värdet på "passed" från tex. True till False?

""" test_grades = {
9210114413 : {"grade": 55, "passed": True},
9010054514 : {"grade": 22, "passed": False},
8504129392 : {"grade": 60, "passed": True},
9201134555 : {"grade": 15, "passed": False},
}



def remove_true_students(test_grades):  ## send original list to parameter 
    new_test_grades = test_grades.copy()  ## make copy of original list 
    keys_to_remove_list={}
    for key,value in new_test_grades.items():  ## 
       if value["passed"] == True:
            keys_to_remove_list[key]=value

    for key,value in keys_to_remove_list.items():
        del new_test_grades[key]

    return new_test_grades


print(remove_true_students(test_grades)) """



#### **Uppgift 6.** Ponera att du har ett register av hela sveriges befolkning (ca 10 miljoner invånare) som vi sparat i en dictionary med personnumret som key och övrig data som value. 

#swedish_ssn_collection = {199105125545: {}...}

#Varför är det ett rimligt val att använda en dictionary istället för exempelvis en list, med avseende på tex. hastighet?

##för att vi inte behöver loopa igenom alla värden itan vi kan dirket fp fram en value om vi specify key 

""" 
Snabbare uppslagning: Dictionaries använder en hash-tabell för att lagra sina nyckel-värde-par, vilket 
gör att uppslagning av ett värde baserat på en nyckel (t.ex. personnummer) är 
i genomsnitt O(1) i tidskomplexitet. Det innebär att vi kan hämta en persons
 information direkt utan att behöva loopa igenom alla poster.

Ingen redundans: Eftersom varje personnummer är unikt, kan vi enkelt 
använda det som nyckel i en dictionary. Om vi istället använde en lista skulle vi behöva loopa
 igenom hela listan för att hitta en specifik person, vilket skulle vara mycket ineffektivt, särskilt
   med ett stort antal poster (t.ex. 10 miljoner invånare).

Lättare att uppdatera: Med en dictionary kan vi enkelt lägga till, 
uppdatera eller ta bort information om en person baserat på deras personnummer 
utan att behöva hantera index eller positioner som vi skulle behöva göra i en lista. """