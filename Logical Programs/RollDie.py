"""Find number that has occurred maximum times and it's frequency"""
import random

n = int(input('Enter number of times you want to roll a die:'))

result = [random.randint(1, 6) for i in range(n)]
print(result)

unique = []
for r in result:
    if r not in result:
        unique.append(r)


max_count = 0
unique = []
counts = []
for r in result:
    count = 0
    if r not in unique:
        unique.append(r)
        for k in result:
            if k == r:
                count += 1
        counts.append(count)
        if count > max_count:
            max_count = count

for j in range(len(unique)):
    if counts[j] == max_count:
        print(unique[j], end=' ')

print(f'occurred maximum {max_count} times')


