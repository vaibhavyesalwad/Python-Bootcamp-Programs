
n= int(input('Enter order of magic matix:'))

magic = [[0 for j in range(n)] for i in range(n)]

numbers = [i for i in range(1,n*n+1)]

i= 0
j= n//2

for num in numbers:
 


for i in range(n):
    for j in range(n):
        print(magic[i][j],end=' ')
    print()



