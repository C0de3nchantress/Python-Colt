def combine_words(word, **kwargs):
    if 'suffix' in kwargs:
        return word+ kwargs['suffix']
    elif 'prefix' in kwargs:
        return kwargs['prefix']+word
    return word
print(combine_words("child", suffix="ish"))