# '''
# multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
# '''

# flesh out multiple_letter count:
# def multiple_letter_count(str1):
#     length = len(str1) -1
#     list1 = list(str1)
#     dict1 = {list1[i]: list1.count(list1[i]) for i in range(0, length)}
#     return dict1
# print(multiple_letter_count('awesome'))

def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}
print(multiple_letter_count('hello'))