def missing_number(nums):
    l=0
    u=max(nums)
    length=u-l+1
    print(l,u,length)
    i=0
    while length!=0:
        if l+i in nums:
            i+=1
            length-=1
        else:
            return l+i
    return l+i
nums=[0]
print(missing_number(nums))
        
         
        
        
