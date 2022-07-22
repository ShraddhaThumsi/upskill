def choose_median(arr):
    leftmost_element_index = 0
    righmost_element_index = len(arr)-1
    middle_element_index = (leftmost_element_index + righmost_element_index)//2
    sorted_array_of_indices = sorted([leftmost_element_index,righmost_element_index,middle_element_index])
    #print(sorted_array_of_indices)
    return sorted_array_of_indices[1]

# def partition(arr,left_index,right_index):
#     print("array before partitioning")
#     print(arr)
#     pivot_value = arr[left_index]
#     print("pivot value is: " + str(pivot_value))
#     i = left_index+1
#     print("starting index of smaller numbers: " + str(i))
#     for j in range(left_index+1,right_index+1):
#         while arr[left_index+1] < arr[left_index]:
#             if arr[j] < pivot_value:
#                 temp = arr[j]
#                 arr[j] = arr[i]
#                 arr[i] = temp
#                 i += 1
#     temp2 = arr[left_index]
#     arr[left_index] = arr[i-1]
#     arr[i-1] = temp2
#     print("array after partitioning")
#     print(arr)

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
    arr = final_list

test_list =  [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
n = len(test_list)
median_index = choose_median(test_list)
print("median element for input array is")
print(test_list[median_index])
partition(test_list,0,len(test_list)-1)

def quicksort(arr,l):
    if l == 1:
        return
    pivot_index = choose_median(arr)
    partition(arr,0,pivot_index-1)
    partition(arr,pivot_index+1,l-1)

quicksort(test_list,n)
