
lines= int(input('Enter number of lines:'))

for line in range(1,lines+1):
    print(' '*(lines - line),end='')
    for i in range(1,2*line):
        if i==1 or i==(2*line-1):
            print(1,end='')
        else:
            print(line,end='')

    print()