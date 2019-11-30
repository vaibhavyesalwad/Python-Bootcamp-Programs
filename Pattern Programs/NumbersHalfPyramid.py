"""Print half pyramid of numbers"""
lines = int(input('Enter number of lines:'))
num = 1

for i in range(1, lines+1):
    numstr= ''
    for j in range(i):
        numstr += str(num)
        num += 1
    print(numstr)
