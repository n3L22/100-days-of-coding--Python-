#creating a class

class User:
    #to initialise a variable (create) self --> object , others after -->  parameters 
    #if you do it like this you will always have an user_id and username required when calling class   
    def __init__(self, user_id, user_name):
        #.id and .name are the attributes you can call later on 
        self.id = user_id
        self.name = user_name
        #for example followers doesnt need to be initialise as they always start from 0 
        self.followers = 0
        print("new user being created ")
        
        
    
    
user_1 = User("001", "Antonela")


print(user_1.name)


# #attributes even without creating inside class try to leave class empty 
# user_1.id = "001"
# user_1.name = "antonela"

