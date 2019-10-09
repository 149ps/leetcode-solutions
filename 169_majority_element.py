"""def majorityElement(nums):
        nums=sorted(nums)
        print(nums)
        n=len(nums)
        print("n is: " + str(n))
        m=n//2
        print("m is: " + str(m))
        i=0
        while i<=m:
            print(nums[i]==nums[i+m])
            if nums[i]==nums[i+m]:
                return (nums[i])
            i+=1


nums=[3,2,3]
print(majorityElement(nums))
"""
#Moore Voting Algo
def majorityElement(nums):
    majority_index=0
    count=1
    for index in range(1,len(nums)):
        if nums[index]==nums[majority_index]:
            count+=1
        else:
            count-=1
        if count==0:
            majority_index=index
            count=1
    f_count=0
    for num in nums:
        if num==nums[majority_index]:
            f_count+=1
    if f_count>(len(nums)//2):
        return nums[majority_index]
nums=[1,1,1,3,3,2,2,2]
print(majorityElement(nums))

