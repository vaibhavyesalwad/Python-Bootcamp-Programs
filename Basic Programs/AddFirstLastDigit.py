""""Add first and last digit of given number"""
num = int(input('Enter number'))
last = num % 10

while num >= 10:
    num //= 10

print(num, last)
print(num+last)
