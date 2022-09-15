'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

def number_compare(num1 = 0,num2 = 0):
    if num1>num2:
        return 'First is greater'
    elif num2>num1:
        return 'Second is greater'
    return 'Numbers are equal'
print(number_compare())
