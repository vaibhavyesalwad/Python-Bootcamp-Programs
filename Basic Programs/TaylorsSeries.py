"""Find sin and cos of angle using Taylor's Series"""


def factorial(m):
    if m == 0 or m == 1:
        return 1
    else:
        return m*factorial(m-1)


def sin_term(x, n):
    return (-1)**(n-1)*(x**(2*n-1))/factorial(2*n-1)


def cos_term(x, n):
    return (-1)**(n-1)*(x**(2*n-2))/factorial(2*n-2)


def take_input():
    angle = int(input('Enter angle in degrees:'))
    angle_radians = angle*3.14/180                            # = math.radians(angle)
    terms = int(input('Enter number of terms(precision):'))
    return angle, angle_radians, terms


print("Finding cos & sin using Taylor's Series")
print("Let's find sin ")
angle, angle_radians, terms = take_input()
sin= 0

for i in range(1, terms+1):
    sin += sin_term(angle_radians, i)


print(f'sin({angle}):{sin}')

print("\nLet's find cos ")
angle, angle_radians, terms = take_input()
cos = 0

for i in range(1, terms+1):
    cos += cos_term(angle_radians, i)

print(f'cos({angle}):{cos}')