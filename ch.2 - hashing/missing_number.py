class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # return sum(range(len(nums)+1)) - sum(nums)
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum