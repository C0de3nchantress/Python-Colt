'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

#define single_letter_count below:
# def single_letter_count(word = '', letter = ''):
#     word = word.lower()
#     letter = letter.lower()
#     return word.count(letter)
# print(single_letter_count('hElLo world', 'l'))

#A shorter version would be

def single_letter_count(string, letter):
    return string.lower().count(letter.lower())
    