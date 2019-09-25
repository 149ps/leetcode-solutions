class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = dict(collections.Counter(magazine))
        for i in range(len(ransomNote)):
            if ransomNote[i] not in magazine_count.keys():
                return False
            else:
                if magazine_count[ransomNote[i]]==0:
                    return False
                magazine_count[ransomNote[i]]-=1
        return True
