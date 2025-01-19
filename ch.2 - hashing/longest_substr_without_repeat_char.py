class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = ''
        ans = len(curr)
        left = 0
        for right in range(len(s)):
            while s[right] in curr:    
                curr = curr[1:]
                left += 1
            curr += s[right]
            ans = max(ans, right - left + 1)
        return ans
