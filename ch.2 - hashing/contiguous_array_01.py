class Solution: #thanks neetcode
    def findMaxLength(self, nums: List[int]) -> int:
        zeros, ones = 0, 0
        res = 0
        diff_index = {} # count[1] - count[0] -> index
        
        for i, n in enumerate(nums):
            if n == 0;
                zeros += 1
            else:
                ones += 1
            if ones - zeros not in diff_index:
                diff_index[ones - zeros] = i
            
            if ones == zeros: # the longest starts at the beginning of the array
                res = ones + zeros 
            else:
                idx = diff_index[ones - zeros]
                res = max(res, i - idx)
        
        return res
            