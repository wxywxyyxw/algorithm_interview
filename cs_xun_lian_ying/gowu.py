#!/usr/bin/env python3

# n,m,k = map(int, input().split(' '))
# w_list =[int(x) for x in input().split(' ')]

n,m,k  = 160,8, 234
w_list = [116, 7, 34, 67, 10, 124, 54, 74]


def money(k,m,w_list,max_len):
    if max_len >= m:
        if k > 0:
            return 0
        else:
            return 1
    else:
        count = 0
        #print (max_len)
        for i in range(w_list[max_len]):
            count +=  money(k-i,m,w_list,max_len+1)
        return count

print (money(k,m,w_list,0) %(1000000000+7))





