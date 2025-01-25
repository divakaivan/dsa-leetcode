import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sq_pts = [((pts[0] - 0)**2 + (pts[1] - 0)**2, pts) for pts in points]
        ans = []
        heapq.heapify(sq_pts)
        for _ in range(k):
            closest = heapq.heappop(sq_pts)
            ans.append(closest[1])
        
        return ans
        
        
        