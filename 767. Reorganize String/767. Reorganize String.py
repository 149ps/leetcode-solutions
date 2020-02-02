"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""
class Solution:
    def reorganizeString(self, S: str) -> str:
        hmap = collections.Counter(S)
        max_freq = 0
        final_list = []
        for key,val in hmap.items():
            max_freq = max(val,max_freq)
        if max_freq > (len(S)+1)/2:
            return ""
        charFreq = [(-v,k) for k,v in hmap.items()]
        heapq.heapify(charFreq)
        while len(charFreq) >= 2:
            item1 = heapq.heappop(charFreq)
            item2 = heapq.heappop(charFreq)
            final_list.extend([item1[1],item2[1]])
            if item1[0] < -1:
                heapq.heappush(charFreq,(item1[0]+1,item1[1]))
            if item2[0] < -1:
                heapq.heappush(charFreq,(item2[0]+1,item2[1]))
        return ''.join(final_list) + (charFreq[0][1] if charFreq else '')
