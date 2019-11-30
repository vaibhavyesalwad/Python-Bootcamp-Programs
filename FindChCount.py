
word = input('Enter word:')

unique = []
for i in word:
    if i not in unique:
        unique.append(i)

for i in unique:
    print(i,word.count(i))
