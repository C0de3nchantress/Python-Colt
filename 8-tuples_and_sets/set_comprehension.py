print({x**2 for x in range(10)})
print({char.upper() for char in "balls"}) #NOTICE HOW THE DOUBLE L GETS CUT TO A SINGLE L AND DOES NOT REPEAT

string = "sequioa"
def are_all_vowels_in_string(string):
    return len({char for char in string if char in "aeiou"}) == 5
are_all_vowels_in_string(string)