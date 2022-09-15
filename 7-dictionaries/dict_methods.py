#CLEAR
instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "fav_language": "python",
    "is_hilarious": False,
    44: "My favorite number"    
}
instructor.clear()
print(instructor)

#COPY
instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "fav_language": "python",
    "is_hilarious": False,
    44: "My favorite number"    
}
clone = instructor.copy()
print(clone)
print(clone == instructor)
print(clone is instructor)

#FROMKEYS
new = {}.fromkeys(['name','bio','age','email'], 'unknown')
print(new)

#GET
print(instructor.get('name'))
print(instructor.get('phone'))

#POP
print(instructor)
instructor.pop('owns_dog')
print(instructor)

#POPITEM
instructor.popitem()
print(instructor)
person = {"city": "Antigua"}

#UPDATE
person.update(instructor)
print(person)
person['name'] = "Pratham"
print(person)
person.update(instructor)
print(person)