inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
stock_list = {}
stock_list.update(inventory)
stock_list['cookie'] = 18
stock_list.pop('cake')
print(stock_list)