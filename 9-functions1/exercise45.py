'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(list = []):
    if list:
        return list[-1]
    return None
print(last_element())