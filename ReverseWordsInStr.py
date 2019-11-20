
string= input('Enter string:')

words= string.split()
print(words)
rev_wordstring= ''

for word in words:
    rev_word=''
    for ch in word:
        rev_word = ch + rev_word

    rev_wordstring += rev_word +' '

print(rev_wordstring)


