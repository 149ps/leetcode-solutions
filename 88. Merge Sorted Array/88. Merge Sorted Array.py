class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #copy m elements of nums1 into temp list
        nums1_1 = nums1[:m]
        #clear nums1 list
        nums1[:] = []
        # Take Two pointers initialized to 0.
        i,j = 0,0
        while i < m and j < n:
            if nums1_1[i] <= nums2[j]:
                nums1.append(nums1_1[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1
        if i < m:
            nums1[i+j:] = nums1_1[i:]
        if j < n:
            nums1[i+j:] = nums2[j:]