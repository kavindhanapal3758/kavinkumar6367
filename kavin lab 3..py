'''#1.print number from 1 to 10 using for loop.
for i in range (1,101):
    print(i)

#2.print the multiplication table of a number entered by the user.
a=int(input("Enter a:"))   
for i in range(1,9):
    print(i,'x',a,'=',i*a)

#3.print all even number from 1 to 50.
for i in range(1,50):
    if i%2==0:
        print(i)

#4.print the factorial of a number.
n=int(input("enter n:"))
f=1
for i in range (1,n+1):
    f*1
print("factorial:,f")

#5.print the alphabet from A to G
for letter in range(ord('A'), ord('H')):
    print(chr(letter))

#6.print a pattern:
for i in range (1,5):
    for i in range (i):
        print('*',end=" ")
    print()

#7.print odd number from 0 to 20
for i in range(0,21):
    if i % 2 !=0:
        print(i)




        #Hollow Square pattern

n=5

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j ==0 or j ==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#9.print the inverted triangle.
for i in range(6,-1):
    for i in range(i):
        print('+',end=" ")
    print()
# Floyd's Triangle Pattern
n=9
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num +=1
    print()'''    

    
