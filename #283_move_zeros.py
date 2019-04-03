def moveZeroes(nums):
    for i in range(len(nums)):
        if nums[i]==0:
            nums+=[nums.pop(i)]
    return nums
            
nums=[0,1,0,3,12]
print(moveZeroes(nums))
        
            
    
         