'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(string):
    string = string.replace(" ", "").lower()
    if string == string[::-1]:
        return True
    return False
print(is_palindrome('a man a plan a canal Panama'))