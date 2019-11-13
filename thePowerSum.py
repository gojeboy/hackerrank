# import sys
#
# num1,num2 = int(input()),int(input())
# def power_sum(num,count,total,pair_count):
#     powered_num = num**num2
#     if powered_num==total:
#         return pair_count+1
#     if powered_num < total:
#         return power_sum(num+1,count-1,total-powered_num,pair_count) + power_sum(num+1,count,total,pair_count)
#     return pair_count
#
# limit=(num1**(1/float(num2)))
#
# print(limit)
# print(power_sum(1,limit,num1,0))


# X = 100
# N = 2
#
#
def rec(X, N, start):
    count = 0
    for i in range(start, X):
        ans = X - i ** N
        print(ans)
        if ans == 0:
            count += 1
        if ans > 0:
            count += rec(ans, N, i + 1)
        if ans < 0:
            continue
    return count
#
#
# print(rec(X, N, 1))

total = 10

def rec_dummy(n, m):
    if n+m ==total:
        return total
    else:
        return rec_dummy(2,4)


rec_dummy(4,7)