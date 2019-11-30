""""""
import random

cash = int(input('Enter stake amount $:'))
goal = int(input('Enter goal $:'))
games = int(input('No of games want to play:'))

win, loss, bets = 0, 0, 0
faces = (-1, 1)

for i in range(games):
    while 0 < cash < goal:
        if random.choice(faces) == 1:
            cash += 1
            bets += 1
        else:
            cash -= 1
            bets += 1

    if cash == goal:
         win += 1
    else:
         loss += 1

print(f'\nTotal bets:{bets}')
print(f'No of wins:{win}')
print(f'% of games won:{win*100/games}')
print(f'Average bets:{bets/games}')


