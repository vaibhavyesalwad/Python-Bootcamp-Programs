"""Reverse words in given string but keep string in order"""
string = input('Enter string:')

words = string.split()
print(words)
rev_string = ''

for word in words:
    rev_word = ''
    for ch in word:
        rev_word = ch + rev_word

    rev_string += rev_word + ' '

print(rev_string)


