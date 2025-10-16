nums = [-1,-100,3,99]
k=2
n=len(nums)
k=k%n
nums[:] = nums[n-k:] + nums[:n-k]
print(nums)



