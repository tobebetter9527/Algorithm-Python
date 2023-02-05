# author: tobebetter9527
# since: 2023/1/12 23:26
def remainder(x, a, p):
    rem = 1
    for i in range(a):
        print(i)
        rem = (rem * x) % p
    return rem


rem = remainder(3, 39, 1000000007)
print(rem)
