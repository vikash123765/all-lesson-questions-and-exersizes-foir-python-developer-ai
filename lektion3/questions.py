

##1

""" words = ["Python", "is", "amazing", "Guido Van Rossum"]

lenght= 3
count =0

for word in words:
      if len(word)> lenght:
          count += 1 

        
print(f"there are {count} words thats is longer then variable lenght ")  
 """

##2

""" words = ["Python", "Java", "C", "JavaScript"] 

longest_word =""

for word in words:
      if len(word)> len(longest_word):
          longest_word = word

print(f"the longest word is{longest_word}")
 """


##3 
""" 
words = ["Python", "Java", "C", "JavaScript"]
user_word = input("Choose a word and check if it exists in any of the words in the list")

for word in words:
    if user_word in words:
        print(f' "{user_word }" is found in the word "{word}"')
    
 """


##4 
""" threshold = 6



def sum_of_num_abv_threshold(numbers,total_sum):
    for num in numbers:
        if num > threshold:
            total_sum += num
    return total_sum        


total_sum = 0

numbers = [5, 12, 8, 3, 7, 18, 4]


print(sum_of_num_abv_threshold(numbers,total_sum))

 """



## 5
""" 
students = ["Tobias", "Andreas", "Lisa"]

while True: 
    print("press q to exit program")
    print("press[0] to display students")
    print("press[1] to serach for student")
    print("press[2] to remove a student")


    user_shoise = input()

    if user_shoise == "q":
        break
    elif user_shoise == "0":
        for student in students:
           print(student)
        inner_chose= input("press q to go back or enter to continue")
        if inner_chose == "q":
            break
        else:
            continue   

    elif user_shoise == "1":
        student_name= input("search for student name")
        for student in students:
            if student_name in students:
                print(f" this is the student you serached for{student_name}")  
                remove_or_not = input("do you want to remove the student? Y/N ")
                if remove_or_not =="Y":
                    students.remove(student)
                    continue
                elif remove_or_not =="N":
                    break
                    

            

            
            elif student_name not in students:
                print(f"{student_name} does not exissts")  ## why is this getting triggered regardless of the return  value      
    else:
        print("invalid input please try again ")
       """

        

## fråga 1 av notbook övingarna 
""" value = 0
 
while value < 10 :
    value += 1
    print(value)       

 """

## 2

""" word = "python"

for char in word:
    print(char, end= " ") """

## 3 Skriv en for-loop som summerar talen från 1 till 100 med hjälp av range()
""" 
total_sum = 0

for i in range(100+1):
    total_sum += i

print(total_sum)

 """


## 4 Skriv en for-loop som räknar antalet bokstäver i en string som användaren får välja. Räkna sedan hur många svenska bokstäver som förekommer, dvs. "å, ä, ö".
##Du kommer behöva att kombinera loopen med en if-statement.

""" word = input("please write an word")

counter_swedish_char =0

counter_char_in_word= 0

swedish_letter = "åäö"

for char in word:
     counter_char_in_word = len(word) 
     if  char in swedish_letter: ## if char is in swedish lettrs, (each iteration will go trough each characater) for every matching iteration 
          counter_swedish_char +=1  ## increase counter by one represtning matches 

          
           

print(f"{counter_char_in_word}   and {counter_swedish_char}")

 """
 
## 5.) 1. Skriv ett program som använder en loop och enumerate() för att hitta positionen för ett visst element i en lista. Fråga användaren efter ett element, tex. "a" och printa sedan ut vilken position det är.
##   2. Avbryt programmet loopen om den hittar elementet med hjälp av break-keywordet


""" cars = ["audi","bmw","mustang","masarati"]

while 1 == 1:    
    

    for index,car in enumerate(cars):
        print(car)
    choosen_car = input("please choose a car: ") 


    if choosen_car not in cars:
        print("that car does not exist in list")
        continue
    elif cars.index(choosen_car) > 0 or cars.index(choosen_car) < len(cars) :
        print(f"the index of {choosen_car} is {cars.index(choosen_car)}")
        break

    else:
        print("invslid input please try again ")   
 """


## 6 Vad är skillnaden mellan while och for? Varför skulle jag vilja använda en forloop när jag oftast kan göra samma sak med en whileloop?

##while lope is to perform an operation infinite amount of times until condition is met 

""" secret_num = 6

guessed_num = int(input("please guess a num"))


while 1 == 1 :
    if guessed_num == secret_num:
        print(f"you guessed correct: my secret num is {secret_num}, and you guessed {guessed_num} ")
        break
    else:
        print(f"you guessed incorrect, you guessed {guessed_num} ")
        guessed_num= int(input("please guess again ! : ")) """


## 6 .) for loop is to perform either an iteration a set number of times or iteration of elements,char,numerical values in  alist/string and so on . 
"""
name = "vikash"

 for letter in name:
    print(letter, end= "") """   ## iterating over charactaers in string or elements in list or  numbers 

""" 
for i in range(10):    ## doing opertion a set number of times 
    print(i,name)
    
 """


## 7.) ### **Uppgift 7.**
##Ponera att du har en lista med 10000 string-elements i sig (tex. addresser). Du inser att det inte är nödvändigt att behålla addresser med ordet "Katrineholm" i sig och du bestämmer dig för att skriva denna kod:

""" 
addresses = ["Sultangatan 15, Katrineholm", "Hotellgatan 12, Stockholm"]
print(addresses)

for index, address in enumerate(addresses):
   if "Katrineholm" in address:
       addresses.pop(index) # remove the item using its index
       print(addresses) 

 


addresses = ["Sultangatan 15, Katrineholm", "Hotellgatan 12, Stockholm"]  ## my take on it this does not work as we chnage the list index positions when we modify list while iterating over it this causing unexpected behavior
print(addresses)


for index,adrees in enumerate(addresses):
   if adrees in "Katrineholm":
    addresses.pop(adrees)
print(addresses)  



addresses = ["Sultangatan 15, Katrineholm", "Hotellgatan 12, Stockholm"]  ## inseted we need to remove element with index and pop function if we want to modify list while iterating an expect intended outcome 
print(addresses) 


for index,adress in enumerate(addresses):
   if "Katrineholm" in adress:
      addresses.pop(index)
      print(addresses) 

"""
""" 
## 8.) ### **Uppgift 8.**
#1. Hur skapar du en lista?
#2. Varför behöver vi listor? 
#3. Vad är ett index? Svara med kod och ord.
#4. Vad är ett element? Svara med kod och ord.
#5. Kan vi stoppa vilka typer som helst i en lista? Pröva!

##1 creating a list 
phones = ["samsung", "iphone", "Lg"]

##2 why we need lists ? to store multiple values or strings in a single variable 
phones = ["samsung", "iphone", "Lg"] 

##3 index is a position of the element starting from 0 and incrimenting with one by each elemnt
##print(phones[2])  ## will print lg as its index position is 2 

##4 element is an value in the list or an entry whataver you want to call it entrie is more often used for complexe object and values or simple structure 
phones = ["samsung", "iphone", "Lg"]  ## any of theese phone models are elements 

#5 we can have multiple databays insreted in a list 
phones = ["samsung",23,True,]  ## we have an string value, we have an numerical value and we have an bool value
 


 """


## 9 ### **Uppgift 9.**
# Du har listan 
#numbers = [1,2,3,4,5]
# 1.  Hur printar du ut första elementet i listan? Svara med kod.
# 2. Hur printar du ut sista elementet? Tips: Du kan använda len()-funktionen eller ett annat sätt som är mer typiskt för python. Svara med kod.
# 3. Jag vill lägga till ett element på slutet av listan, hur gör jag? Svara med kod.
# 4. Jag ångrar mig! Jag vill nu ta bort det sista elementet. Svara med kod.

""" #1 
print(numbers[0])
#2
print(numbers[-1])
#3
numbers.append(6)
print(numbers)
#4
numbers.pop()    ## will remove last element 
print(numbers)

# 5. Ta bort elementet på index 2. Svara med kod
for index,num in enumerate(numbers):
    if index == 2:
        numbers.pop(index)
        print(numbers) 

 """

#Du nu istället  listan 
""" names = ["tobias","martin","anna","li",]
print(names) """

# 6. Låtsas som att du inte har någon aning om vilka element som finns i listan, du vet alltså inte vilken plats (index) exempelvis namnet "martin" ligger på. Hur tar du bort "martin" från listan?

""" names.remove("martin")
print(names) """


# det finns det 2 st martin. Funkar det att endast köra remove?
""" names = ["tobias","martin","anna","li","martin"]
print(names)

for index,name in enumerate(names):    ## vi kör en enumarte loop och tar bort lla occurenies av martin via index och functin pop 
    if name == "martin":
        names.pop(index)
print(names)
      
    """


##10Ge ett exempel med helst kod och ord hur du kan använda break-keywordet och continue-keywordet inom loopar.

""" for i in range(10):
    if i == 8:     ## will break loop at index 8 
        break
    elif i ==2:
        continue    ## will skip/continue over index 2 
    print(i)     
       """


##11Du har en lista av listor med nummer. Din uppgift är att skriva en kod som går igenom varje tal i varje lista. Om talet är jämnt ska du lägga till det i en ny lista.
# Denna uppgift bygger på att du ska arbeta med "nestade" listor. Det är väldigt ofta vi kan behöva loopa igenom en datastruktur, sedan loopa igenom varje element 
# (för elementen är också listor!).
""" even_numbers = []
num_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

for list in num_lists:
    for num in list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            continue
print(even_numbers, end="")            

 """

## 12### **Uppgift 12.**

# Nu ska du få öva på att jobba med slices. En slice är ett sätt att kopiera en lista där du kan specificera vilka element som ska inkluderas. Du vet att det är en slice så fort du upptäcker kolon i en lista, tex. [:], [0:5], [0:5:1] osv!

# 1. Vad gör denna kod?
""" 
data = ["tobias", "marcus", 1, 5.0]    ## will start from index 2 until last index 
#l = data[2:]
print(data[2:]) """

# 2. Vad gör denna kod?
""" 
data = ["tobias", "marcus", 1, 5.0,"somethign","somethign 2"]
print(data[:5])        ## will stop at index 5 from first index  """
 

# 3. Vad gör denna kod? Vad betyder minussiffran?
""" 
data = ["tobias", "marcus", 1, 5.0]   ## 2ill print each eleemtn backwards starting from last index position 
print(data[::-1]) """



##13. Förklara vad "in" gör i denna kod gör. Keywordet används två gånger,vad är skillnaden på dessa två användningsområden?:
""" 
names = ["tobias", "andreas", "tove"]
new_names = []
for name in names:
   if "to" in name:    ## denna iterarear över all ement i listan names och chedkar ifall strängarna to är i name ifall det är(uuprerpar samma handling för alla name in names )
      new_names.append(name)   ## addera det namnet i den nya listan 
print(new_names)      

#2. Förklara vad "in" gör i denna kod gör:

names = ["doctor", "teacher", "programmer"]    
exists = True              ## Sätter esict variablen till true intitellt 
if "programmer" not in names:    ## checkar ifal stränger programmer inte är i listan names 
   exists = False 
print(exists)   ## resultatet kommer ju  true för att programmmer exists in list 




 """
