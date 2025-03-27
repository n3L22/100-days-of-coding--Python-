student_score = [160, 120, 190,167,34,89,90]

#total 
print(sum(student_score))


#max value 
temp = 0
for i in student_score:
    if i > temp:
        temp = i

print(temp)