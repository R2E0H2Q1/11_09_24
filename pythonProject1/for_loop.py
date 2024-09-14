

# when we know the range
# 1.. 10
# -100 .. 1000
# 0 .. 200 jump 5

for i in range(10):  # 0 1 2 3 4 5 6 7 8 9
    print(i, end=" ")

# x: int = 10
# while x <= 20:
#     print(x, end=" ")  # end=" " instead of line break ==> write space
#     x = x + 1  # x += 1

#              start, end, gap
for i in range(10, 20 + 1, 1):
    print(i, end=" ")
print()

#              start, end, gap
for i in range(10, 20 + 1, 2):
    print(i, end=" ")
print()

#              start, end, gap=1 default
for i in range(10, 20 + 1):
    print(i, end=" ")
print()

for i in range(20, 10 - 1, -1):
    print(i, end=" ")
print()

# write a for loop to print all odd(e-zugi) number between 7 and 39, same-line
for i in range(7, 39 + 2, 2):
    print(i, end=" ")
print()

# write a for loop to print all 10 multiplies between 50 and 200 , same-line
#             start=50, end, gap=10
for i in range(50, 200 + 10, 10):
    print(i, end=" ")
print()

# input a number from the user, write a for loop to print all numbers between 1 and the given number jump by 1
#     i.e. if the user wrote 5 then print -> 1 2 3 4 5
num: int = int(input('whats the number?'))
for i in range(1, num + 1, 1):
    print(i, end=" ")
print()

# input a number from the user, write a for loop to print all numbers between 0 and the given number jump by 0.5
#     i.e. if the user wrote 5 then print ->  0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0
num: int = int(input('whats the number?'))
for i in range(0, num + 1, 1):
    print(float(i), end=" ")
    if i is not num:
        print(float(i) + 0.5, end=" ")
print()

# input(5) * 2 ==> 10
# 0/2 = 0
# 1/2 = 0.5
# 2/2 = 1.0
# 3/2 = 1/5
# ...
for i in range(0, num * 2 + 1, 1):
    print(float(i / 2), end=" ")
print()

# input 5 numbers from the user
for _ in range(1, 5 + 1):
    x: int = int(input('enter a number'))


