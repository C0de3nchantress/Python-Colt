from unicodedata import name


instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "fav_language": "python",
    "is_hilarious": False,
    44: "My favorite number"    
}
if "name" in instructor:
    print(f"There is a name! it's {instructor['name']}")
else:
    print("There is no name")
if "phone" in instructor:
    print(f"There is a phone! it's {instructor['phone']}")
else:
    print("There is no phone :(")