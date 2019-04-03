import math
def powerof_two(n):
    if n<=0 or n==1:
        return False
    print(int(math.log2(n)))
    if (math.log2(n)*2)%2==0:
        return True
    else:
        return False
    
print(powerof_two(1))