class User:   
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0
        
    #a method needs to have a self parameter
    def follow(self, user):
        user.followers += 1
        self.following += 1
    
user_1 = User("001", "Antonela")
user_2 =User("002", "Glei")

#      method we created inside class
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)