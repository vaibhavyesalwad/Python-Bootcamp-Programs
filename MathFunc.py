import math as m

def is_prime(num):
    if num == 1:
        return '1 is neither prime nor composite'
    else:
        for i in range(2, num//2+1):
            if num % i == 0:
                return False
        else:
            return True

print(dir(m))
print(m.pow(2,4))
print(m.sin(m.pi/6))
print(m.cos(m.pi/3))
print(bin(100))
print(m.sqrt(3))

number= int(input('Enter number to check prime:'))

if is_prime(number):
    if is_prime(number) == True:
        print(f'{number} is prime number')
    else:
        print(is_prime(number))
else:
    print(f'{number} is composite number')