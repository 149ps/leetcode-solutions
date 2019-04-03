def count_primes(n):
    nums=[1 for i in range(n+1)]
    p=2
    while (p*p <=n):
        if nums[p]==1:
            for i in range(p*2,n+1,p):
                nums[i]=0
        p+=1
    return nums.count(1)-2


print(count_primes(10))
    