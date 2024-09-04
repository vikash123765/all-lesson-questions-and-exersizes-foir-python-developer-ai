

""" 
def multiply(*nums):  ## we can pass miltiple nums as a tuple
    total=1  ## create a total count with start if 1 as we cannot start at 0

    for num in nums:   ## loop trough each values 
        total = total *num   ## perform mulitply operation 
    return total


result=multiply(2,3,4,5)

print(result) """


## to pass multiple key value pairs to an function we use ** 

""" def user_save(**user):
    print(user["id"])   ## we create an dict 


user_save(name="vikash",age=21,id=2343)

 """
## scope= local and global, if local variable is only accessable inside a function 
##if global variable is acessable outside function and can be acessed by mulyiple functions 

##

""" def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
       return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
  
    else:
        return num 





print(fizz_buzz(7))
     """

""" 
def first_last_name_capitalize(first,last):
    first= first.capitalize()  ## will capitalize the first letter in the name  
    last=last.capitalize()
    return first+ " " +last


print(first_last_name_capitalize("vikash","kosaraju")) """

## defult arguments

""" 
def net_price(list_price,discount,tax=0.2): ## we can assign default v alue to parmeter argument which will be used if all argumnets required from caller is not passed 
    return list_price * (1 - discount) * (1+tax)


##net_price(500,0.1,0.2)   ## here we pass 3 arguments 

net_price(500,0.1)   ## incase we dont pass 3 arguments   
 """
""" import time 
def count(stop,start=0,): ## onstead we can pass start as a default value 
    for x in range(start,stop+1):
        print(x)
        time.sleep(1)
    print("Done")    


count(23,1) """
        


## keyword arguments = an argument proceeded by its identifier mske it so position of the argument does not matther 

""" def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

phone_num= get_phone(area=23,country=46,last=2346,first=345)  ## here we dont have to pass arument in positional synchronisity instead we specify what value shoul be assigned to what variable does not need to positional

print(phone_num)

 """


## dicts = ordered and changable, no duplicates need uniwe key identifier

country_captitals= {"germany":"berlin","sweden":"stockholm","india":"mumbai"}


""" if country_captitals.get("germany"):
    print("that capital exists")
else:
    print("that capital does not exist") """

""" 
country_captitals.update({"Burma":"laos"})
print(country_captitals)

country_captitals.update({"Burma":"Naypyidaw"})
print(country_captitals)


country_captitals.pop("Burma")
print(country_captitals)

country_captitals.popitem() ## will remove the latest key value pair 


 """
""" for city in country_captitals.values():
    print(city)


for country in country_captitals.keys():
    print(country)



 """


items = country_captitals.items()
print(items)

for key,value in country_captitals.items():
    print(f"{key} = {value}")