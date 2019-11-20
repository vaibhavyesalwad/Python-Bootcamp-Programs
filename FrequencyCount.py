
string = input('Enter string:')
words= string.split()

for i in range(len(words)-1):
    min = i
    for j in range(i+1,len(words)):
        if words[j] < words[min]:
            min = j

    words[min],words[i]= words[i],words[min]

print(words)

unique = []
for word in words:
    if word not in unique:
        unique.append(word)

frequency= []
for word in unique:
    freq= words.count(word)
    frequency.append(freq)

freq_words = dict(zip(unique,frequency))

print(freq_words)