# Given an unsorted integer array, find the smallest missing positive integer.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num1 = 0
        nums = list(set(nums))
        nums.sort()
        flag = 0
        for i in range(len(nums)):
            if nums[i] <= 0:
                continue    
            else:
                flag += 1
                if nums[i] - num1 != 1:
                    #print(nums[i], num1)
                    return num1+1
                else:
                    num1 = nums[i]
        if flag == 0:
            return 1
        return nums[i] + 1
                    
                    
            
        
