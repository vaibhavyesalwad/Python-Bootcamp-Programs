
def TOH(n,a,b,c):
    if n:
        TOH(n - 1, a, c, b)
        print(f'{a} to {b}')
        TOH(n - 1, c, b, a)


TOH(3,'A','B','C')




