'''#dictionaries
#create a dictionary with 5 students and their marks.

students={"kavin":94,"ruthran":95,"abhi":98,"samith":98}
print(students)

#access and print the marks of a specific student.

students={"prathish":95,"kavin":98,"ruthran":99,"abhi":97,"samith":89}
print(student["kavin"])

#add a new student to the dictionary.

students={"prathish":94,"kavin":99,"ruthran":90,"abhi":97,"samith":89}

student["venkat"]=100

print(students)

#find the student with the highest marks.
students={"kavin":98,"dhanush":97,"samith":97,"ruthran":99,"abhi":100}

top_student=max(students,key=students.get)

print("student with the highest marks:",top_student)
print("marks:",students[top_student])

#merge two dictionaries into one.

students1={"kavin":97,"ruthran":98,"abhi":96}

students2={"samith":89,"prathish":90}

students1.update(dtudents2)

print(students1)'''

#count character frequencies in a string using a dictionary

text= input("Enter a string:")

frequency={}

for char in text:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1


print("character frequencies:")
for char,count in frequency.items():
    print(char,":",count)






