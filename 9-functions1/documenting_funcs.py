import random
print(print.__doc__) #prints out general information about the inbuilt function
print(random.randint.__doc__)
print([1,2,3].pop.__doc__)

def exponent(num, power=2):
    """Exponent(num,power)raises num to specified power, power defaults at 2""" #we can specify our own information about our custom made functions
    return num**power
print(exponent(8))
print(exponent(2,3))
print(exponent(7))

print(exponent.__doc__)