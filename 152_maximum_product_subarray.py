#Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = nums[0]
        prev_min = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            curr_max = max(nums[i], prev_max*nums[i], prev_min*nums[i])
            curr_min = min(nums[i], prev_max*nums[i], prev_min*nums[i])
            
            ans = max(curr_max, ans)
            prev_max = curr_max
            prev_min = curr_min
            
            #print(prev_max, prev_min)
        return ans
