
def matrix_mult(x,y):
    result = [[0 for j in range(my)] for i in range(nx)]

    for i in range(nx):
        for j in range(my):
            for k in range(ny):
                result[i][j] += x[i][k] * y[k][i]

    return result


nx,mx= [int(i) for i in input('Enter dimension of x matrix:').split()]
x= [[1 for j in range(mx)]for i in range(nx)]
ny,my= [int(i) for i in input('Enter dimension of y matrix:').split()]
y= [[1 for j in range(my)]for i in range(ny)]

while mx != ny:
    print('\nMultiplication not possible')
    nx, mx = [int(i) for i in input('Enter dimension of x matrix:').split()]
    x = [[1 for j in range(mx)] for i in range(nx)]
    ny, my = [int(i) for i in input('Enter dimension of y matrix:').split()]
    y = [[1 for j in range(my)] for i in range(ny)]

for i in range(nx):
    for j in range(mx):
        print(x[i][j], end=' ')          # print x matrix
    print()
print()

for i in range(ny):
    for j in range(my):
        print(y[i][j], end=' ')      # print y matrix
    print()
print()

result= matrix_mult(x,y)

for i in range(nx):
    for j in range(my):
        print(result[i][j], end=' ')      # print resultant matrix
    print()



