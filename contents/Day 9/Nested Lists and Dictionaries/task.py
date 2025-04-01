# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Italy": ["Venice", "Roma", "Verona"]
# }

#print(travel_log["France"][1])


#nested_list

nested_list=["A", "B",["C", "D"]]

print(nested_list[2][0])


#nested dict

travel_log = {
     "France": {
         "num_times_visited": 8,
         "cities_visited":["Paris", "Lille", "Dijon"]
     },
     "italy": {
         "num_times_visited": 5,
         "cities_visited":["Venice", "Roma", "Verona"]
     }
}

print(travel_log["France"]["cities_visited"][2]) #to print dijon