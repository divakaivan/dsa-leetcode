import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)
        for i in range(k):
            max_pile = heapq.heappop(heap)
            heapq.heappush(heap, floor(max_pile/2))
        return abs(sum(heap))