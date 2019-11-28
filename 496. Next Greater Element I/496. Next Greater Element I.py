class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}  
        for i,num in enumerate(nums2):
            hmap[num] = i
        final_arr = []
        for num in nums1:
            flag = True
            for i in range(hmap[num],len(nums2)):
                if nums2[i] > num:
                    final_arr.append(nums2[i])
                    flag = False
                    break
            if flag == True:
                final_arr.append(-1)
        return final_arr