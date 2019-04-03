def majorityElement(nums):
    hash={}
    major=[]
    for num in nums:
        hash[num]=hash.get(num,0)+1
    for num,value in hash.items():
        if hash[num]>(len(nums)//3):
            major.append(num)
    return major


nums=[1,1,1,3,3,2,2,2]
print(majorityElement(nums))
            
    
        
            