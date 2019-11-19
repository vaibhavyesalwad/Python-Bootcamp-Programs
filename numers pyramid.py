
lines= int(input('Enter number of lines:'))
num=0
for i in range(1,lines+1):
    spaces= ' '*(lines-i)
    numstr=''
    for j in range(2*i-1):
        numstr += str(num)
        num += 1

    msg= spaces + numstr
    print(msg)