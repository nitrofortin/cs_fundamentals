class SearchException(Exception):
    pass

def sequential_search(array, value_to_find):
    if not len(array):
        raise SearchException('Emtpy array')

    for current_value in array:
        if current_value == value_to_find:
            return True
    return False

def binary_search(sorted_array, value_to_find):
    if not len(sorted_array):
        raise SearchException('Emtpy array')
    
    cut_array = sorted_array
    cut_idx = len(sorted_array)//2
    found = False
    while len(cut_array)>0:
        if value_to_find > cut_array[cut_idx]:
            cut_array = cut_array[cut_idx+1:]
        elif value_to_find < cut_array[cut_idx]:
            cut_array = cut_array[:cut_idx]
        else:
            found = True
            break
        cut_idx = len(cut_array)//2
    return found

