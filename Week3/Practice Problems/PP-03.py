# Reverse the digits in the given number:

num = int(input("Enter a number: "))
absNum = abs(num)

rev = absNum % 10
absNum = absNum // 10

while (absNum > 0):
    r = absNum % 10
    absNum = absNum // 10
    rev = rev * 10 + r

if num >= 0:
    print(rev)
else:
    print(rev - rev * 2)