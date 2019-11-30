"""Generate n coupons with m length"""
import random

char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

n = int(input('Enter total number of coupons:'))
m = int(input('Enter coupon length:'))

for i in range(n):
    for j in range(m):
        print(random.choice(char), end='')
    print()
    