
def fibo(n):
    a= 0
    b= 1

    for i in range(n):
        print(a)
        a,b= b,a+b

terms = int(input('Enter of terms in fibonacci series:'))

fibo(terms)