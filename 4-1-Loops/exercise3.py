for i in range(1,21):
    if i == 4 or i == 13:
        print(f"{i} is UNLUCKY!")
    elif i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")