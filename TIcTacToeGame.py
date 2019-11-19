import random

def show_values():
    for i in range(3):
        for j in range(3):
            print(f'{positions[i][j]}:{values[i][j]}',end=' ')
        print()
    print()

def fill_value(pos, usr_sign):
    for i in range(3):
        for j in range(3):
            if positions[i][j] == pos:
                values[i][j]= usr_sign


def check_position(pos):
    if pos < 1 or pos > 9:
        return 'Invalid position'

    for i in range(3):
        for j in range(3):
            if positions[i][j] == pos:
                if values[i][j] != ' ':
                    return f'{pos} already filled'

    return False

def check_end(sign):
    i=0
    for j in range(3):
       if values[i][j]== sign:
           continue
       else:
           break
    else:
        return True

    i = 1
    for j in range(3):
        if values[i][j] == sign:
            continue
        else:
            break
    else:
        return True

    i = 2
    for j in range(3):
        if values[i][j] == sign:
            continue
        else:
            break
    else:
        return True

    j= 0
    for i in range(3):
        if values[i][j] == sign:
            continue
        else:
            break
    else:
        return True

    j = 1
    for i in range(3):
        if values[i][j] == sign:
            continue
        else:
            break
    else:
        return True

    j = 2
    for i in range(3):
        if values[i][j] == sign:
            continue
        else:
            break
    else:
        return True


    for i in range(3):
        if values[i][i]==sign:
            continue
        else:
            break
    else:
        return True

    if values[0][2]== values[2][0]==values[1][1]== sign:
        return True

pos= 1
positions= [[0 for j in range(3)] for i in range(3)]
values= [[' ' for j in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        positions[i][j] = pos
        pos += 1

show_values()
print("Let's play tic toe game")
usr_sign= input("Choose 'x' or  'o'  sign:")
if usr_sign == 'x':
    comp_sign = 'o'
else:
    comp_sign = 'x'

s= 0
comp_pos=[i for i in range(1,10)]
count=0

while True:
    pos = int(input('Enter position to fill:'))
    while check_position(pos):
        print(check_position(pos))
        pos = int(input('Enter position to fill:'))

    fill_value(pos, usr_sign)
    show_values()
    sign= usr_sign
    check_end(sign)
    if check_end(sign):
        print('You won')
        break
    count += 1
    if count == 9:
        print('Game tie')
        break

    comp_pos.remove(pos)
    random.seed(s)
    pos = random.choice(comp_pos)
    fill_value(pos,comp_sign)
    random.seed(s)
    comp_pos.remove(pos)
    s += 1
    show_values()
    sign= comp_sign
    if check_end(sign):
        print('comp won')
        break
    count += 1

