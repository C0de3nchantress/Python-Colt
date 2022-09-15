'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(list = []):
    list2 = [num for num in list if num % 2 == 0]
    result = 1
    for num in list2:
        result = result * num
    return result
print(multiply_even_numbers([2,3,4,5,6]))