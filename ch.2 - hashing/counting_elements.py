class Solution:
    def countElements(self, arr: List[int]) -> int:
        my_set = set(arr)
        ans = 0
        for i in arr:
            if i+1 in my_set:
                ans += 1
        return ans