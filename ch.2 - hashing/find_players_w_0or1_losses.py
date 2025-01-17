# 1st accepted solution O(nlogn) time, O(n) space
# from collections import defaultdict
#
# class Solution:
#     def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
#         winners = defaultdict(int)
#         losers = defaultdict(int)
#         for match in matches:
#             winners[match[0]] += 1
#             losers[match[1]] += 1
#        
#         winners_list = [i for i in winners.keys() if i not in losers.keys()]
#         losers_list = [i for i in losers.keys() if losers[i] == 1]
#        
#         return [sorted(winners_list), sorted(losers_list)]
        
# 2nd accepted; way better runtime (top 10%)
# from collections import Counter
# 
# class Solution:
#     def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
#         winners = set(i[0] for i in matches)
#         lost_counts = Counter([i[1] for i in matches])
#         losers = [item for item, count in lost_counts.items() if count == 1]
        
#         return [sorted(list(winners - lost_counts.keys())), sorted(losers)]
        