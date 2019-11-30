"""Convert decimal to binary & vice versa"""
# Converting decimal to binary
number = int(input('Enter decimal number:'))
binary_str = ''

while number:
    remainder = number % 2
    binary_str = str(remainder) + binary_str
    number //= 2

length = len(binary_str)
if length < 8:
    binary_str = '0'*(8-length) + binary_str

print(binary_str[:4], binary_str[4:])

print('After swapping nibbles:', binary_str[4:], binary_str[:4])


# converting binary to decimal

binary = input('Enter binary number:')
power = 0
num = 0

for i in binary[::-1]:
    num += (2**power)*int(i)
    power += 1

print(num)


