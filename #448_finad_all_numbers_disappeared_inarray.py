def find_disappeared(nums):
    max_num=max(nums)
    min_num=min(nums)
    missing=[]
    for i in range(1,max_num-min_num+1):
        if i in nums:
            continue
        else:
            missing+=[i]
    return missing