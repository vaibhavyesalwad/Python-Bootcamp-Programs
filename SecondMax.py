
numbers= [4,2,1 -2,5,8,6,100,99,89]

max,max2= 0,0
for num in numbers:
    if num > max:
        max = num
    elif num < max and num > max2 :
        max2 = num

print(max, max2)