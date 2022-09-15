#tuples are lists but are faster and immutable
a = (1,2,3,4,5,5)
print(type(a))
#also lists cannot be used as keys for dictionaries but tuples can be used as keys.
b = {
    (33,44): "dick",
    (44,44): 'vagina'
}
print(b[(33,44)], b[(44,44)])
# tuples use .count() and index() 

#SETS
cities = ["delhi", 'gurgaon', 'gujarat', 'mumbai', 'delhi', 'gurgaon', 'odissa', 'mumbai']
print(cities)
b = set(cities)
print(b)
print(list(set(cities)))