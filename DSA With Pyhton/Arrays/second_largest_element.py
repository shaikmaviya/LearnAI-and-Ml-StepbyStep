# # Creating and initializing an array
# arr = [10, 20, 30, 40, 50,65,3,4,2]

# # x= sorted(arr)
# # print("Second largest element is:", x[-2])

# def second_largest(arr):
#     largest = second_largest = arr[0]
#     for i in arr:
#         if i > largest:
#             second_largest = largest
#             largest = i
#         elif i > second_largest and i != largest:
#             second_largest = i
#     return second_largest

# print("Second largest element is:", second_largest(arr))


# sorted_arr = sorted(arr)


# Creating and initializing an array
arr = [10, 20, 30, 40, 50,65,3,4,2]

# x= sorted(arr)
# print("Second largest element is:", x[-2])

def second_largest(arr):
    largest = second_largest = arr[0]
    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i
    return second_largest

print("Second largest element is:", second_largest(arr))


sorted_arr = sorted(arr)