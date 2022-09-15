def exponent(num, power=2):
    return num ** power
print(exponent(7))
print(exponent(3))
print(exponent(3,3))

def info(first_name="colt", is_instructor = False):
    if first_name == "colt" and is_instructor:
        return "Welcome back instructor colt"
    elif first_name == "colt":
        return "I really thought you were an instructor..."
    return f"Hello {first_name}"

print(info())
print(info(is_instructor= True))
print(info('pratham'))

def add(a,b):
    return a+b

def math(a,b, fn=add):
    return fn(a,b)

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

print(math(3,3, multiply))
print(math(4,3, subtract))
print(math(2,2))