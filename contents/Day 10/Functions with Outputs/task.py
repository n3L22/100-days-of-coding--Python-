def format_name(name, surname):
    f_name = name.capitalize()
    f_sname = surname.capitalize()
    return (f_name, f_sname)

    
#with return we can store it in a variable 
print(format_name("ANTONELA", "RAKIPAJ"))


#or 
store_it_here = format_name("ANTONELA", "RAKIPAJ")
print(store_it_here)

#to assign a function into a variable
variable_name = format_name #make sure you dont have the parenthesis 

#why is this useful --> for example we want to use a function inside a function 
def function_1(text):
    return text+text
#put it as a variable to continue do something else
def function_2(text):
    return text.title()

output = function_2(function_1("Hello"))

#it will concate first and also make it capitalise from function 2
print(output)