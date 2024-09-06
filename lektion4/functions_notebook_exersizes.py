# # Assignment

# Create a function called "register_user" that takes a username as a parameter

# Check if the username is longer than 10 characters
# - If it's longer, print("Username XYZ is too long")
# - If it's good, print("Success")
""" 
def word_more_then_10(username):
    if len(username)< 10:
        return "sucess"
    else:
        return f"{username} is too long"




username= input("please eneter a name ")
print(word_more_then_10(username))

 """



## Assignment - easy
# Write a function that returns the first Swedish letter it finds in a string (parameter).
# Otherwise, return None.



## find first swedish first  letter  and return it 
""" 
def find_first_swedish_letter(word):
    for letter in word:
        if letter in "åäö":
            return letter 
    else:                      ## need to put else outside of the loop as it will check the first letter and if there is no letter matching the first swedeish letter it will jump to else vblock  and stop the iterations
        return None
        
user_input= input("please enter a word with swidish letters")


print(find_first_swedish_letter(user_input))
 """




## Assignment - intermediary
# Imagine you are a moderator on a forum like reddit.
# Write a function that takes a word and checks if it includes curse-words, and replaces those words with stars *****
# Bonus: Try to add as many stars as the length of the word

# the function:
# - takes a string as a parameter
# - takes a list of curse-words as a second parameter



""" def replace_curse_words(words,curse_words,):
    replaced_words=[]     ## create an empty list  to place the repaced words
    for word in words:   ## iterate ech word in list curse_words
        if word.lower() in curse_words:   ## check if word is in the example curses
            replaced_words.append ("*" * len(word))   ## if there is an match append to empty list replacing letters with asterisk with  the len of the current word 
            ##we can use replace function word.replace(word, "atersik")
        else:
            replaced_words.append(word)    ## or just append word as is 

    return replaced_words   ## reurn empty list after complete for loop is done 


curse_words = ["crap", "idiot", "shit"]

words = ["crap", "idiot", "sh*t"]

print(replace_curse_words(words,curse_words))  

 """

# Modify this function to use default values for whatever variables you think is reasonable.
# - The users can only choose between status public, private or locked
# - The users can only choose between light and dark mode
# - Any user might be used in the function

""" def set_profile_visibility(user, status="public", theme="light"):
    return f"{user}'s profile is now {status}. Using the {theme} theme."

#print(set_profile_visibility("Alice", "public",))
#print(set_profile_visibility("Bob", "private"))

print(set_profile_visibility("Bob"))   ## will use default paramter values

print(set_profile_visibility("vikash","private"))  ## will owerride default paramters because we are providing input


print(set_profile_visibility("vikash","private","dark")) ## will owerride default paramters because we are providing input

 """


 ## extra questions 




# Add a function named list_benefits() that returns the following list of strings: "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Add a function named build_sentence(info) which receives a single argument containing a string and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"

# Run and see all the functions work together!


# Modify this function to return a list of strings as defined above
def list_benefits():
    
    return ["More organized code","More readable code","Easier code reuse"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(list_of_benefits):

    list =[]
    for value in list_of_benefits:
        new_value= value + "is a benefit of functions!"
        list.append(new_value)

    
    return list

def name_the_benefits_of_functions():
    benefits_list = list_benefits()
    added_list =build_sentence(benefits_list)

    for item in added_list:
        print(item)

    print("Allowing programmers to share and connect code together is a benefit of functions!")



name_the_benefits_of_functions()



# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", 
            "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return benefit + " is a benefit of functions!"

# Use both functions together
def name_the_benefits_of_functions():
    benefits_list = list_benefits()
    
    # For each benefit, build the sentence and print it
    for benefit in benefits_list:
        print(build_sentence(benefit))

# Run the main function
name_the_benefits_of_functions()






