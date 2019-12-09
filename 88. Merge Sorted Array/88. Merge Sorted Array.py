class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_temp = nums1[:m]
        nums1[:] = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1_temp[i] <= nums2[j]:
                nums1.append(nums1_temp[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1
        if i < m:
            nums1[i+j:] = nums1_temp[i:]
        if j < n:
            nums1[i+j:] = nums2[j:]
        return nums1