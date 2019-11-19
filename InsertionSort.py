
numbers = [int(i) for i in input('Enter list of numbers:').split()]
print(numbers)

for i in range(1,len(numbers)):
    j=i
    while j > 0:
        if numbers[j] < numbers[j-1]:
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
        j -= 1


print(numbers)

