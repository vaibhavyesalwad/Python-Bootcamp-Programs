import random

n = int(input('Enter number of times you want to roll a die:'))

result = [random.randint(1,6) for i in range(n)]
print(result)

distinct_faces = list(set(result))
print(distinct_faces)

max_count = 0
for i in distinct_faces:
    count = result.count(i)

    if count >= max_count:
        max_count = count

maxterms =[]
for f in distinct_faces:
    if result.count(f) == max_count:
        maxterms.append(f)

print(f'{maxterms} occurred maximum {max_count} times')


