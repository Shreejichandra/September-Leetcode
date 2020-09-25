# Given a list of non negative integers, arrange them such that they form the largest number.

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 0:
            return ""
        
        for j in range(len(nums)):
            for i in range(len(nums) - j - 1):
                if str(nums[i]) + str(nums[i+1]) < str(nums[i+1])+str(nums[i]):
                    nums[i], nums[i+1] = nums[i+1], nums[i] 
                    #print(nums)
                
        s = "".join(str(i) for i in nums)
        if int(s) == 0:
            return "0"
        return s
           
    
                
        
        
