class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        stack, result = [], []
        for num in nums2:
            while stack and stack[-1] < num:
                hmap[stack.pop()] = num
            stack.append(num)

        for num in nums1:
            result.append(hmap.get(num, -1))

        return result