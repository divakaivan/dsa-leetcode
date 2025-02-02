class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        def backtrack(curr, idx):
            if len(curr) == len(digits):
                ans.append("".join(curr))
                return
            curr_letters = dic[digits[idx]]
            for letter in curr_letters:
                curr.append(letter)
                backtrack(curr, idx+1)
                curr.pop()
        ans = []
        backtrack([], 0)
        return ans