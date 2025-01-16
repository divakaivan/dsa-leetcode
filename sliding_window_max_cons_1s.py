class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
        left = curr = ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
    