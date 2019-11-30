"""Find pairs of numbers adding to given sum"""

arr= [10, 20, 25, 30, 40, 50, 60]
print(arr)
summation= int(input('Enter sum to find  numbers:'))

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j] == summation:
            print(arr[i], arr[j])
