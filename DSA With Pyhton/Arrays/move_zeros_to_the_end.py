nums=[1,0,3,0,4,5]
n=len(nums)
count=0
for i in range(n):
    if nums[i] != 0:
        nums[count]=nums[i]
        count+=1
while count<n:
    nums[count]=0
    count+=1
        
        
        
        
print(nums)
                