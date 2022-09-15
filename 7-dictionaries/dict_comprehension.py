numbers = {'first': 1, 'second': 2, 'third': 3}
squared_numbers = {keys: value**2 for keys,value in numbers.items()}
print(squared_numbers)

second = {num: num**2 for num in range(1,6)}
print(second)

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0,len(str1))}
print(combo)

me = {'name': 'pratham', 'city': 'delhi', 'age': 'eighteen'}
print(me)
yelling_me = {k.upper():v.upper() for k,v in me.items()}
print(yelling_me)
