"""Find second max and minimum in given list of numbers"""
numbers = [int(n) for n in input('Enter list of numbers:').split()]
print(numbers)
min = min2 = max = max2 = numbers[0]

for num in numbers:
    if num > max:
        max2 = max
        max = num
    elif num < min:
        min2 = min
        min = num

print(f'max and 2nd max {max, max2}')
print(f'min and 2nd min {min, min2}')
