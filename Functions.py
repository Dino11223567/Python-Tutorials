#What is a function?
#Function Calls[edit] A callable object is an object that can accept some arguments 
#(also called parameters) and possibly return an object (often a tuple containing multiple objects)

#Types of functions in python

#Type 1 = Built-in
print("I am a built in function") #Probably the most wideknown function
print(ord('I')) #This prints the ascii value of "I"
print(chr(73)) #This gives the character with the ascii value of 13

#Type 2 = User- Defined
#The Users are able to create their own functions through the use of def

def Tutorial():
    print("Why we are just getting started!")
    
Tutorial()

#User defined function can receive parameters and functions

def Printer (str):
    print(str)

Printer("Oh wow! I am not really different")

#There can be up to multiple parameters inside a function 

def Two (list_name, items):
    list_name = []
    list_name.append(items)
    
#This will allow you to add new things to different lists
#Last but not least, You can have functions within functions

def function_eater(function):
    Tutorial()
    function
function_eater(Printer("HUH"))

    






