def threesumclosest(nums,target):
    nums.sort()
    print(nums)
    for i in range(0,len(nums)-2):
        l=i+1
        r=len(nums)-1
        cur_sum=nums[i]+nums[l]+nums[r]
        closest_sum=
        
        while l<r:
            #print("Currrent sum is:" + str(cur_sum))
            if abs(cur_sum)<abs(closest_sum):
                closest_sum=cur_sum
                #print(closest_sum)
            if cur_sum<target:
                l+=1
                #print(l)
            else:
                r-=1
    return closest_sum

nums=[1,1,1,0]
print(threesumclosest(nums,-100))
            
