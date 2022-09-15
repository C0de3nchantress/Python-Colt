num_list = [1,2,3,4]
num_dict = { num: ("even" if num % 2 ==0 else "odd") for num in range(1,100)}
print(num_dict)