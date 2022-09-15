# *args

'''
This is a special operator we can pass to functions

This gathers remmaining arguments as a tuple

This is just a parameter- You can call it whatever you want!
'''
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total+=num
    return total
print(sum_all_nums(1,5,6,7))

def ensure_correct_info(*args):
    if "Pratham" in args and "Verma" in args:
        return "Welcome back Pratham"
    return "Not sure who you are"

print(ensure_correct_info('hey', 'you', 'are', 'the', 'dumbest', 'person', 'to' 'set', 'foot', 'in', 'this', 'universe'))
print(ensure_correct_info('hey', 'Pratham', 'Verma', 'is', 'the', 'dumbest', 'person', 'to' 'set', 'foot', 'in', 'this', 'universe'))