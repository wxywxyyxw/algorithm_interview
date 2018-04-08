#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import datetime

# 字符串循环位移
# 方法： (x`y`)` = YX  如 x = ab y = cdef x`= ba y` = fedc  x`y`= bafedc  (x`y`)` = cdefab
def left_rotate_string(char_list,distance):
    list_left = char_list[:distance]
    list_right = char_list[distance:]
    new_list =   list_left[::-1] + list_right[::-1]
    return new_list[::-1]

# 最长公共子序列 LCS longest common subsequence
def lcs(str1,str2):
    pass

# 字符串匹配算法kmp
# https://blog.csdn.net/u010189459/article/details/30067705
def learn_kmp():

    def BF_Match(s, t):
        slen = len(s)
        tlen = len(t)
        if slen >= tlen:
            for k in range(slen - tlen + 1):
                i = k
                j = 0
                while i < slen and j < tlen and s[i] == t[j]:
                    i = i + 1
                    j = j + 1
                if j == tlen:
                    return k
                else:
                    continue
        return -1

    def KMP_Match_1(s, t):
        slen = len(s)
        tlen = len(t)
        if slen >= tlen:
            i = 0
            j = 0
            next_list = [-2 for i in range(len(t))]
            getNext_1(t, next_list)
            #print next_list
            while i < slen:
                if j == -1 or s[i] == t[j]:
                    i = i + 1
                    j = j + 1
                else:
                    j = next_list[j]
                if(j == tlen):
                    return i - tlen
        return -1

    def KMP_Match_2(s, t):
        slen = len(s)
        tlen = len(t)
        if slen >= tlen:
            i = 0
            j = 0
            next_list = [-2 for i in range(len(t))]
            getNext_2(t, next_list)
            #print next_list
            while i < slen:
                if j == -1 or s[i] == t[j]:
                    i = i + 1
                    j = j + 1
                else:
                    j = next_list[j]
                if j == tlen:
                    return i - tlen
        return -1

    def getNext_1(t, next_list):
        next_list[0] = -1
        j = 0
        k = -1
        while j < len(t) - 1:
            if k == -1 or t[j] == t[k]:
                j = j + 1
                k = k + 1
                next_list[j] = k
            else:
                k = next_list[k]

    def getNext_2(t, next_list):
        next_list[0] = -1
        next_list[1] = 0
        for i in range(2, len(t)):
            tmp = i -1
            for j in range(tmp, 0, -1):
                if equals(t, i, j):
                    next_list[i] = j
                    break
                next_list[i] = 0

    def equals(s, i, j):
        k = 0
        m = i - j
        while k <= j - 1 and m <= i - 1:
            if s[k] == s[m]:
                k = k + 1
                m = m + 1
            else:
                return False
        return True


    def rand_str(length):
        str_0 = []
        for i in range(length):
            str_0.append(random.choice("abcdefghijklmnopqrstuvwxyz"))
        return str_0

    def main():
        x = rand_str(2000000)
        y = rand_str(50)

        print "The String X Length is : ", len(x), " String is :",
        for i in range(len(x)):
            print x[i],
        print ""
        print "The String Y Length is : ", len(y), " String is :",
        for i in range(len(y)):
            print y[i],
        print ""

        time_1 = datetime.datetime.now()
        pos_1 = BF_Match(x, y)
        time_2 = datetime.datetime.now()
        print "pos_1 = ", pos_1

        time_3 = datetime.datetime.now()
        pos_2 = KMP_Match_1(x, y)
        time_4 = datetime.datetime.now()
        print "pos_2 = ", pos_2

        time_5 = datetime.datetime.now()
        pos_3 = KMP_Match_2(x, y)
        time_6 = datetime.datetime.now()
        print "pos_3 = ", pos_3

        print "Function 1 spend ", time_2 - time_1
        print "Function 2 spend ", time_4 - time_3
        print "Function 3 spend ", time_6 - time_5


#反转字符串
def reverse_string():
    s = u'abcdefghijk'

    #利用递归的方法： abcd -> bcd + a ->  cd + b + a -> d + c + b + a -> dcba 结束
    def func(s):
        if len(s) <1:
            return s
        return func(s[1:])+s[0]

    #利用栈实现 abcd -> d出栈 d -> c出栈 dc -> b出栈 dcb -> a出栈 dcba 结束
    def func2(s):
        l = list(s) #模拟全部入栈
        result = ""
        while len(l)>0:
            result += l.pop() #模拟出栈
        return result

    #普通的一个for循环
    def func3(s):
        result = ""
        max_index = len(s)-1
        for index,value in enumerate(s):
            result += s[max_index-index]
        return result
    result = func(s)

    result = func2(s)
    print result




if __name__ == '__main__':
   # print left_rotate_string(u'abcdef',3)
   reverse_string()