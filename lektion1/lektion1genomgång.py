## reassigning value 
## primitive datatypes 


""" first_variable= 500000  # heltal 

print(id(first_variable))

second_variable=10000000000
first_variable = second_variable

print(id(second_variable))

 """

# reassinging values id location 

""" first_variable= 500000   
print(id(first_variable))

second_variable=10000000000

first_variable =second_variable
print(id(first_variable))


sum_of_values= first_variable + second_variable

print(id(sum_of_values))
 """

""" prevoius_num=0
current_number = 0

sum=0


for i in range(10):
    

    sum=current_number +prevoius_num

    
    print(f"current number {current_number} Prevoius number {prevoius_num} Sum: {sum} " )
    current_number = current_number +1 
    prevoius_num=current_number-1 """
""" 
number1 = 40
number2 = 30

product = number1 * number2 
sum = number1 + number2 

if(product <= 1000):
    print(product)
else:
    print(sum)
 """


""" 

##checking if the naumbers are same based on index position in a list of numbers
def SameOrNot(numbers1):
    if(numbers1[0] == numbers1 [-1]):
        return True 
    else:
        False
      




numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

SameOrNot(numbers_x)

print(SameOrNot(numbers_x)) """

# for lists we do not use for i in range rather we use this which means each wi iterate each  elemnt in nums once via num keyword 
""" def devisibleBy5(nums):
    for num in nums:
        if num % 5 == 0:
            print(num)

        


nums= [10, 20, 33, 46, 55]

devisibleBy5(nums)

 """
#count how many times a substring is repeated in a text


""" str_x = "Emma is good developer. Emma is a writer" 

spilt_words = str_x.split(" ")

count= 0

for word in spilt_words:
    if word == "Emma":
        count = count +1
print(f"Emma appeared {count} times")            
 """


""" for i in range(1, 6):
    print(f"{i} "* i) """

""" def pass_fail(score):
    if score >= 50:
        print(f"you got {score} marks, you passed!!")
    else:
        print(f"you got {score} marks, you failed")



pass_fail(70) """


print(bool("hi"))