class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def min_subarrs_required(mid: int) -> int:
            cur_sum = 0
            cur_splits = 0
            
            for element in nums:
                if cur_sum + element <= mid:
                    cur_sum += element
                else:
                    cur_sum = element
                    cur_splits += 1

            return cur_splits + 1

        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (left + right) // 2
            
            if min_subarrs_required(mid) <= k:
                right = mid - 1
                min_max_sum = mid
            else:
                left = mid + 1
        
        return min_max_sum