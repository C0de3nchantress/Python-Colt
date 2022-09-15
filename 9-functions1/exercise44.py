# '''
# return_day(1) # "Sunday"
# return_day(2) # "Monday"
# return_day(3) # "Tuesday"
# return_day(4) # "Wednesday"
# return_day(5) # "Thursday"
# return_day(6) # "Friday"
# return_day(7) # "Saturday"
# return_day(41) # None
# '''

# def return_day(day):
#     days_dict = {
#         1: 'Sunday',
#         2:'Monday',
#         3: 'Tuesday',
#         4: 'Wednesday',
#         5: 'Thursday',
#         6: 'Friday',
#         7: 'Saturday'
#     }
#     return days_dict.get(day, None)
# print(return_day(8))

#With lists

# def return_day(num):
#     days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#     if num>0 and num<= len(days):
#         return days[num-1]
#     return None
# print(return_day(0))

#Lists advanced version

def return_day(num):
    try:
        return['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] [num-1]
    except IndexError as e:
        return None
print(return_day(9))