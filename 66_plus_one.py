def Plus_One(nums):
    tmp=int(''.join(str(x) for x in nums))
    tmp+=1
    a=[int(i) for i in str(tmp)]
    return a

nums=[1,2,4,5,3,2,2,9]
print(Plus_One(nums))
    
