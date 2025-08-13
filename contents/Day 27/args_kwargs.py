'''  *ARGS  '''
def add(*pafund):
    #if you want to see the first arg 
    #print(pafund[0])
    sum = 0 
    for i in pafund:
        sum += i
    print(sum)
#now add as many args as you want to.
add(1,2,3,4,5)

#these args are also known as positional arguments 

#usually we have **arg ang **kwarg (key word arguments) to put inside methods for example
#a kwarg:
''' key word argument are when you actually call them in methods write(text="what do you write)'''

#an arg:
'''when a method is arg it means that you only have to put that others will be default '''


#to make unlimited number of arguments we can simply use *args
def add(*args):
    for n in args:
        print(n)


'''  **KWARGS  '''
#these are stored as dictionary
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
        
    #lets say i want to do some add and multiply 
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply =5)

#that is why in tkinter you do the other keywords 
#whatever you want bc every method is a kwarg

''' One example is:'''

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        #to avoid the crash if one is deleted we use the method below:
        #the diff with get is that if this doesnt exist in dict it wont give us any error
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seat = kw.get("seat")
        
#if we delete one of these it will crash 
my_car = Car(make="Nissan", model="GT-5" )
print(my_car.make)