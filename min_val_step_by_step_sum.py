class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # in: nums = [2,3,6] out: ? -> 
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        min_nums = min(nums)
        if min_nums < 0:
            ans = abs(min_nums) + 1
        else:
            ans = 1
            
        return ans