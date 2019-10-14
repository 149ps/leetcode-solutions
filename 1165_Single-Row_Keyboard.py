class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hmap = {}
        for i,char in enumerate(keyboard):
            if not char in hmap.keys():
                hmap[char] = i
        time = 0
        time+=hmap[word[0]]
        for i in range(len(word)-1):
            time+=abs(hmap[word[i+1]] - hmap[word[i]])
        return time
