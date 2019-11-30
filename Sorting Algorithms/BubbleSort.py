"""Sort numbers in list using bubble sort algorithm"""
numbers = [int(n) for n in input('Enter list of numbers:').split()]
print(numbers)

for i in range(len(numbers)-1):
    for j in range(len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)
