"""Print Pascal triangle"""
lines = int(input('Enter number of lines:'))
num = [1]

for i in range(1, lines+1):
    spaces = ' '*(lines-i)
    print(spaces, end='')
    for j in num:
        print(j, end=' ')
    print()

    numbers = []
    numbers.append(num[0])
    for i in range(len(num)-1):
        term = num[i] + num[i+1]
        numbers.append(term)

    numbers.append(num[-1])
    num = numbers