#FileNotFound
#IndexError
#KeyError
#TypeError

#HANDLING EXCEPTION
#TRY
#--- Something that might cause the prob
#EXCEPT
#--- Do this instead if there is an exception
#ELSE
#---Do this instead if there are no exceptions
#FINALLY 
#---do this no matter what happens

#example with filenotfound error
try:
    file = open(r"100-days-of-coding--Python-\contents\Day 30\a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["fnjenej"])
except FileNotFoundError:
    file = open(r"100-days-of-coding--Python-\contents\Day 30\a_file.txt", "w")
    file.write("Yee")
except KeyError as error_message:
    print(f"This key{error_message}does not exist")
else:
    content= file.read()
    print(content)
finally:
    raise TypeError("i just made this up")
    
#this allows us to raise our own exceptions
#raiseTypeError("i just made this up")