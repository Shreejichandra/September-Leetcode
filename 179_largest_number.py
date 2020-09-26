# Given a list of non negative integers, arrange them such that they form the largest number.

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 0:
            return ""
        
        def compare(a, b):
            return int(str(b)+str(a)) - int(str(a)+str(b))
                    
        
        nums.sort(key = cmp_to_key(compare))
        #print(nums)        
        s = "".join(str(i) for i in nums)
        return str(int(s)     
        
