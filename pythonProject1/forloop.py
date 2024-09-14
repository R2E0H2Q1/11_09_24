"""
For loop runs from number "a" to "b", where a parameter can be added to regulate the size
"""
"""Write a forloop to print all odd numbers between 7 and 39, same line"""

for i in range(7, 40):
    if i % 2 != 0:
        print(i, end=" ")

print()

for i in range(7, 40, 2):
    print(i, end=" ")

print()
"""Write a forloop to print all multiples of ten between 50 and 200, same line"""

for i in range(50, 201):
    if i % 10 == 0:
        print(i, end=" ")
print()

"""Input a number from the user, write a for loop to print all numbers between 1
and the given number, jump by 1"""

x: int = int(input("Please enter a number: "))

for i in range(1, x):
    print(i, end=" ")
print()

""" input a number from the user, write a for loop to print all numbers between 0 
and the given number, jump by 0.5"""

y: int = int(input("Please enter a number: "))

for i in range(y):
    print(i, end=" ")