# number  = 0 #This is a global variable
# def num():
    # number +=1 #this will show an error since number is a variable outside the function
    # return number
# print(num())
# 

# def num():
#     number = 0
#     number +=1
#     return number #this will not show an error because number is a variable inside the function
# print(num())

#another way to increment global variables is:
number = 0
def num():
    global number #this is how you import global varibales, you use the global function
    number +=1
    return number
print(num())


#NON LOCAL FUNCTION

def outer():
    count = 0
    def inner():
        nonlocal count #you use non local whenever you have to import a variable from the parent variable into the nested variable
        count +=6
        return count
    return inner()
print(outer())
