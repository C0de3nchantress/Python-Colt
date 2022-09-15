'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(list, search_term):
    return list.count(search_term)
print(frequency([True, False, True, True], True))