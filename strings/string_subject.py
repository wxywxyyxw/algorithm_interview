#!/usr/bin/python
# -*- coding: utf-8 -*-

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
if __name__ == '__main__':
    print left_rotate_string(u'abcdef',3)
