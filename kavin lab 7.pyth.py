'''#1.dictionaries
#3.

students={"kavin":94,"ruthran":95,"abhi":98,"samith":98}
print(students)

#4.

students={"prathish":95,"kavin":98,"ruthran":99,"abhi":97,"samith":89}
print(student["kavin"])

#5.

students={"prathish":94,"kavin":99,"ruthran":90,"abhi":97,"samith":89}

student["venkat"]=100

print(students)

#6.
students={"kavin":98,"dhanush":97,"samith":97,"ruthran":99,"abhi":100}

top_student=max(students,key=students.get)

print("student with the highest marks:",top_student)
print("marks:",students[top_student])

#7.

students1={"kavin":97,"ruthran":98,"abhi":96}

students2={"samith":89,"prathish":90}

students1.update(dtudents2)

print(students1)

#8.

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

#10.functions:
#12.

def find_length(text):
    return len(text)

string =input("enter a string:")
print("length of the string is:",find_length(string))

#13.

def find _max(numbers):
    return max(numbers)

number=[20,45,7,65,42]

print("maximum value is:",find_max(number))

#14.

def find_min(numbers):
    return min(numbers)

number=[20,45,7,64,53]
print("minimum value is:",find_min(numbers))

#15.

def find_sum(numbers):
    return sum(numbers)
number=[10,20,30,40,50,]

print("sum of the number is:",find_sum(numbers))

#16.

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

num=int(input("Enter a number:"))
print("factorial of",num,"is:",factorial(num))

#17.

def student_details(name,roll,dept):
    print("student name:",name)
    print("roll number:",roll)
    print("department:",dept)

student_details("harish",102,"computer science")

#18.

def calculate_total(marks1,marks2,marks3):
    total=marks1+marks2+marks3
    print("total marks:",total)

calculate_total(67,88,98)

#19.

def rectangle_area(length,width):
    area=length*width
    print("area of the rectangle:",area)

rectangle_area(10,6)

#20.

def greet_user(name,message="good morning"):
    print(message +","+name+"!")
greet_user("ruthran")
greet_user("ruthran","welcome")

#21.

def add_numbers(*args):
    return sum(args)

total=add numbers(10,30,50,70,90)
print("sum:",total)

#22.

def multiply_all(*args):
    result=1
    for num in args:
        result*=num
    return result

product =multiply_all(2,3,4,5)
print("product:",product)'''
    





