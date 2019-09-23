def sum_3_zero(nums):
    triplets=[]
    nums.sort()
    for i in range(len(nums)-1):
        l=i+1
        r=len(nums)-1
        while l<r:
            sum=nums[i]+nums[l]+nums[r]
            if sum==0:
                if not [nums[i],nums[l],nums[r]] in triplets:
                    triplets +=[[nums[i],nums[l],nums[r]]]
            if sum<0:
                l+=1
            else:
                r-=1
    return triplets

nums=[-1, 0, 1, 2, -1, -4]
print(sum_3_zero(nums))
    