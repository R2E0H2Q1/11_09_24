
# while1.drawio
# input number from the user until the number is positive
# while the user gave input of a negative number -- input again

# START

x: int = int(input('Enter positive number: '))

#while False: # 0 times
#while True:  # will always go in, until ... break
while x <= 0:
    print('this number is not positive!')
    x = int(input('Enter positive number: '))

print('goodbye...')

# STOP
