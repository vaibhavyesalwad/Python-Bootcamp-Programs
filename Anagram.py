def anagram(first,second):
    for i in first:
        if i not in second or first.count(i) != second.count(i):
            return False
    else:
        return True
num2 = 100

first = input('Enter first word:')
second = input('Enter second word:')

first= list(first)
second= list(second)

print(anagram(first,second))
