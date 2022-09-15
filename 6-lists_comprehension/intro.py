numbers = [1,2,3,4,5,6]
# doubled_numbers = []
# for num in numbers:
#     doubled_number = num*2
#     doubled_numbers.append(doubled_number)
# print(doubled_numbers)
print("DOUBLED NUMBERS EXAMPLE")
doubled_numbers = [num *2 for num in numbers]
print(doubled_numbers)

print("STRING EXAMPLE")
friends = ["ashley", "matt", "michael"]
a= [friend[0].upper() + friend[1:] for friend in friends]
print(a)

name = "pratham"
upper = [char.upper() for char in name]
print(upper)
numbers_3 = numbers[:3]
doubled_numbers = [num*10 for num in range(3)]
print(doubled_numbers)

string_list = [str(num) for num in numbers]
print(string_list)

evens = [num for num in numbers if num % 2 ==0]
odds = [num for num in numbers if num %2 != 0]
print(evens, odds)


with_vowels = "This is so much fun"
without_vowels = ''.join([char for char in with_vowels if char not in "aeiou"])
print(with_vowels)
print(without_vowels)