"""
Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc" 
Explanation: The same letters are at least distance 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: "" 
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.
"""
import operator
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if not k:
            return s 
        count = collections.Counter(s)
        max_freq = 0
        result = []
        for key,val in count.items():
            max_freq = max(val,max_freq)
        """
        len(count) > 1 for case s = 'a' , k = 2
        """
        if (max_freq)*(k-1) >= len(s) and len(count) > 1: 
            return ""
        """
        In Python, Min heap is created by default. So if we want to build a max heap out of it. We have to take the negative values of the keys.
        """
        charFreq = [(-v,k) for k,v in count.items()]
        heapq.heapify(charFreq)
        while charFreq:
            temp,count1 = [],0
            for i in range(k):
                if charFreq:
                    item = heapq.heappop(charFreq)
                    result.append(item[1])
                    count1 +=1 
                    if item[0] < -1:
                        temp.append((item[0]+1,item[1]))
            if count1 < k and temp: # if count < k then there are still some chars left to arrange and makes impossible for us to arrange all characters.
                return ""
            for item in temp:
                heapq.heappush(charFreq,item)
        return ''.join(result)