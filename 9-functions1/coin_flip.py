# from random import random

# def flip_coin():
#     r = random()
#     if r>0.5:
#         return("Even")
#     else:
#         return("Odd")
# print(flip_coin())

# from random import randrange
# def flip_coin():
#     if randrange(2):
#         return("Even")
#     else:
#         return("Odd")
# print(flip_coin())

from random import choice

def flip_coin():
    a = choice(["even","odd"])
    return(a)
print(flip_coin())