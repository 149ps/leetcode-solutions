def reverse_integer(x):
    if x<0:
        x=int(str(x)[::-1][-1] + str(x)[::-1][:-1])
    if x>=0:
        x=int(str(x)[::-1][:])
    if abs(x) > 0x7FFFFFFF:
        return 0
    return x

i=-12389589999999999999999
print(reverse_integer(i))