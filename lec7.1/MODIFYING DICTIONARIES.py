student = {'name': 'Alice' , "age":25, 'grade': "A"}

student['age']=26
student["major"] ="Computer Sciene"
print(student)

del student['grade']
print(student)

remove_major = student.pop("major")
print(remove_major)
print(student)