# while3.drawio
# START
counter: int = 1
x: int = int (input("enter a positive number: "))

while x <= 0 and counter < 3:
    counter += 1
    x = int(input("enter a positive number: "))

if counter == 3:
    print('too many failures...')
else:
    print(f"you did it! the number is {x}")

# STOP
