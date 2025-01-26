# import heapq
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        # sorted nums = [1,2,4,5]
        # prefix = [1,3,7,12]
        # queries = [3,10,21]
        ans = []
        for q in queries:
            # count = 0
            # for num in nums:
            #     if num <= q:
            #         count += 1
            #     else:
            #         break
            # ans.append(count)
            idx = bisect.bisect_right(nums, q)
            ans.append(idx)
        return ans
        
#         min_heap = [num for num in nums].copy()
#         heapq.heapify(min_heap)
#         ans = []
#         for q in queries:
#             tmp = 0
#             min_heap_copy = min_heap.copy()
#             while min_heap_copy and q >= 0:
#                 max_val = heapq.heappop(min_heap_copy)
#                 if max_val <= q:
#                     q -= max_val
#                     tmp += 1
#             ans.append(tmp)

#         return ans