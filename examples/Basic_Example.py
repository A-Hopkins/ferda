"""
Basic example showing you all the basics of python.

Created by alex
"""

this_is_a_variable = 9
string = "hello"
str2 = 'hello1'
x = "ahs"

this_is_a_variable = '9'

y = 10
z = 10

a = y + z
a = y / z
a = y ** 2
print(a)

if y == 10:
    y = 5
elif y == 100:
    y = 50
else:
    print("Y isnt a known number")

for i in range(0, 10):
    print(i)
    x = i ** 2
    print(x)

a_list = [9, "string", 'a', 9.8]
b_list = []

for i in range(0, 10):
    x = i ** 2
    b_list.append(x)

print(b_list)

print(b_list[0], b_list[-1])
print(b_list[0:3])

user_input = input("What is your input?\n")

"""
Create a program that asks for the user input and prints out the input letter by letter.
"""
