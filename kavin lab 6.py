'''#1.take your name as input and print it in uppercase
a="kavinkumar"
print(a.upper())

#take a sentence and convert it into lowercase
b="you can do it"
print(b.lower())

#Enter a sentence and print it with the first letter capitalized.
c="title"
print(c.capitalize())

#use format() to display your name and age in a sentence
name="kavinkumar"
age=18
print("my name is {}and I am {} years old.".format(name,age))

#find the index of a given character in a word.
d="try your best"
print(d.index('o'))
print(d.index('y'))
print(d.index('t'))

#find the position of a substring in a sentence using find().

sentence="python is easy to learn"
substring="1"

position=sentence.find(substring)

print("position:",position)

#check  if a word ends with "ing" using endswith()

e=input("Enter a word:")

if e.endswith("ing"):
    print("the word end with 'ing'.")
else:
    print("the word does not end with 'ing'.")

#print a string with tabs (\t) and then use expandtabs()to show spaces

text = "name\tof\tthe company"
print("Original string:")
print(text)
print("After expandtabs():")
print(text.expandtabs())

#9.
e="kavinkumar!"
f=e.encode("utf-8")
print(f)

#10.
g=input("Enter a string:")

if g.isdigit():
    print("the string contain only digits.")
else:
    print("the string does not contain only digitals.")

#11.
h=input("Enter a string:")

if h.isnumeric():
    print("the string is numeric.")
else:
    print("the string is not numeric.")

#12.
i=input("Enter a string:")

if i.isalnum():
    print("the string is isalnum.")

else:
    print("the string is not isalnum.")

#13.

j=input("Enter a string:")

if j.isascii():
    print("the string contains only ASCII characters.")
else:
    print("the string contains non-ASCII characters.")'''

#14.

k= input("Enter a string:")

if k.isalpha():
    print("the string is isalpha.")
else:
    print("the string is not isalpha.")




