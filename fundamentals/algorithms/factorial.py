# def factorial(num):
#     if num == 1:
#         return num
#     return num*factorial(num-1)
#
# fact4 = factorial(3)
# print(fact4)


def print_recursively(arr):
    if len(arr) == 1:
        print(arr)
        return
    print_recursively(arr[1:])

arr = [1,2,3,4,5]
print_recursively(arr)
