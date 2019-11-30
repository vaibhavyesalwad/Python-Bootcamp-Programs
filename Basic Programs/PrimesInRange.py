"""Find all prime numbers in given range"""
start = int(input('Enter starting number:'))
end = int(input('Enter ending number:'))

count = 0
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num//2+1):
            if num % i == 0:
                break
        else:
            print(num, end=' ')
            count += 1


print('\nTotal prime numbers:', count)
