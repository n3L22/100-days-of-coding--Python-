#after the return keyword nothing on the other lines will be executed
def format_name(name, surname):
    if name == "" or surname == "":
        return "You have to input something"
    f_name = name.capitalize()
    f_sname = surname.capitalize()
    
    return (f"{f_name} {f_sname}")

print(format_name(input("What is your first name: "), input("What is your last name: ")))




#another way to do functions 
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)