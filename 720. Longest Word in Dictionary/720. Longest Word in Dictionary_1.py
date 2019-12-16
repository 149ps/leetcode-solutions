import collections,functools
def longestWord(words):
    Trie = lambda: collections.defaultdict(Trie)
    print(Trie)
    trie = Trie()
    END = True

    for i, word in enumerate(words):
        functools.reduce(dict.__getitem__, word, trie)[END] = i
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