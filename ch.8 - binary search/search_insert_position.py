class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # nums = [1,3,5,6], target = 2
        #         0,1,2,3
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
            