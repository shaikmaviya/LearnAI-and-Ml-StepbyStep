nums = [8,1,2,2,3]
class Solution:
    def smallerNumbersThanCurrent(self, nums) :
        output_list =[] 
        for i in nums:
            count = 0
            for j in nums:
                if i>j:
                    count = count + 1
            output_list.append(count)
        return output_list
print(Solution().smallerNumbersThanCurrent(nums))
                