'''Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        start = 0
        end = 0
        prod = 1
        ans = 0
        while end < len(nums):
            prod *= nums[end]
            
            while prod >= k:
                prod /= nums[start]
                start += 1 
            
            ans += end - start + 1
            end += 1   
            
        return ans
            
                    
            
        
