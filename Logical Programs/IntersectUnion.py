"""Find intersection and union of given 2 sets of numbers"""
a = [1, 2, 3, 4, 5]
b = [7, 8, 9, 4, 3, 0, 6]
print(a)
print(b)

alength = len(a)
blength = len(b)

if alength >= blength:
    large = a
    small = b
else:
    large = b
    small = a

common = []
for num in small:
    if num in large:
        common.append(num)

print('Intersection:', common)

union = []

for num in large:
    union.append(num)

for num in small:
    if num not in union:
        union.append(num)

print('Union:', union)


