
summation= int(input('Enter sum to find  numbers:'))

arr= [10,20,25,30,40,50,60]

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j] == summation:
            print(arr[i],arr[j])
