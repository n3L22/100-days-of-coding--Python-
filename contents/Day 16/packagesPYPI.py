#use PyPI to search for packages on python
from prettytable import PrettyTable

#created a new object 
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])

table.add_column("Type", ["Electric", "Water", "Fire"])

#make sure that attributes are used as f letter for 'field' as a logo when choosing 
#while for methods you have m logos when choosing from class


#     .f logo  it is a attribute so you can just assign it 
table.align = "l"

print(table)