# the bubble sort works on adjacent swaps
# the bubble sort works on adjacent swaps
# arr = [64, 34, 25, 12, 22, 11, 90]
arr = [1,2,3,4,5,6,7,8,9]
def bubble_sort(arr):
    n=len(arr)
    is_sorted=sorted(arr)
    if arr==is_sorted:
        return True
    else:   
        for i in range(n-2,-1,-1):
            for j in range(0,i+1):
                if arr[j]> arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
        
print(bubble_sort(arr))