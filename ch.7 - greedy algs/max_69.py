class Solution:
    def maximum69Number (self, num: int) -> int:
#         nums = [int(x) for x in str(num)]
#         swapped = [num]
        
#         for i in range(len(nums)):
#             tmp = nums.copy()
#             if tmp[i] == 6:
#                 tmp[i] = 9
#             else:
#                 tmp[i] = 6
#             swapped.append(int("".join(str(x) for x in tmp)))
        
#         return max(swapped)
        str_num = str(num)

        return int(str_num.replace('6', '9', 1))