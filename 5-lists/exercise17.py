sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]


# Define your code below:
length = 0
result = ""
while length < len(sounds):
    result += sounds[length].upper()
    print(result)
    length +=1