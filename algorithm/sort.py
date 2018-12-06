def heap_sort(min_heap, array):
    sorted_array = []
    min_heap.heapify(array)
    while min_heap.get_size()>0:
        sorted_array.append(min_heap.delete_min())
    return sorted_array


def quick_sort():
	pass

def merge_sort():
	pass

def insertion_sort(array):
	for idx, current_value in enumerate(array):
		while idx > 0 and array[idx-1]>current_value:
			array[idx] = array[idx-1]
			idx -= 1
		array[idx] = current_value
	return array

