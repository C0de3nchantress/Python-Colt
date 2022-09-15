instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "fav_language": "python",
    "is_hilarious": False,
    44: "My favorite number"    
}
for value in instructor.values():
    print(value)
print(instructor.values())

print("KEYS UNDER\n")

for k in instructor.keys():
    print(k)
print(instructor.keys())

print("BOTH  UNDER HERE\n\n")

a = instructor.items()
for values,keys in a:
    print(f"The values are: {values}, The keys are: {keys}")
print(a)