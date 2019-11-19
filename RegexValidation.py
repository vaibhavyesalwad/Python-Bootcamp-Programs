import re

'''fname= input('First name:')
match= re.search('[^a-zA-Z]',fname)
while match:
    print('Invalid first name')
    fname = input('First name:')
    match = re.search('[^a-zA-Z]', fname)

lname= input('Last name:')
match= re.search('[^a-zA-Z]',lname)
while match:
    print('Invalid last name')
    lname = input('Last name:')
    match= re.search('[^a-zA-Z]', lname)
'''
email= input('Email:')
atdrate= re.findall('@',email)
prefix, domain= re.split('@',email)
prefix_full= re.search('[^a-zA-Z0-9._-]',prefix)
prefix_start= re.search('^[^a-zA-Z0-9]',prefix)
prefix_end= re.search('[^a-zA-Z0-9]',prefix)

while prefix_full or prefix_start or prefix_end or len(atdrate) != 1:
    print('Invalid email id')
    email = input('Email:')
    atdrate = re.findall('@', email)
    prefix, domain = re.split('@', email)
    prefix_full = re.search('[^a-zA-Z0-9._-]', prefix)
    prefix_start = re.search('^[^a-zA-Z0-9]', prefix)
    prefix_end = re.search('[^a-zA-Z0-9]', prefix)









