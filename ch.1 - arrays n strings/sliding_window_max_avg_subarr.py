class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 0:
            return 0.0
        if k == 1:
            return float(max(nums))
        
        curr = 0 
        for i in range(k):
            curr += nums[i]
        
        ans = curr
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            ans = max(ans, curr)
            
        return ans / k