file = open("100-days-of-coding--Python-\contents\Day 24\my_file.txt")
contents = file.read()
print(contents)
file.close()

#another method which doesn't need closure in case you forget (mostly used)
with open("100-days-of-coding--Python-\contents\Day 24\my_file.txt") as file:
    contents = file.read()
    print(contents)

#to add something you write:
#make mode writing -> 'w' will replace everything with that new text 
#make mode append -> 'a' will append upon the text that was previously existing
with open("100-days-of-coding--Python-\contents\Day 24\my_file.txt", mode='a') as file:
    file.write("New text as i am testing")
    
    
#to create a new file simply use the with open, mode write and it will create it for you 
with open("100-days-of-coding--Python-\contents\Day 24\hmmm_text", mode='w') as file:
    file.write("awesome")
    