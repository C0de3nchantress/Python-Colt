'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''

def calculate(**kwargs):
    operation = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    op_val = operation[kwargs.get('operation', '')]
    if is_float:
        final = f"{kwargs.get('message','the result is')}, {float(op_val)}"
    else:
        final = f"{kwargs.get('message','the result is')}, {int(op_val)}"
    return final
print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))