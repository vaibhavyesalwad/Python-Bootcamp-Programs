import random

char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

n = int(input('Enter total number of coupons:'))
length = int(input('Enter coupon length:'))

for i in range(n):
    for j in range(length):
        print(random.choice(char),end='')
    print()