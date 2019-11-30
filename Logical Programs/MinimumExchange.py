"""Find minimum notes for exchange"""
denominations = [1000, 500, 200, 100, 50, 10, 5, 2, 1]
change = int(input('Enter amount to be given as change:'))

result = {}
for d in denominations:
    if d <= change:
        count = change//d
        change -= count*d
        result[d] = count
        if change == 0:
            break

print(result)

