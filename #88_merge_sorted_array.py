def Merge_sort_array(nums1,m,nums2,n):
    nums1=nums1[:m]
    nums1.extend(nums2[:n])
    nums1.sort()
    return nums1

nums1=[1,2,3,0,0,0]
nums2=[2,5,6,8]

print(Merge_sort_array(nums1,3,nums2,3))