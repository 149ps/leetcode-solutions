class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def issub(x,y):
            i,j = 0,0
            while i < len(x) and j < len(y):
                if x[i] == y[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return j == len(y)
        longest_string = ''
        for string in d:
            if issub(s,string):
                if len(string) > len(longest_string):
                    longest_string = string
                if len(string) == len(longest_string):
                    if ord(string[0]) < ord(longest_string[0]):
                        longest_string = string 
        return longest_string