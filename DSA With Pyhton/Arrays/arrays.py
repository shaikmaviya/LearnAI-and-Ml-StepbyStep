# import array as arr

# a = arr.array('i', [1, 2, 3, 4, 5])
# # print(a[0])
# # a.append(4)
# # print(a)


# # for i in range(0, 5):
# #     print(i, end=' ')

# # a.insert(1, 5)

# # print(*a)

# # a.append(4)
# # print(*a)


# # a.remove(5)
# # print(*a)

# # a.pop(1)
# # print(*a)
# slice = a[:]
# print(slice)

# import array
# arr = array.array('i', [1, 2, 3, 1, 2, 5])

# # index of 1st occurrence of 2
# print(arr.index())

# # index of 1st occurrence of 1
# print(arr.index(1))

# import array
# arr = array.array('i', [1, 2, 3, 4, 5])


# print("Reversed array:", *arr[::-1])

# a = arr.array('u', ['a', 'b', 'c', 'd', 'e'])
# print(a[0])



# a = arr.array('i', [1, 2, 3, 4, 5])
# # max_value = max(a)
# # min_value = min(a)
# # print(max_value,min_value)
# sum = 0


# for i in range(0, 5):
#     sum = sum + a[i]

# print(sum)
    
    
# def is_palindrome(arr):
#     # n = len(arr)
#     # for i in range(n // 2):  # Only need to check up to the middle of the array
#     #     if arr[i] != arr[n - i - 1]:  # Compare the element with its counterpart
#     #         return False
#     # return True
#     reversed=arr[::-1]
#     return arr==reversed

# # Input
# array = [4,1, 2, 3, 2, 1, 4]

# # Check if the array is a palindrome
# if is_palindrome(array):
#     print("The array is a palindrome.")
# else:
#     print("The array is not a palindrome.")


# def evenorodd(arr):
#     even = 0
#     odd = 0
#     for i in range(len(arr)):
#         if arr[i] % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     return even, odd

# # findevenandodd = evenorodd(a)
# # print(f"Even: {findevenandodd[0]}, Odd: {findevenandodd[1]}")

# string = arr.array('u', 'maviya')
# reversed = string[::-1]
# print("".join(reversed))

