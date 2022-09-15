def display_names(first, second):
    return f"{first} says hello to {second}"
names = {'first': 'pratham', 'second': 'amulya'}
print(display_names(**names))

def add_and_multiply_numbers(a,b,c, **kwargs):
    print(a + b * c)
    print("OTHER STUFF")
    print(kwargs)
data = dict(a=1,b=2, c=3, d=55, name='tony')
add_and_multiply_numbers(**data, cat='blue')