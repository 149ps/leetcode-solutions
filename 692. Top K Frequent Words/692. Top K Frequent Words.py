class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hmap_sorted = sorted(collections.Counter(words).items(), key = lambda w:(-w[1],w[0]))
        return [k[0] for k in hmap_sorted[:k]]