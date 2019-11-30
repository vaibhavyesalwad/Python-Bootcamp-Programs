"""Print Magic matrix  for odd number of lines"""
n = int(input('Enter order of magic matrix:'))

magic = [[0 for j in range(n)] for i in range(n)]
i = 0
j = n//2

for num in range(1, n*n+1):
    magic[i][j] = num
    if num % n == 0:
        i += 1
    else:
        i = (i - 1) % n
        j = (j + 1) % n

for i in range(n):
    for j in range(n):
        print(magic[i][j], end=' ')
    print()



