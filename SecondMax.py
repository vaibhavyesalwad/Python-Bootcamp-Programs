
numbers= [4,2,1 -2,2000,5,8,6,100,99,89,4000,-4]

flag= 0

for num in numbers:
    if flag==0:
        min= min2= max = max2 = num
        flag +=1
    if num > max:
        max2 =max
        max = num
    if num < min:
        min2= min
        min= num



print(max, max2)
print(min, min2)
