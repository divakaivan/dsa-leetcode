from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # stones_dic = Counter(stones)
        ans = 0
        # for i in jewels:
        #     if i in stones_dic.keys():
        #         ans += stones_dic[i]
        
        # beats 100% in running time, stil high in memory
        for i in stones:
            if i in set(jewels): # set is O(1) for lookup
                ans += 1
        
        return ans