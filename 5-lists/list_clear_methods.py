#clear
first_list = ["hi", "this", "is", "an", "example"]
print(first_list)
first_list.clear()
print(first_list)

#pop
second_list = ["hi", "this", "is", "also", "an", "example"]
print(second_list)
second_list.pop()
print(second_list)
second_list.pop(3)
print(second_list)
last_word_second_list = second_list.pop() #I can store the popped word in a variable
print(second_list)
print(last_word_second_list)

#remove
third_list = ["pratham", "angie", "pratham", "kiwi", "shnaya"]
print(third_list)
third_list.remove("kiwi")
print(third_list)
third_list.remove("pratham")
print(third_list)
third_list.remove("pratham")
print(third_list)