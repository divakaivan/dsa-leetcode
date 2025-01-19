from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dic = Counter(ransomNote)
        magazine_dic = Counter(magazine)

        for i in ransom_dic.keys():
            if i not in magazine_dic.keys():
                return False
            elif ransom_dic[i] > magazine_dic[i]:
                return False

        return True
        
            
        
        