# 222222
# answer should be 31
# apply any of the operators


# BITWISE OPERATORS

# bitwise AND
# print(2 & 3)
# 2 ---- 010
# 3 ---- 110
#AND ---- 010

# bitwise OR
# print(2 | 4)
# 2 ---- 010
# 4 ---- 100
#OR ---- 110 -- 6

# bitwise NOT
# print(~4)
# 4 ---- 100
#   -( 100 )
#       +1
  # -(101)
  # 101 --- 5

# bitwise XOR

# print(2^3)
# 2 ---- 010
# 3 ---- 011
# XOR -- 001   -    1

# left shift
# print(2<<1)
# 2 ---- 010
#       0100   - 4

#right shift

# print(4>>1)
# 4 ---- 0100
#        0010  - 2

# n = int(input("Enter n:"))
# r = 1
#
# while r <= n:
#     c = 1
#     count = 1
#     spaces = n - r
#     while spaces:
#         print(" ", end=" ")
#         spaces = spaces - 1
#         c = c + 1
#     while c <= n:
#         print(count, end=" ")
#         count = count + 1
#         c = c + 1
#     x = 1
#     y = r - 1
#     while y:
#         print(y, end=" ")
#         x = x + 1
#         y = y - 1
#     r = r + 1
#     print()


# while 1:
#     n = int(input("Enter no:"))
#     fact = 1
#     i = 1
#     while i <= n:
#         fact = fact * i
#         i = i + 1
#     print(fact)
#     choice = input("y/n: ")
#     if choice == 'y':
#         continue
#     else:
#         exit()


num = int(input("Enter number: "))
r = 1
while r <= num:
  c = 1
  # x = 1
  spaces = num - r 
  while spaces:
    print(" ",end=" ")
    c = c + 1
    spaces = spaces - 1
  while c <= num:
    print("*",end=" ")
    # x = x + 1
    c = c + 1
  y = 1
  # z = r - 1
  while y < r:
    print("*",end=" ")
    y = y + 1
    # z = z - 1
  print()
  r = r + 1
