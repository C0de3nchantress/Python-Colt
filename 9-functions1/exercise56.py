'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

def partition(list1, fn):
    return [[val for val in list1 if fn(val)], [val for val in list1 if not fn(val)]]
print(partition([1,2,3,4]))