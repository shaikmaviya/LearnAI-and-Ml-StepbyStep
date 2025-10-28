# Creating and initializing an array
def findtheLargest(arr):
    largest = arr[0]
    for i in range (1, len(arr)):
        if arr[i] > largest:
            
            largest = arr[i]
    return largest

arr = [10, 20, 30, 40, 50]
print("The largest element is:", findtheLargest(arr))