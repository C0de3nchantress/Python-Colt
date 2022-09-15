'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(list1 = [], command = '', location = '', value = 0):
    if command == 'remove':
        if location == 'end':
            return list1.pop()
        elif location == 'beginning':
            return list1.pop(0)
    elif command == 'add':
        if location == 'beginning':
            list1.insert(0, value)
            return list1
        elif location == 'end':
            list1.append(value)
            return list1
print(list_manipulation([1,2,3], 'add', 'end', value  = 20))