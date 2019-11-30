"""Find factorial of given number"""


def fact(num):
    if num < 0:
        return 'factorial of negative number not possible'
    elif num == 0:
        return 1
    else:
        factorial= 1
        for i in range(1, num+1):
            factorial *= i
        return factorial


def recurse_fact(num):
    if num < 0:
        return 'Factorial of negative number not possible'
    elif num == 0 or num == 1:
        return 1
    else:
        return num*recurse_fact(num-1)


num= int(input('Enter number:'))
print(fact(num))
print(recurse_fact(num))
