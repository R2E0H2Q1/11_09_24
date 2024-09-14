"""o use when we don't have a defined begin and end.
the loop runs until I get the requested action"""
x: int = int(input("Please enter a positive number: "))
while x <= 0:
    print("This is not a positive number")
    x: int = int(input("Please enter a positive number: "))
    print(F"{x} is a positive number!")


"""
When I want to count the amount of provided x
"""
y: int = int(input("Please enter a positive number: "))
counter: int = 1 #starts with 1
while y <= 0 and counter != 3:
    counter += 1
    y: int = int(input("Please enter a positive number: "))

    if counter == 3: #can't try more than 3 times
        print("You tried too many times")
    else:
        print(F"{y} is a positive number!")

"""
input grade from the user
input again and again until: 55<= grade <=100
don't input more than 3 
if the grade was incorrect 3 times print "Test the course again"
else "You passed the Test" 
"""

# score: int = int(input("Please enter your grade: "))
# counter: int = 1 #starts with 0

while score <= 55 and counter < 3:
    counter += 1
    print("You need to take the Test again")
    score = int(input("Please enter your grade: "))

    if score < 55:
        print("You need to take the Test again")

    else:
        print(F"Your score is {score}, you passed the test!")

"""
ex4
input grade from user, until the grade is valid 
valid grade is between 0-100
"""

grade: int = int(input("Please enter your grade: "))

while grade < 0 or grade > 100:
    print("Your score is incorrect, Please enter a grade between 0 and 100.")
    grade = int(input("Please enter your grade: "))
print(f"Your score is {grade}, you grade is valid!")