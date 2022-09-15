'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(list = []):
    true_values = [i for i in list if i]
    return true_values
print(compact([0,1,2,"",[], False, {}, None, "All done"]))