numbers =[1,2,3]
new_numbers= [n+1 for n in numbers]

name ="Antonela"
letters_list = [letter for letter in name]

#python sequence- bc they have an order
#list, string, tuple, range

new_list = [n*2 for n in range(1,5)]
print(new_list)

#CONDITIONAL LIST COMPREHENSION
names = ['Alex', 'Nela', 'Ria', 'Antonela', 'Glei', 'Woohaa', 'Visi', 'Andrea']
#only names 4 letters and less
short_names = [name for name in names if len(name)< 5]
print(short_names)

#capitalize each of names who are 5 letters and more
long_names = [name.upper() for name in names if len(name)> 5]
print(long_names)