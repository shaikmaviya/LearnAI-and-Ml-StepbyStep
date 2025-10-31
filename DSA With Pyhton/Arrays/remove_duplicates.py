nums = [1,2,2,3,4,4,5,6,7,8,8,9]

frequency = {}
n=len(nums)
for i in range(0,n):
    frequency[nums[i]] = 0
j=0
for k in frequency:
    nums[j]=k
    j+=1
    
    
    
    
    
    
print("Length of array after removing duplicates:",len(frequency))
print(nums)

    