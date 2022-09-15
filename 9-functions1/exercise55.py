# flesh out intersection pleaseeeee

#LIST COMPREHENSION WAY


# def intersection(list1 = [], list2 = []):
#     # return [i for i in list1 if i in list2]
# print(intersection([1,2,3], [2,3,4]))

# flesh out intersection pleaseeeee
def intersection(list1 = [], list2 = []):
    return [val for val in set(list1) & set(list2)]
print(intersection([1,2,3], [2,3,4]))