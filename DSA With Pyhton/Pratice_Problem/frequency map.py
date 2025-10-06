# method 1
nums = [1, 2, 2, 3, 4, 4, 4, 5]
frequency_map = dict()

for i in range(len(nums)):
    if nums[i] in frequency_map:
        frequency_map[nums[i]] += 1
    else:
        frequency_map[nums[i]] = 1
print(frequency_map)


# method 2
frequency_map = dict()
n= len(nums)
for i in range(n):
    frequency_map[nums[i]] = frequency_map.get(nums[i], 0) + 1
print(frequency_map)