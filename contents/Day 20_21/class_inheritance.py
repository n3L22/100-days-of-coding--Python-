#How can we inheritance

class Animal:
    #attribute
    def __init__(self):
        self.num_eyes =2
        
    #method
    def breathe(self):
        print("inhale, exhale")
        
        
      #fish is inheriting from animal class
class Fish(Animal):
    def __init__(self):
        #super will initialise everything that our superclass will do 
        super().__init__()
        
    #if we want to modify something that we inherited 
    def breathe(self):
        super().breathe()
        print("im doing this underwater")
    
    def swim(self):
        print("moving in water")
    
nemo = Fish()

nemo.swim()
#now with fish class you can also use breathe
nemo.breathe()