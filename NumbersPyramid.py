"""Print Pyramid of numbers in increasing and decreasing order"""
lines = int(input('Enter number of lines:'))

for i in range(1, lines+1):
    spaces = ' '*(lines-i)
    n= 2*i-1
    nums = ''
    k = 1
    for j in range(1, n+1):
        nums += str(k)
        if j >= i:
            k -= 1
        else:
            k += 1
    msg = spaces + nums             # string for each line
    print(msg)
