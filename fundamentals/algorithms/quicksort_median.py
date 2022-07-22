def choode_median(arr):
    leftmost_element_index = 0
    righmost_element_index = len(arr)-1
    middle_element_index = (leftmost_element_index + righmost_element_index)//2
    sorted_array_of_indices = sorted([leftmost_element_index,righmost_element_index,middle_element_index])
    #print(sorted_array_of_indices)
    return sorted_array_of_indices[1]#,arr[sorted_array_of_indices[1]]

def partition(arr,pivot_value):
    list_of_smaller_elements = []
    list_of_larger_elements = []
    list_of_elements_equl_to_pivot= []
    no_of_comparisons = 0
    for a in arr:
        if a  < pivot_value:
            list_of_smaller_elements.append(a)
            no_of_comparisons += 1
        elif a > pivot_value:
            list_of_larger_elements.append(a)
            no_of_comparisons += 1
        else:
            list_of_elements_equl_to_pivot.append(a)

    final_list = list_of_smaller_elements
    final_list.extend(list_of_elements_equl_to_pivot)
    final_list.extend(list_of_larger_elements)
    print("list of elements after partition is: ")
    print(final_list)
    print("computations so far: " + str(no_of_comparisons))
    return final_list.index(pivot_value)


test_list =  [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
#test_list = [2, 1, 3, 6, 5, 4, 9, 8, 7, 10, 20, 15, 11, 13, 16, 19, 14, 18, 17, 12][0:9]
#test_list = [2, 1, 3, 4, 5, 6, 9, 8, 7][0:4]
median_index = choode_median(test_list)
print("median element for input array is")
print(test_list[median_index])
index_of_pivot_value = partition(test_list,test_list[median_index])


def quicksort(arr,len_of_array):
    if len_of_array == 1:
        return arr
    pivot_index = choode_median(arr)
    pivot_index_partitioned_list = partition(arr,arr[pivot_index])
    left_half = arr[0:pivot_index_partitioned_list]
    right_half = arr[pivot_index_partitioned_list+1:]
    quicksort(left_half,len(left_half))
    quicksort(right_half,len(right_half))


print(quicksort(test_list,len(test_list)))
