programming_dict = {
    "Bug":"Error in the program from not running as expected",
    "Loop":"The action of doing something over and over"
}
#Different from lists in dictionaries you give a key to find the value
print(programming_dict["Bug"])

#to add to a dict so they are mutable
programming_dict["Function"]="A piece of code that you can call over and over"
print(programming_dict)


#to create an empty dict 
dict_empty ={}

#you can wipe out a dict just by calling it again
programming_dict = {}


#edit an item inside a dict 
#                key                  value
programming_dict["Function"]="a math operation"


#this loop gives you only the keys 
for thing in programming_dict:
    print(thing) #here you get only the keys
    print(programming_dict[thing]) #give you also the values