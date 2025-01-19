class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        chars = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }
        for i in text:
            if i in ['b','a','l','l','o','o','n']:
                chars[i] += 1
            # 3, 1, 3, 4, 1
            # 1, 1, 2, 2, 1
            # -> 1 balloon
        res = [i // j for i, j in zip(chars.values(), [1,1,2,2,1])] 
        return min(res)
        
        