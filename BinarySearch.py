def binary_search(arr, element):
    length = len(arr)
    first = 0
    last = length - 1

    while (first <= last):
        mid = (first + last) // 2
        if arr[mid] == element:
            return str(mid)
        elif element < arr[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return 0


arr = [40, 50, 65, 89,138, 147, 149, 187, 211, 222]
print(arr)
element= int(input('Enter number to search:'))

length= len(arr)
first= 0
last = length -1

position= binary_search(arr,element)
if position:
    print(f'{element} found at {position}')
else:
    print(f'{element} not found')






