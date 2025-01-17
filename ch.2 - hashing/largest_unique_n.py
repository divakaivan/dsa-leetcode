# 1st accepted: beats 100% of submissions, beats 20% of submissions in memory usage
# from collections import Counter

# class Solution:
#     def largestUniqueNumber(self, nums: List[int]) -> int:
#         dic = Counter(nums)
#         occurred_once = [i for i in dic.keys() if dic[i] == 1]
        
#         return max(occurred_once) if occurred_once != [] else -1