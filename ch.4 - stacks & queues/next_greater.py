from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = deque()
        next_greater = {}
        # nums1 = [4,1,2]
        # nums2 = [1,3,4,2]
        # {
        #   1: 3,
        #   3: 4
        # }
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        return [next_greater.get(num, -1) for num in nums1]