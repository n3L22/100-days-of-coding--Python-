from art import image

print(image)
bid_dict= {}
bid = True 
while bid:
    name = input("Please enter your name: ")
    bid = input("Please put the bid price: £")
    bid_dict[name]= bid
    
    while True:  # Add an inner loop for validating the choice
        choice = input("Is there any other bidders? Type 'yes' or 'no'\n").lower()
        
        if choice == "yes":
            print('\n' * 100)
            break  # Break the inner loop and continue with the outer loop
        
        elif choice == "no": 
            bid = False
            highest = max(bid_dict, key=bid_dict.get)
            print("The winner is: "+ highest + " with the value £" +bid_dict[highest])
            break  # Break the inner loop
        
        else:
            print("There is a 'typo' try to only type yes or no!")
        
    
    


