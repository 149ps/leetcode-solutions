import collections,functools
def longestWord(words):
    Trie = lambda: collections.defaultdict(Trie)
    print(Trie)
    trie = Trie()
    END = True

    for i, word in enumerate(words):
        print("get item: ",dict.__getitem__)
        print("word: ",word)
        print("trie: ",trie)
        print("")
        functools.reduce(dict.__getitem__, word, trie)[END] = i
    for k,v in trie.items():
        print(k,v)
    
    stack = list(trie.values())
    ans = ""
    while stack:
        cur = stack.pop()
        if END in cur:
            word = words[cur[END]]
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                ans = word
            stack.extend([cur[letter] for letter in cur if letter != END])

    return ans

print(longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple",'caa']))