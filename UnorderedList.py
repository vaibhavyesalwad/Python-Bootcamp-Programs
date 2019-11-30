
import utilities

mylist = utilities.List()

with open("myfile.txt",'r') as f:
    string = f.read()

print(string)
words = string.split()
print(words)
print(len(words))


for word in words:
    mylist.add(word)

mylist.traverse()

while True:
    print('''
        Enter ur choice:
        1. Add item to list
        2. Remove item from list
        3. Search item in the list
        4. Check list empty or not
        5. Size of list
        6. Append item at end of list
        7. Find index of item
        8. Insert item at given position in list
        9. Pop item from end list or pop item at position in list
       10. Enter element
       11. Traverse list
       12. Exit  
        ''')

    choice = input(':>')
    if choice == '1':
        item = input('Enter item to add:')
        mylist.add(item)
    elif choice == '2':
        item = input('Enter item to remove:')
        mylist.remove(item)
    elif choice == '3':
        item = input('Enter item to search:')
        mylist.search(item)
    elif choice == '4':
        print(mylist.isEmpty())
    elif choice == '5':
        print(mylist.size())
    elif choice == '6':
        item = input('Enter item to append:')
        mylist.append(item)
    elif choice == '7':
        item = input('Enter item to find index')
        print(mylist.index(item))
    elif choice == '8':
        item = input('Enter item to be inserted:')
        pos = input('Enter position of element:')
        try:
            pos = int(pos)
            mylist.insert(pos, item)
        except:
            print('Please enter only integers as entry for position')
    elif choice == '9':
        pos = input('Enter position of item to pop:')
        if pos == '':
            mylist.pop()
        else:
            try:
                pos = int(pos)
                if pos < 1:
                    print('Index outbound')
                else:
                    mylist.pop(pos)
            except:
                print('Please enter only integers as entry for position')
    elif choice == '10':
        item = input('Enter item:')
        if mylist.search(item):
            mylist.remove(item)
            print(f'{item} found and deleted')
        else:
            mylist.add(item)
            print(f'{item} not found so added to list')
    elif choice == '11':
        mylist.traverse()
    elif choice == '12':
        break
    else:
        print('Invalid choice')


string1 = mylist.extract()
print(string1)
with open('newfile','w') as f:
    f.write(string1)


