import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1:
            return 0
        
        heap = sticks
        heapq.heapify(heap)
        cost = 0
        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
        
            combined = first + second
            cost += combined

            heapq.heappush(sticks, combined)
        
        return cost