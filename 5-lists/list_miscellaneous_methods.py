#index
first_list = [5,5,6,7,5,8,8,9,10]
print(first_list)
print(first_list.index(6)) #returns the value of the first item of the name provided in the list.
print(first_list.index(5,1))
print(first_list.index(5,2)) #the second number is the starting point from where it will start finding the number, ignoring everything behind the starting point.
print(first_list.index(8, 6, 8)) # the  third number is the ending point and our index will ignore everything after it

#count
print(first_list.count(5))
print(first_list.count(8))
print(first_list.count(69))#literally just counts the no. of times the value repeats itself


#reverse
first_list.reverse()
print(first_list)


#sort
first_list.sort()
print(first_list)
second_list = ["pratham", "kiwi", "shnaya", "angie"]
print(second_list)
second_list.sort()
print(second_list)
second_list.append("ANGIE")
print(second_list)
second_list.sort()
print(second_list)

#join
third_list = ["coding", "is", "fun"]
print(" ".join(third_list)) # concatentates the values and the value before the .join() is what will be added between the strings/other data type
fourth_list = ["Mr", "Pratham"]
print(". ".join(fourth_list))
friends = ", ".join(second_list)
print(f"I am friends with: {friends}")