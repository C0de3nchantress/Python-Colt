# start
first_list = [1,2,3,4,5,6]
first_slice = first_list[1:]
print(first_slice)
first_slice = first_list[3:]
print(first_slice)
first_slice = first_list[-4:]
print(first_slice) 
first_slice = first_list[:]
print(first_slice)
print(first_list)
equal_check = first_list == first_slice
print(equal_check)
is_check = first_list is first_slice
print(is_check)

#end
second_list = [1,2,3,4]
second_slice = second_list[:2]
print(second_slice)
second_slice = second_list[:4]
print(second_slice)

#both start and end
second_slice = second_list [1:3]
print(second_slice)
second_slice = second_list[1:-1]
print(second_slice)

#steps (basically jumps you want to make, interval you want your slice to move at)
print(first_list)
third_slice = first_list[1::2]
print(third_slice)
third_slice = first_list[::2]
print(third_slice)

#negative steps
print(first_list)
third_slice = first_list[1::-1]
print(third_slice)
third_slice = first_list[:1:-1]
print(third_slice)
third_slice = first_list[2::-1]
print(third_slice)

#reversing strings
string = "This is fun"
reversed_string = string[::-1]
print(reversed_string)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
print(colors[5])
print(colors[5][::-1])
print(string[::3])
print(string[:4])