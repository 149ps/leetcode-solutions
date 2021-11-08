"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.



Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.


Constraints:

1 <= words.length <= 500
1 <= words[i] <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]
"""
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