from math import sqrt
def prime(num):
    if 0 not in [num % d for d in range (2,int(sqrt(num))+1)]:
        return 1
    else:
        return 0
def monisen(no):
    flag = 2
    x = 1
    a = []
    a.append(0)
    while x - 1 != no:
        if prime(flag) == 1:
            temp = 2**flag-1
            if prime(temp) == 1:
                a.append(temp)
                x += 1
        flag += 1
    return a[no]
print(monisen(int(input())))
