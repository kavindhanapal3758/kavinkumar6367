'''#1.lambda tasks
#2.
add=lambda a,b:a+b
print(add(20,30))

#3.
square=lambda x:x**2
print(square(5))

#4.
cube=lambda x:x**3
print(cube(3))

#5.
even _ odd=lambda x:"even" if x % 2==0
else"odd"
print(even_odd(7))

#6.
largest=lambda a,b:a if a>b else b
print(largest(16,38))

#7.filter task

nums=[1,2,3,4,5,6,7,10,-3,-4,-6]

print(list(filter(lambda x:x%2==0,nums)))

print(list(filter(lambda x:x%2!=0,nums)))

print(list(filter(lambda x:x>10,nums)))

print(list(filter(lambda x:x>0,nums)))

prrint(list(filter(lambda x:x % 5==0,nums)))

#13.map tasks.

nums=[1,2,3,4,5]
 
print(list(map(lambda x:x**2,nums)))

print(list(map(lambda x:x*2,nums)))

print(list(map(lambda x:x+5,nums)))

print(list(map(lambda x: x**3,nums)))

print(List(map(lambda x: str(x),nums)))

#19.combined map + filter tasks.

data=[11,12,13,14,15,16,17,18,19,20]

print(list(map(lambda x: x**2,filter(lambda x: x % 2==0,data))))

print(list(map(lambda x: x*2,filter(lambda x:x % 2!=0,data))))

print(list(map(lambda x:x**3,filter(lambda x: x> 5,data))))

print(list(map(lambda x: x+10,filter(lambda x: x > 0,data))))

print(list(map(lambda x: x*2,filter(lambda x:x % 3 ==0,data))))'''      

 
 
