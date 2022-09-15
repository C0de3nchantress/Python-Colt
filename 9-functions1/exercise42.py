# def speak(animal='dog'):
#     if animal == 'pig':
#         return 'oink'
#     elif animal == 'duck':
#         return 'quack'
#     elif animal == 'cat':
#         return 'meow'
#     elif animal == 'dog':
#         return 'woof'
#     return '?'

# def speak(animal='dog'):
    # noises = {'dog': 'woof', 'pig': 'oink', 'duck': 'quack', 'cat': 'meow'}
    # noise = noises.get(animal)
    # if noise:
        # return noise
    # return '?'

def speak(animal = 'dog'):
    noises = {'dog': 'woof', 'pig': 'oink', 'duck': 'quack', 'cat': 'meow'}
    return noises.get(animal, '?')
print(speak('ok'))