"""Print pyramid of stars with spaces"""
lines = int(input('Enter number of lines:'))

for i in range(1, lines+1):
    print(' '*(lines-i)+' *'*i)
    