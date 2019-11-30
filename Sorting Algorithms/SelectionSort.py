"""Sort numbers in list using Selection sort algorithm"""
numbers = [int(n) for n in input('Enter list of numbers:').split()]
print(numbers)

for i in range(len(numbers)-1):
    min = i
    for j in range(i+1,len(numbers)):
        if numbers[j] < numbers[min]:
             min = j

    numbers[i], numbers[min] = numbers[min], numbers[i]

print(numbers)
