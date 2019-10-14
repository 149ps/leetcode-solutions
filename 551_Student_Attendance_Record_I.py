class Solution:
    def checkRecord(self, s: str) -> bool:
        return 'LLL' not in s and collections.Counter(s)['A']<=1
