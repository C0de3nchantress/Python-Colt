def add_nums(*nums):
    total = 0
    for num in nums:
        total+=num
    return total
nums = [1,2,3,4,5,6,10]
print(add_nums(*nums))
nums_tuple = (1,2,3,4,5,6,11)
print(add_nums(*nums_tuple))