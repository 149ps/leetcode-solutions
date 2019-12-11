class Solution:
    def longestWord(self, words: List[str]) -> str:
        result = ""
        wordset = set(words)
        print(wordset)
        for word in words:
            print(word)
            if len(word) > len(result):
                if all([word[:i] in wordset for i in range(1,len(word))]):
                    result = word
                    print("result: ",result)
            elif len(word) == len(result) and word < result:
                if all([word[:i] in wordset for i in range(1,len(word))]):
                    result = word
                    print("2nd result: ",result)
        return result