## a dictonary is key value pairs inside and curcly brace bracket where each pair is seaprated by comas
## in lists we use index position to acess value but in dicts we use the uniqe key 

country_captitals= {"germany":"berlin","sweden":"stockholm","india":"mumbai"}

#print(country_captitals)

##print(country_captitals["germany"])  ## we acess the value with the key 


## add items to dictoinary 
country_captitals["Italy"] = "Naples"   ## this is how we add entries to dict

##print(country_captitals)

##delete an entry via the key
##del country_captitals["germany"]  
##country_captitals.clear() ## will rmeove all entries 



##change dictinary items 
#country_captitals["Italy"] = "Rome"  ## via the key we can actually assign new value to the pair


## iterate trough dictionaries

""" for country in country_captitals:  ## to print keys one by one 
    print(country)  

for capital in country_captitals:
    value=  country_captitals[capital]  ## to print value one by one 
    print(value)
 """



## find dicts lenght  
""" print(len(country_captitals))
 """

## few useful methods for dict 

#country_captitals.pop("Italy")  ## removesan item with specified key 
#country_captitals.update(["Italy"] ="Rome")
#print(country_captitals.keys()) ## returns all thw keys in the dict 
#print(country_captitals.values())  ## returns all the values in dict 
#(country_captitals.get("Italy"))  ## return a value of specific key 
#print(country_captitals) 
##country_captitals.popitem() ## remove last inserted key an value as a tuple
#countries_and_city=country_captitals.copy() ## return a coopy of the dictionary 
#print(countries_and_city)



## We can check if a key exists in a dict with in or not in operators 
""" 
print("italy" in country_captitals)
print("Italy" in country_captitals)
print("italy" not in country_captitals) """


#Assignment


""" def merged_dicts(d1,d2):
    new_dict={}
    new_dict.update(d1)
    new_dict.update(d2)
    return new_dict


d1={"Sweden":"stockholm","italy":"Rome","India":"Munbai"}
d2={"Rusiia":"moskov","china":"juansingd","Spain":"madrid"}
print(merged_dicts(d1,d2))
 """

## video examples 
person1= {"name":"vikash","age":21}
""" 
##print(person1.get("hobbies", ["dancing","fishing"]))  ## if the key does not exist create an default value do not completly understand this keep this on ice 

person1["hobbies"] = ["dancing","fishing"] ## adding entrie with key hobbies and value of list dancing and fishing 
print(person1)


person1.pop("name")

print(person1) """


## print key and value 
""" for key in person1:
    print(key)
    print(person1[key]) """

## tessting dict functionality 
synonyms={"mountain":"peak","forest":"jungle"}

print("1,", synonyms["mountain"]) ## will priont peak 

synonyms["terrain"] = "land"
print("2.",synonyms)     ## will add this key value pair after forest:jungle

synonyms.pop("forest") # will remove forest:jungle key pair and display the rest now terrain land will be at last position 
print("3.",synonyms )