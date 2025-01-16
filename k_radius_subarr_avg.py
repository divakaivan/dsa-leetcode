class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        if len(nums) == k or len(nums) < k+k+1 or len(nums) < k:
            return [-1] * len(nums)
        
        ans = [-1] * k
        curr = 0
        curr = sum(nums[:k+k+1])
        ans.append(curr // (k+k+1))
        
        for i in range(k+1, len(nums)-k):
            curr += nums[i + k] - nums[i - k - 1]
            ans.append(curr // (k+k+1))
        
        ans += [-1] * k
        
        return ans
    