'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(string):
    return string[:1].upper() + string[1:]
print(capitalize('tim'))