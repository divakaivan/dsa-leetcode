class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # nums = [1,2,5,9], threshold = 6
        def check(divisor):
            return sum(ceil(i/divisor) for i in nums) <= threshold
        
        left = 1
        right = 10**6
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
        