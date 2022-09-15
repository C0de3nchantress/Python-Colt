# **kwargs

'''
A special operator we can pass to functions

Gathers remaining keyword arguments in a dictionary
'''

def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s fav color is {color}")

fav_colors(pratham = 'white', ted = 'green', walt = 'purple')


def special_greeting(**kwargs):
    if 'david' in kwargs and kwargs['david'] == 'special':
        return 'You get a special greeting David'
    elif 'david' in kwargs:
        return f"{kwargs['david']} david"
    return "not sure who u are"
print(special_greeting(david = 'hey'))
print(special_greeting(walt = 'special'))
print(special_greeting(david = 'special'))