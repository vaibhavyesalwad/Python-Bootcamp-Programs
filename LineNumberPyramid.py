
lines= int(input('Enter number of lines:'))

for line in range(1,lines+1):
    print(' '*(lines- line),end='')
    j= lines
    for i in range(1, 2*line):
        if i < line:
            print(j,end='')
            j -= 1
        else:
            print(j,end='')
            j += 1
    print()