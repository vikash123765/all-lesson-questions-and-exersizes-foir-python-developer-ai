
## EXAMPLE CODE 


##You have $20,000 in sales the first month, 5% growth each month. What will your sales be for each of the next 12 months?

""" sales = 20000
growth_rate = 0.05

for month in range(1, 13):
    print(f"Projected sales for month {month}: ${sales:.2f}")
    sales= sales  *  (1+growth_rate)    ## here the 1 represents original sales (100%) + the growth rate in each iteration 


    


 """
""" 
##calculate the area of side 
for side in range(1, 11):
    area = side * side
    print(f"Area of square with side {side} is {area}") """

""" import time
 
for i in range(3):   ## will iterate 3 times 
    print(f"Updating...attempt: {i}")  ## i is orinting the current index 
    time.sleep(3)  ## will wait 3 secionds until the next iteration via time.sleep(whatver time) """

""" 
import time

loop_count = 0
loop_max_count = 3

while loop_count < loop_max_count:
    print(f"Updating...loop_count: {loop_count}")
    time.sleep(1)
    loop_count += 1
 """


##ASSIGNMENTS 


# 1. Use `input()` to ask the user how many times they want to loop.
# 2. Create a `for` loop and utilize `range()` to specify the number of iterations (loops) you want to perform.
# 3. Print "This is the XYZ loop" for each iteration, where "XYZ" represents the current loop index.
""" 
user_input=int(input("how many times you want to loop ? :"))

for i in range(user_input):
    print(f"this is the {i} loop")

 """


#- Create a list of people, add some duplicates values
#- Ask the user to input a name 
#Iterate over the list and print "Found {name}!" when you find the name they input. Since there are some duplicates it might print it multiple times.

""" names = ["tobias", "andreas", "tove","andreas"]

user_input= input("please eneter a name :")

for name in names:
    if user_input in name:
        print("found")
 """


#Write a loop that counts how many words in the list are longer than the variable "length."Then, print the result after the loop is finished.

""" words = ["Python", "is", "amazing", "Guido Van Rossum"]

lenght= 3
count =0

for word in words:
      if len(word)> lenght:
          count += 1 

        
print(f"there are {count} words thats is longer then variable lenght ")  
 """

##Once again, create a list of names and ask the user to input a name.
#  Iterate over the list, and print "Found {name} at the position {index}".
# You need to use enumerate() to have access to the index AND the value of each element
""" 

names = ["tobias", "andreas", "tove","andreas"]

user_input= input("please eneter a name :")


for index,name in enumerate(names):
    if user_input in name:
        print(f"{index} {name}")

 """



## find the longest word an print it 

""" words = ["Python", "Java", "C", "JavaScript"] 

longest_word =""

for word in words:
      if len(word)> len(longest_word):
          longest_word = word

print(f"the longest word is{longest_word}")
 """


##  
""" 
words = ["Python", "Java", "C", "JavaScript"]
user_word = input("Choose a word and check if it exists in any of the words in the list")

for word in words:
    if user_word in words:
        print(f' "{user_word }" is found in the word "{word}"')
    
 """

## slices, subset of lists... 
""" 

first_list = [1,2,3,4,5]
 
new_slice = first_list[:3]     ## will start from index 0 to index 3  it will stop at 3
  
print(new_slice) """



""" first_list = ["tobias", "marcus", "andreas", "linda"]
new_slice = first_list[2:4]   ## will start from index 2 to 4  will print andreas and linda

print(new_slice) """



""" first_list = ["tobias", "marcus", "andreas", "linda","vikash","johan"]


print(first_list[4])



new_slice = first_list[0:5:2]  ## will start from index 0 step 2 each tiume it print  and stop at index 4, so output will be tobia and andreas (tip in the stop value count as if index starts from 1 and not 0 because stop value is not included anyhow)
print(new_slice)
print """



""" first_list = ["tobias", "marcus", "andreas", "linda"]

# Only using a colon means we want everything from the beginning to the end
# This will create a copy of the list
new_slice = first_list[:]

new_slice[0] = "johan"   ## assigning the value johan to index position 0 to the new opied list 
print(first_list)
print(new_slice)  """