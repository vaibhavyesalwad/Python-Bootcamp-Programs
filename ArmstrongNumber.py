
number = input('Enter number:')
degree = len(number)

number = int(number)
temp = number
sum = 0
while number > 0:
    remainder = number % 10
    sum += pow(remainder,degree)
    number //= 10

if temp == sum:
    print(f'{temp} is armstrong number')
else:
    print(f'{temp} is not armstrong number')
