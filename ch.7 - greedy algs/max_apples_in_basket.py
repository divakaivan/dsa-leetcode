import heapq
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        if sum(weight) <= 5000:
            return len(weight)
        
        ans = cur_weight = 0
        heapq.heapify(weight)
        while weight:
            max_weight = heapq.heappop(weight)
            if cur_weight + max_weight <= 5000:
                cur_weight += max_weight
                ans += 1
            else: 
                break
            
        return ans
            