
lines= int(input('Enter number of lines:'))

for line in range(1,lines+1):
    print(' '*(lines-line),'*'*line,sep='')