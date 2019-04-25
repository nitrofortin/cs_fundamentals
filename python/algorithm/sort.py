def heap_sort(min_heap, array):
    sorted_array = []
    min_heap.heapify(array)
    while min_heap.get_size()>0:
        sorted_array.append(min_heap.delete_min())
    return sorted_array


def quick_sort():
    pass

def merge_sort(array):
    if len(array)>1:
        mid_idx = len(array)//2
        left_array = array[:mid_idx]
        right_array = array[mid_idx:]

        left_array = merge_sort(left_array)
        right_array = merge_sort(right_array)

        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i+=1
            else:
                array[k] = right_array[j]
                j+=1
            k+=1
    return array


def insertion_sort(array):
    for idx, current_value in enumerate(array):
        while idx > 0 and array[idx-1]>current_value:
            array[idx] = array[idx-1]
            idx -= 1
        array[idx] = current_value
    return array

