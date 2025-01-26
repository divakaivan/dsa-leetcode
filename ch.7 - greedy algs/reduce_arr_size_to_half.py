from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # Count frequencies of each element
        arr_counts = Counter(arr)
        sorted_counts = sorted(arr_counts.values(), reverse=True)

        target = len(arr) / 2
        removed_count = 0
        
        for count in sorted_counts:
            target -= count
            removed_count += 1
            if target <= 0:
                break
        
        return removed_count
        
        
        # max_heap = [(-count, num) for num, count in arr_counts.items()]
        # max_heap.sort(reverse=True)
        # ans = 0
        # target = len(arr) / 2
        # while target > 0:            
        #     most_occur = max_heap.pop()
        #     target += most_occur[0]
        #     ans += 1
        # return ans
        