"""Print pyramid of stars"""
lines = int(input('Enter number of lines:'))

for i in range(1, lines+1):
    print(' '*(lines - i)+'*'*(2*i-1))

    