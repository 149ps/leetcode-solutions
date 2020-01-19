"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        hmap = collections.Counter(A[0])
        temp_list = [] # list of keys which are not common for all the strings
        for string in A[1:]:
            temp_hmap = collections.Counter(string)
            for k,v in hmap.items():
                if temp_hmap.get(k):
                    hmap[k] = min(hmap[k],temp_hmap[k]) # We have to take common elements so take min of two strings
                else:
                    temp_list.append(k)
        
        for k in temp_list: # remove all the keys which are not common
            del hmap[k]
        return hmap.elements()