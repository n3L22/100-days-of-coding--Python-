names = ['Alex', 'Nela', 'Ria', 'Antonela', 'Glei', 'Woohaa', 'Visi', 'Andrea']

#to create a dictionary with student score randomly
import random 
students_score = {student:random.randint(1,100) for student in names}
print(students_score)

#create a dictionary that only adds the passed students 
passed_students = {student:score for (student,score) in students_score.items() if score > 60}
print(passed_students)

#convert to farenheits 
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {days:(temp_c * 9/5) + 32 for (days,temp_c) in weather_c.items()}
print(weather_f)


#looping through a dictionary 
students_dict= {
    "student": ["Glei", "James", "Antonela"],
    "score":[56,76,98]
}

#Looping through the dictionary 
for (key,value) in students_dict.items():
    print(value)
    
#looping through a dataframe 
import pandas 
student_data_frame = pandas.DataFrame(students_dict)
print(student_data_frame)

#loop through a data frame is the same as dict but this is not good
for (key,value) in student_data_frame.items():
    print(value)
    
#for dataframe we use a built-in loop through
#which allows us to loop through rows of a dataframe
# index => corresponds to the number along the data 
# row==> get hold of the data, each of the rows is a panda series
#to get hold of a column inside that row
for (index,row) in student_data_frame.iterrows():
    print(row.student) #or print(row.score) or print(row)
    
#what we can also do is:
for (index,row) in student_data_frame.iterrows():
    if row.student == "Antonela":
        print(row.score)
        
        
#for dataframe comprehension
#passed_students = {new_key:new_value for (index,value) in df.iterrows()}