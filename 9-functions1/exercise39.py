# def generate_evens():
#     a = []
#     for i in range(1,50):
#         if i %2 == 0:
#             a.append(i)
#     return a
# print(generate_evens())
def generate_evens():
    return [i for i in range(1,50) if i%2==0]
print(generate_evens())