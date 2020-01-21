class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hmap = collections.Counter(words)
        result = [(-val,key) for key,val in hmap.items()]
        heapq.heapify(result)
        final_result = []
        while len(final_result) < k:
            final_result.append(heapq.heappop(result)[1])
        return final_result

#nlogk solution
"""
Create Hahsmap
Create a new array having tuples of negative frequency and word in a tuple.

Why Negative Frequency?

Since we are using Min heap in python by default, and keys will be alphabetically sorted , it makes sense to use negative frequency.

Extract the first k elements from min heap which contains sorted frequencies and sorted words in aalphabetical order.
"""