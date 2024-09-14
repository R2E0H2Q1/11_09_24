from while_loop import grade

# for
# while
# do-while

# input 3 grades
# calculate avg
# (grade1 + grade2 + grade3) / 3
# do it until all 3 grades are different
# all grades are between 0-100
# avg is more than 85

while True:
    grade1: int = int(input("grade1:"))
    grade2: int = int(input("grade2:"))
    grade3: int = int(input("grade3:"))
    avg_grades = (grade1 + grade2 + grade3) / 3
    # check if iterate to again ...
    if 0<= grade1 <= 100 and 0<= grade2 <= 100 and 0<= grade3 <= 100\
        and avg_grades > 85 and not grade1 == grade2 == grade3:
        break
    # go back to while

x: int = 10
while True:
    print(x)
    x += 1
    if x == 21:
        break
