import re

print()
string = 'How are you, all good?. 2 eyes and 4 legs 6 400 5 300'
pattern = 'y'

# all mathches are return & empty list<- no found
result = re.findall(pattern, string)
print(string)
print(result)
print('Total counts:', len(result))

pattern = 'z'
# list of substrings after split
# if no found list containing string
result = re.split(pattern, string)
print(result)

pattern = ' '
# at max 3 splits
result = re.split(pattern, string, 3)
print(result)

pattern = 'e'
replace = 'a'
# replacing pattern if no found return original str
result = re.sub(pattern, replace, string)
print(result)

# at max 2 replacements
result = re.sub(pattern, replace, string, 2)
print(result)

pattern = ' '
replace = '*'
# replace all places & return count
result = re.subn(pattern, replace, string)
print(result)

pattern = '(\d{3}) (\d{1})'
match = re.search(pattern, string)
print(match)  # only 1st match object if found

# if match not found None
if match:
    print(match.group())
else:
    print('No match')

print(match.group(1))
print(match.group(2))
print('match start:', match.start())
print('match end:', match.end())
print('match span:', match.span())
print('search pattern made:', match.re)
print('string for search:', match.string)