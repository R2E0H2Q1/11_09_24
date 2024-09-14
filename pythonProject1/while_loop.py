
# input grade from the user
# input again and again while grade < 55
# but don't input more than 3 times
# if the grade was too low print "take the course again"
# if the grade was too low 3 times print "go home"
#    otherwise print "you passed the course!"
counter: int = 1
grade: int = int(input("enter your grade: "))

while grade <= 55 and counter < 3:
    counter += 1
    print("take the course again")
    grade = int(input("enter your grade: "))

if grade <= 55:
    print('go home...')
else:
    print(f"you passed the course!")

# input grade from user
# until the grade is valid
# valid grade is between 0-100
grade: int = int(input("enter your grade: "))
#while not 0<= grade <=100:
while grade < 0 or grade > 100:
    print("illegal grade")
    grade: int = int(input("enter your grade: "))

print(f"your grade is valid: {grade}")


