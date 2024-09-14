# # 1.a.
# pizza_slices = int(input('how many pizza slices?'))
# friends: int = 4
#
# each_one_got = pizza_slices // friends  # integer div תוצאה שלמה קיצוץ שארית
# left_over = pizza_slices % friends  # modulus שארית
#
# # 9  / 4 = 2.25
# # 9 // 4 = 2
# # 9 % 4 = 1
# # 13 // 6 = 2
# # 13 % 6 = 1
# # 14 % 6 = 2
# # 15 % 6 = 3
#
# print(f"each one got: {each_one_got} left over: {left_over}")
#
# # 1.b.
#
# pizza_slices = int(input('how many pizza slices?'))
# friends: int = int(input('how many friends?'))
#
# each_one_got = pizza_slices // friends  # integer div
# left_over = pizza_slices % friends  # integer div
#
# print(f"each one got: {each_one_got} left over: {left_over}")

# 2
# MAKE ALL OF THIS CONDITION TRUE
# a = 1
# b = 1
# if a == b:
#     print(f"was True for {a} {b}")
# else:
#     print(f"was False for {a} {b}")
#
# a = 1
# b = 0
# c = 1
# d = 0
# # 1 + 3
# # 3 + 1
#
# #           +         *
# #if a == b or c == d and a == c:
#
# #   0     *     0
# #   0    and    0
# if a + b and c + d:
#     print(f"was True for {a} {b} {c} {d}")
# else:
#     print(f"was False for {a} {b} {c} {d}")
#
# # MAKE ALL OF THIS CONDITION FALSE
# a = 1
# b = 0
# if a == b:
#     print(f"was True for {a} {b}")
# else:
#     print(f"was False for {a} {b}")
#
# a = 0
# b = 0
# c = 0
# d = 0
# if a + b and c + d:
#     print(f"was True for {a} {b} {c} {d}")
# else:
#     print(f"was False for {a} {b} {c} {d}")

x: int = 10
while x <= 20:
    print(x, end=" ")  # end=" " instead of line break ==> write space
    x = x + 1  # x += 1

print()  # line break

x = 10
while x <= 20:
    print(x, end=" ")  # end=" " instead of line break ==> write space
    x += 2  # x = x + 2

print()  # line break

x = 10
gap: int = float(input('whats the gap?'))  # can be 0.5
while x <= 20:
    print(float(x), end=" ")  # end=" " instead of line break ==> write space
    x -= gap  # x = x + gap