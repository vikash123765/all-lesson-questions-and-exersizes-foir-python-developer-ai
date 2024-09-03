##  collections a single variable which stores muliple values 
#List = [] orderered and changable
## Set ={unordered and immutable}
##Tuple = () ordered an unchangable


##List 
"""
fruits = ["apple","orange","mango"]

print(dir(fruits)) ## we can find out the methods that we cane use for list 

 print(fruits[0:2]) ## targeting a range of elements 
print(fruits[::2]) ## step i would like every second element
print(fruits[::-1]) ## fruit backward start with last index -1  """

## iteratin over a list of elements 
""" 
for fruit in fruits:
    print(fruit)
 """


## diffrent functions to perfor mwith the lsut 
""" 

print(len(fruits)) ## lenght of fruits list how many elemnts 

print("apple" in fruits) ## if element apple is within fruits 

fruits[0] = "banana"

print(fruits)

fruits.append("pinapple") ## add elemtent in the end of the list 

fruits.remove("apple")  

fruits.insert(0,"kiwi") ## insert specific index

fruits.sort() ## will sort list in alpatheical order 

fruits.revers() ## reverse a list ased on  index 

fruits.clear()

fruits.index("apple") ##will return an index position of apple 

fruits.count("apple") ## how many occurensies of bana in the list  

"""


## Set  we can not change values but we cann addd and remove will mot print base dont he index positin thus unordered
 
""" fruits = {"apple","orange","mango"}

print(fruits)

fruits.add("kiwi")

fruits.remove("apple")

fruits.pop() ## will remove ehatever element is first  

fruits.clear()

print(fruits) """



## Tuple 

fruits = ("apple","orange","mango")

##only 2 methods 
fruits.index("apple") 
fruits.count("orange")




