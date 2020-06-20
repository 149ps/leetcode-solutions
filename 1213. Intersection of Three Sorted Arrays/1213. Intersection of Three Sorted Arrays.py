"""
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.



Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.


Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i, j, k = 0, 0, 0
        result = []
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            max_element = max(arr1[i], arr2[j], arr3[k])
            if arr1[i] == arr2[j] == arr3[k]:
                result.append(arr1[i])
                i += 1
                j += 1
                k += 1
                continue
            while i < len(arr1) and arr1[i] < max_element:
                i += 1
            while j < len(arr2) and arr2[j] < max_element:
                j += 1
            while k < len(arr3) and arr3[k] < max_element:
                k += 1
        return result

