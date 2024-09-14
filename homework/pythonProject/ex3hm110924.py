# In the following exercises, solve using a for loop, or a while loop, or a break-true-white loop:

# - Receive from the user his height (decimal), until a height between 0.4 and 2.5 is obtained
# Every time a height outside of this range is received, print: input wrong

while True:
    height: float = float(input('Please provide your height: '))

    if 0.4 <= height <= 2.5:
        print('Your height is average')
        break
    else:
        print("Wrong Input")
print()

# - Receive 2 numbers (whole numbers) from the user. And print the whole numbers between them.
# For example, if 1 and 5 are entered, print: 1 2 3 4 5. Note: the first number entered is not necessarily
# smaller than the second number received. That is, if 5 and 1 are entered, then it will be printed: 5 4 3 2 1

num1: int = int(input('Please enter your first digit: '))
num2: int = int(input('Please enter your second digit: '))

if num1 <= num2:
    for i in range(num1, num2 + 1):
        print(i, end=' ')

else:
    for i in range(num1, num2 -1, -1):
        print(i, end=' ')
print()

# - The value of a pie is 3.14 Ask the user how much a pie is worth? and receive his answer
# in a loop until he types the correct answer. The user has only 3 attempts.
# If successful within 3 attempts (or less), print: "correct are you"
# If we fail 3 times, exit the loop and print: "3.14 is pie"

counter: int = 1
pi = 3.14
value: float = float(input("Please enter the value of Pi: "))

while value != pi and counter < 3:
    counter += 1
    print("Your answer is wrong!, please try again!")
    value = float(input("Please enter the value of Pi: "))

if value == pi:
    print("Your answer is correct!")

else:
    print("The value of pie is 3.14")
print()

# - Receive from the user 3 numbers in a loop until:
# The first number received will be between 0-10
# + And also the second number received will be between 10-60
# + And also the third number received will be between .60-100
# + and the second number received will also be an average of the three numbers.
# For example: 10 50 90
# Enter the 3 numbers in a loop over and over again... until all the conditions are met

while True:
    num1: int = int(input('Please enter a number between 0 and 10: '))
    num2: int = int(input('Please enter a number between 10 and 60: '))
    num3: int = int(input('Please enter a number between 60 and 100: '))
    avg = (num1 + num2 + num3) / 3

    if 0 <= num1 <= 10 and 10 <= num2 <=60 and 60 <= num3 <=100 and num2 == avg:
        print(f'The provided numbers {num1}, {num2}, {num3} are between range!')
        break
print()

# - *Challenge: The pub has 10 beers. It is allowed to give beer only to those who have turned 18 years old. collect
# from the user his age. Only if the user is 18 years old give him a beer. Repeat the process until
# that all 10 beers were distributed

beers = 10

while beers > 0: #will the number of beers is bigger than 0 it will go into the loop
    age: int = int(input('Please enter your age: ')) #needs to be added here so it checks the age  every chance.

    if age >= 18:
        print("You can have a beer!")
        beers -= 1 #this checking needs to be added at the end so it updates the count.
        print(f'There are only {beers} beers left!')
        print()

    else:
        print("You aren't old enough for a beer, please try again in a few years!")
#       break isn't need it
    if beers == 0:
        print("There aren't more beers left!")