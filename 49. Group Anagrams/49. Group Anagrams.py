"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for string in strs:
            if not hmap.get(tuple(sorted(string))):
                hmap[tuple(sorted(string))] = [string]
            else:
                hmap[tuple(sorted(string))].append(string)
        return hmap.values()